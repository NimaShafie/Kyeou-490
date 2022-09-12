
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import itertools

app = Flask(__name__)
CORS(app)


@app.route('/<string:subject>/<string:data>')
def get(**kwargs):
    return json.load(open(f'./json_{kwargs["data"]}/{kwargs["subject"].upper()}_{kwargs["data"]}.json'))


@app.route('/<string:subject>/rating', methods=['POST'])
def new_rating(**kwargs):
    current_ratings = json.load(open(f'./json_rating/{kwargs["subject"].upper()}_rating.json'))
    rating_file = open(f'./json_rating/{kwargs["subject"].upper()}_rating.json', "w")
    new_rating = request.get_json(force=True)
    print('Post Body:', new_rating)
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

    json.dump(current_ratings, rating_file, indent=4)
    return current_ratings


@app.route('/<string:subject>/<string:catalog_number>/history/<int:amount>')
def historical_profs(**kwargs):
    with open(f"../backend/json_historical_profs/{kwargs['subject'].upper()}_history.json") as subject:
        classes = json.load(subject)
        return dict(itertools.islice(classes[f"{kwargs['subject'].upper()} {kwargs['catalog_number'].upper()}"].items(), kwargs["amount"]))

@app.route('/<string:subject>/classes')
def catalog(**kwargs):
    with open(f"../backend/json_catalog/{kwargs['subject'].upper()}_catalog.json") as subject:
        classes = json.load(subject)
        return ([x["catalog_number"] + " - " + x["title"] for x in classes])

@app.route('/<string:subject>/prof/name/<string:prof_email>')
def prof_name(**kwargs):
    with open(f"../backend/json_profname/{kwargs['subject'].upper()}_profname.json") as profs:
        profs = json.load(profs)
        return profs[kwargs['prof_email']]

app.run(port=8000)
