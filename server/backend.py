from google import genai
from google.genai import types
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from pprint import pprint
import os
from dotenv import load_dotenv
from pymongo import MongoClient



load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']
mongoclient = MongoClient(MONGODB_URI)
db = mongoclient['safestreets']
collection = db['users']
# print(collection.find_one({'ObjectId': '67f1d5b4f9efe9e5290971b9'}))
local_user = {
    'name': 'Devankshi',
    'home_city': 'Los Angeles',
    'search_history': [
        {
            'city': 'Los Angeles',
            'timestamp': '2023-10-01T12:00:00Z'
        },
        {
            'city': 'San Diego',
            'timestamp': '2023-10-02T15:30:00Z'
        }
    ]
}



app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:4200", "http://127.0.0.1:4200"], "methods": ["GET", "POST", "OPTIONS"]}}, allow_headers=["Access-Control-Allow-Methods", "Access-Control-Allow-Origin", "Content-Type", "Access-Control-Allow-Headers"], supports_credentials=True)

gemini_API_KEY = os.environ['gemini_API_KEY']
client = genai.Client(api_key=gemini_API_KEY)



@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    fetched_prompt = request.json.get('prompt', '')
    fetched_prompt = fetched_prompt if fetched_prompt.strip() != '' else 'suggest any city in California for a trip'
    print('fetched_prompt:', fetched_prompt)
    additional_prompt = 'Please suggest a city in California for a trip. The city should be a popular tourist destination with good weather and interesting attractions. Just give me the name of the city.'
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents= fetched_prompt,
    )
    chosen_city = response.text

    return jsonify({'response': response.text, 'chosen_city': chosen_city})



if __name__ == '__main__':
    app.run(debug=True)