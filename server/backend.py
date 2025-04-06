import os
import json
from flask_cors import cross_origin
from google import genai
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, make_response, request

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
    print(f"Received request: {request.method}")
    print(f"Headers: {request.headers}")

    whereto = request.json.get('whereto', '')
    budget = request.json.get('budget', '')
    # whereto = whereto if whereto.strip() != '' else 'Los Angeles'
    # budget = budget if budget else 500

    prompt = f"Provide a 1-day itinerary for one person for a trip to {whereto}. The itinerary should include the following: Morning, Afternoon, Evening as keys for a dictionary. The itinerary should be in a dictionary format with each day as a new key. Mention approximate prices for everything. Make sure the itinerary is under the budget of ${budget}. The response should be in json format. The format is as follows: {{'morning': {{'activity': '', 'cost': '', 'description': ''}}, 'afternoon': {{'activity': '', 'cost': '', 'description': ''}}, 'evening': {{'activity': '', 'cost': '', 'description': ''}}}}. No other keys or values are required. Please just give me this much json."

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

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')