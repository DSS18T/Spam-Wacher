import base64

def encode(string):
    encodedBytes = base64.b64encode(string.encode("utf-8"))
    encode = str(encodedBytes, "utf-8")
    return encode

def decode(string):
    decode = base64.b64decode(string).decode("utf-8", "ignore")
    return decode
