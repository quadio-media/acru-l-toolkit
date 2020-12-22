import json

import boto3

secretsmanager = boto3.client("secretsmanager")


def get_secret(secret_id: str, key: str = None):
    secret_string = secretsmanager.get_secret_value(SecretId=secret_id)[
        "SecretString"
    ]
    if key:
        return json.loads(secret_string)[key]
    return secret_string
