import argparse
import json

from mercury import MercuryPredictor


def main():
    parser = argparse.ArgumentParser(description="Run a MERCURY prediction")
    parser.add_argument("text", help="Social-media text to classify")
    parser.add_argument("--device", default="auto", choices=["auto", "cpu", "cuda"])
    args = parser.parse_args()
    predictor = MercuryPredictor(device=args.device)
    print(json.dumps(predictor.predict(args.text), indent=2))


if __name__ == "__main__":
    main()
