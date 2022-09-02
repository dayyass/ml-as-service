import argparse

import joblib
from sklearn.pipeline import Pipeline


def get_argparse() -> argparse.Namespace:

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--path_to_model",
        type=str,
        required=True,
        help="path to trained model",
    )
    parser.add_argument(
        "--path_to_email",
        type=str,
        required=True,
        help="path to email txt file for inference",
    )

    return parser.parse_args()


def load_model(path_to_model: str) -> Pipeline:
    return joblib.load(path_to_model)


def inference(model: Pipeline, email: str) -> str:
    return model.predict([email])[0]


if __name__ == "__main__":

    args = get_argparse()

    model = load_model(path_to_model=args.path_to_model)

    with open(args.path_to_email, mode="r", encoding="utf-8") as fp:
        email = fp.read()

    result = inference(model=model, email=email)
    print(f"E-mail Topic: {result}")
