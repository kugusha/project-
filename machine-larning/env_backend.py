import pickle
import requests
from bs4 import BeautifulSoup
import json
import numpy as np
import datetime
import re

def get_user_info(username):
    r = requests.get("http://instagram.com/" + username)
    html_code = r.text

    try:
        soup = BeautifulSoup(html_code, 'html.parser')
        script = soup.find_all('script')[6].string
        data = json.loads(script[21:-1])
        r = data["entry_data"]["ProfilePage"][0]["user"]

        if r["is_private"]:
            print "Private"
            return None

        r["follows"] = r["follows"]["count"]
        r["followed_by"] = r["followed_by"]["count"]
        r["media_count"] = r["media"]["count"]
        return r
    except:
        print "error"
        return None

def make_user_features(info):
    features = {}

    features["count_followers"] = info["followed_by"]
    features["count_followings"] = info["follows"]
    features["count_media"] = info["media_count"]
    features["average_likes"] = np.mean([i["likes"]["count"] for i in info["media"]["nodes"]])
    features["average_comments"] = np.mean([i["comments"]["count"] for i in info["media"]["nodes"]])

    return features

    
def user_predict(features):
    with open("sex_model.pkl") as f:
        classifier_sex = pickle.load(f)

    with open("age_model.pkl") as f:
        classifier_age = pickle.load(f)

    data = [features["count_followings"],
            features["count_followers"],
            features["count_media"],
            features["average_likes"],
            features["average_comments"]]

    return {
        "sex" : classifier_sex.predict(data)[0],
        "age" : int(classifier_age.predict(data)[0])
    }