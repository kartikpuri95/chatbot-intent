import io
import json
import flask
from flask import Flask, jsonify

from snips_nlu import SnipsNLUEngine

app = Flask(__name__)
with io.open("food_delivery_intent.json") as f:
    sample_dataset = json.load(f) #loading the food delivery intent json that we created using cli

nlu_engine = SnipsNLUEngine() ##Sninluengine object

nlu_engine.fit(sample_dataset) ## Loading the dataset in the snipnlu object

@app.route("/parse/", methods=["GET"])
def parse():
    sample_text=flask.request.json['sample_text'] ## sample text from our postman request
    parsing = nlu_engine.parse(sample_text) # Parsing the utterence sent from postman request
    return flask.jsonify(data=parsing)


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)