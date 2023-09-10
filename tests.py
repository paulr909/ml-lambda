import json

import boto3


def test_sentiment_is_predicted():
    region = "eu-west-2"
    print("Lambda region: ", region)

    client = boto3.client("lambda", region_name=region)
    response = client.invoke(
        FunctionName="ml-model-development-ml_model",
        InvocationType="RequestResponse",
        Payload=json.dumps({"text": "I am so happy! You really did a great job!"}),
    )

    assert (
        json.loads(response["Payload"].read().decode("utf-8"))["sentiment"]
        == "positive"
    )
