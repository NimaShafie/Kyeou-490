from flask import Flask, request, jsonify
import json


app = Flask(__name__)

@app.route('/<string:subject>/<string:data>')
def get(**kwargs):
    return json.load(open('./json_' + kwargs["data"] +  '/' + kwargs["subject"].upper() + '_' + kwargs["data"] + '.json'))

@app.route('/<string:subject>/rating', methods=['POST'])
def new_rating(**kwargs):
    current_ratings = json.load(open('./json_' + 'rating' +  '/' + kwargs["subject"].upper() + '_' + 'rating' + '.json'))
    file1 = open('./json_' + 'rating' +  '/' + kwargs["subject"].upper() + '_' + 'rating' + '.json', "w")
    new_rating = request.get_json(force=True) 
    print ('Post Body:', new_rating)
    try:
        current_ratings[new_rating["professor_first_name"][0:1].upper() + 
                        new_rating["professor_first_name"][1:].lower() + " " + 
                        new_rating["professor_last_name"][0:1].upper() + 
                        new_rating["professor_last_name"][1:].lower()].append(new_rating)
    except KeyError:
        current_ratings[new_rating["professor_first_name"][0:1].upper() + 
                        new_rating["professor_first_name"][1:].lower() + " " + 
                        new_rating["professor_last_name"][0:1].upper() + 
                        new_rating["professor_last_name"][1:].lower()] = []
        
        current_ratings[new_rating["professor_first_name"][0:1].upper() + 
                        new_rating["professor_first_name"][1:].lower() + " " + 
                        new_rating["professor_last_name"][0:1].upper() + 
                        new_rating["professor_last_name"][1:].lower()].append(new_rating)
    
    json.dump(current_ratings, file1, indent=4)
    return new_rating

app.run(port=8000)