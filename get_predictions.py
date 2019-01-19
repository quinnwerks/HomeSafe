import os
import requests


url = "http://max-audio-classifier.max.us-south.containers.appdomain.cloud/model/predict"
dir_ = "data/"


def get_predictions():
    files = os.listdir(dir_)
    data = dict()

    for filename in files:
        best = requests.post(url=url, files={"audio": (dir_ + filename, open(dir_ + filename, "rb"))}).json()["predictions"][0]
        data[dir_ + filename] = (best["label"], best["probability"])

    return data
