from flask import Flask, request
from flask_restful import Api, Resource
from inference import inference, load_model

app = Flask(__name__)
api = Api(app)


class Health(Resource):
    def get(self):
        return {"status": "UP"}


class Info(Resource):
    def get(self):
        return {"info": "sklearn"}


api.add_resource(Health, "/health")
api.add_resource(Info, "/info")


def prepare_data(flask_request: request) -> str:
    email = flask_request.files["email"].read()
    return email


class Predict(Resource):
    def post(self):
        email = prepare_data(flask_request=request)

        # TODO: refactor model init
        model = load_model(path_to_model="models/model.joblib")

        result = inference(model, email)
        return {"result": result}


api.add_resource(Predict, "/predict")


if __name__ == "__main__":
    app.run(debug=True)
