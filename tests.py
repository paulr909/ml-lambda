import json

import boto3
from decouple import config


def test_sentiment_predicted():
    client = boto3.client(
        "lambda",
        region_name=config("AWS_DEFAULT_REGION"),
        aws_access_key_id=config("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"),
    )
    response = client.invoke(
        FunctionName="ml-model-development-ml_model",
        InvocationType="RequestResponse",
        Payload=json.dumps({"text": "I am so happy! You really did a great job!"}),
    )

    assert (
        json.loads(response["Payload"].read().decode("utf-8"))["sentiment"]
        == "positive"
    )
