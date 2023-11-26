from jwt import encode, decode


def create_token(data: dict):
    token: str = encode(payload=data, key="my_secreate_key", algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    data: dict = decode(token, key="my_secreate_key", algorithms=['HS256'])
    return data