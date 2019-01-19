import requests

url = "http://max-audio-classifier.max.us-south.containers.appdomain.cloud/model/predict"


def get_prediction(filename):
    return [i["label"] for i in requests.post(url=url, files={"audio": (filename, open(filename, "rb"))}).json()["predictions"]]
