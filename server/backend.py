import os
import json
from flask_cors import cross_origin
from google import genai
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, make_response, request
import requests

load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']
mongoclient = MongoClient(MONGODB_URI)
db = mongoclient['safestreets']
collection = db['users']
# user = collection.find_one({'_id': ObjectId('67f2131fe0ada19c46a3b9d3')})

app = Flask(__name__)

gemini_API_KEY = os.environ['gemini_API_KEY']
client = genai.Client(api_key=gemini_API_KEY)

@app.route('/calculate', methods=['POST'])
@cross_origin()
def calculate(whereto='los angeles', budget=200):
    whereto = request.json.get('whereto', '')
    budget = request.json.get('budget', '')

    if whereto == 'feelinglucky':
        prompt = f"Provide a 1-day itinerary for one person for a trip to San Francisco. The itinerary should include the following: Morning, Afternoon, Evening as keys for a dictionary. The itinerary should be in a dictionary format with each day as a new key. Mention approximate prices for everything. Make sure the itinerary is under the budget of ${budget}. The response should be in json format. The format is as follows: {{'morning': {{'location': '', 'activity': '', 'cost': '', 'description': ''}}, 'afternoon': {{'location': '', 'activity': '', 'cost': '', 'description': ''}}, 'evening': {{'location': '', 'activity': '', 'cost': '', 'description': ''}}}}. No other keys or values are required. Please just give me this much json."
    else:
        prompt = f"Provide a 1-day itinerary for one person for a trip to {whereto}. The itinerary should include the following: Morning, Afternoon, Evening as keys for a dictionary. The itinerary should be in a dictionary format with each day as a new key. Mention approximate prices for everything. Make sure the itinerary is under the budget of ${budget}. The response should be in json format. The format is as follows: {{'morning': {{'city': '', 'location': '', 'activity': '', 'cost': '', 'description': ''}}, 'afternoon': {{'city': '', 'location': '', 'activity': '', 'cost': '', 'description': ''}}, 'evening': {{'city': '', 'location': '', 'activity': '', 'cost': '', 'description': ''}}}}. No other keys or values are required. Please just give me this much json."

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    res = response.json()
    res1 = json.loads(res)
    res2 = res1['candidates'][0]['content']['parts'][0]['text']
    cleaned = res2.strip('"')
    cleaned = cleaned.replace('\\n', '\n').replace('\\"', '"')
    cleaned = cleaned.replace("```json", "").replace("```", "").strip()
    parsed_json = json.loads(cleaned)

    response = make_response(parsed_json, 200)
    return response

@app.route('/get_user', methods=['GET'])
@cross_origin()
def get_user():
    user = collection.find_one({'_id': ObjectId('67f2131fe0ada19c46a3b9d3')})
    print('user:', user)
    user['_id'] = str(user['_id'])
    user['home_city'] = user['home_city']
    user['search_history'] = user['search_history']
    return user, 200



@app.route('/get_crimes', methods=['GET'])
@cross_origin()
def get_crimes():
    url = "https://spotcrime.com/CA/Los%20Angeles"
    headers = {
        'Cookie': '_spotcrime_key=SFMyNTY.g3QAAAADbQAAAAtfY3NyZl90b2tlbm0AAAAYMjBlRGxURnlpd29GMkdQMEVheDI4MUtnbQAAAA5sYXN0X3Bpbl9sb2dpbnQAAAANZAAKX19zdHJ1Y3RfX2QAD0VsaXhpci5EYXRlVGltZWQACGNhbGVuZGFyZAATRWxpeGlyLkNhbGVuZGFyLklTT2QAA2RheWEGZAAEaG91cmEGZAALbWljcm9zZWNvbmRoAmIADbuPYQZkAAZtaW51dGVhIGQABW1vbnRoYQRkAAZzZWNvbmRhNWQACnN0ZF9vZmZzZXRhAGQACXRpbWVfem9uZW0AAAAHRXRjL1VUQ2QACnV0Y19vZmZzZXRhAGQABHllYXJiAAAH6WQACXpvbmVfYWJicm0AAAADVVRDbQAAAAp1c2VyX3Rva2VubQAAACRkNTU2NDNhYS1jNmIwLTQ5MWEtYmRlMy04OTNhZWUxODJiMDg.2QObcaG5athpv7eFLXLDXui8UiA96hFuO7EJReXVGcA'
    }
    response = requests.get(url, headers=headers)
    # print(response)
    startQueryString = r'var crimes ='
    endQueryString = r'window.initCrimePage(crimes, 34.05329, -118.245009, "area-page__map");'
    startIndex = response.text.find(startQueryString)
    endIndex = response.text.find(endQueryString)
    crimesString = response.text[startIndex + len(startQueryString): endIndex]
    crimes = json.loads(crimesString.strip()[:-1])
    return crimes



if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')