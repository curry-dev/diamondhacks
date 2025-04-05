from google import genai
from google.genai import types
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:4200", "http://127.0.0.1:4200"], "methods": ["GET", "POST", "OPTIONS"]}}, allow_headers=["Access-Control-Allow-Methods", "Access-Control-Allow-Origin", "Content-Type", "Access-Control-Allow-Headers"], supports_credentials=True)

gemini_API_KEY = os.environ['gemini_API_KEY']
client = genai.Client(api_key=gemini_API_KEY)



# @app.route('/calculate', methods=['GET', 'POST'])
# def calculate():
#     fetched_prompt = request.json.get('prompt', '')
#     fetched_prompt = fetched_prompt if fetched_prompt.strip() != '' else 'get me an outfit'
#     print('fetched_prompt:', fetched_prompt)
#     additional_prompt = 'Just give the keywords of the outfit that tell what i should wear in terms of clothing. For example: tee, leather jacket, jeans. No text decoration. Just comma separated words. The request is: '
#     response = client.models.generate_content(
#         model="gemini-2.0-flash",
#         contents= additional_prompt + fetched_prompt,
#     )

#     # make an array of keywords from the response
#     prompt1 = 'Generate a python list containing the suggested outfit keywords from the response attached. Replace each element in the list with the closest option from this list: [Blouses_Shirts, Cardigans, Denim, Dresses, Graphic_Tees, Jackets_Coats, Leggings, Pants, Rompers_Jumpsuits, Shorts, Skirts, Sweaters, Sweatshirts_Hoodies, Tees_Tanks, Jackets_Vests, Shirts_Polos, Suiting]. Only respond with the list and nothing else. Display the result as comma separated words. Use this response to generate the list: ' + response.text
#     getKeywords = client.models.generate_content(
#         model="gemini-2.0-flash",
#         contents=prompt1,
#     )
    
#     # look for keywords_array elements in the database
#     chosen_outfit = []
#     approved_keywords_men = ['Denim', 'Pants', 'Sweaters', 'Sweatshirts_Hoodies', 'Tees_Tanks', 'Jackets_Vests', 'Shirts_Polos', 'Suiting', 'Shorts']
#     approved_keywords_women = ['Blouses_Shirts', 'Cardigans', 'Denim', 'Dresses', 'Graphic_Tees', 'Jackets_Coats', 'Leggings', 'Pants', 'Rompers_Jumpsuits', 'Shorts', 'Skirts', 'Sweaters', 'Sweatshirts_Hoodies', 'Tees_Tanks']
#     keywords = getKeywords.text.split(',')
#     selectedGender = request.json.get('selectedGender', 'WOMEN')
#     selectedGender = 'MEN' if selectedGender == 'male' else 'WOMEN'
#     approved_keywords = approved_keywords_men if selectedGender == 'MEN' else approved_keywords_women
    
#     print('keywords:', keywords, 'selectedGender: ', selectedGender)
#     for keyword in keywords:
#         if len(chosen_outfit) == 3:
#             break
        
#         keyword = keyword.strip().replace('\n', '')
#         if keyword not in approved_keywords:
#             continue
        
#         front_occurrences = collection.find({'gender': selectedGender, 'outfit_type': keyword, 'filename': {"$regex": re.escape('front')}})
#         chosen_front = random.choice(list(front_occurrences))
#         chosen_outfit.append(chosen_front['cloudinary_url'])

#     return jsonify({'response': response.text, 'chosen_outfit': chosen_outfit})



if __name__ == '__main__':
    app.run(debug=True)