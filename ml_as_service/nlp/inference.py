import argparse
from typing import Any, Dict, List

from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline


def get_argparse() -> argparse.Namespace:

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--path_to_model",
        type=str,
        required=True,
        help="path to trained model",
    )
    parser.add_argument(
        "--sentence",
        type=str,
        required=True,
        help="sentence for inference",
    )

    return parser.parse_args()


def load_model(path_to_model: str) -> pipeline:
    tokenizer = AutoTokenizer.from_pretrained(path_to_model)
    model = AutoModelForTokenClassification.from_pretrained(path_to_model)
    pipe = pipeline("ner", model=model, tokenizer=tokenizer)
    return pipe


def inference(model: pipeline, sentence: str) -> List[Dict[str, Any]]:
    return model(sentence)


if __name__ == "__main__":

    args = get_argparse()

    model = load_model(path_to_model=args.path_to_model)

    result = inference(model=model, sentence=args.sentence)

    print("Entites:")
    for entity in result:
        print(entity)
