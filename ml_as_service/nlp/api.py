import ast
import json

from flask import Flask, request
from flask_restful import Api, Resource
from inference import inference, load_model

app = Flask(__name__)
api = Api(app)


model = load_model(path_to_model="models/bert-base-NER")


class Health(Resource):
    def get(self):
        return {"status": "UP"}


class Info(Resource):
    def get(self):
        return {"info": "transformers"}


api.add_resource(Health, "/health")
api.add_resource(Info, "/info")


def prepare_data(flask_request: request) -> str:
    sentence = ast.literal_eval(flask_request.data.decode("utf-8"))["sentence"]
    return sentence


class Predict(Resource):
    def post(self):
        sentence = prepare_data(flask_request=request)
        result = inference(model=model, sentence=sentence)
        return {"result": json.dumps(str(result))}


api.add_resource(Predict, "/predict")


if __name__ == "__main__":
    app.run(debug=True)
