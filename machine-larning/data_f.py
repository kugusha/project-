from pymongo import MongoClient
import numpy as np
import time
import datetime
import random
import re


client = MongoClient()
DB = client["users"]["vk_dataset"]

def first_name():
	vk_ds = DB.find()
	x = np.array([])

	for label in vk_ds:
		x = np.append(x, label["first_name"])
	return x;
#print len(first_name())

def last_name():
	vk_ds = DB.find()
	x = np.array([])

	for label in vk_ds:
		x = np.append(x, label["last_name"])
	return x;
#print len(last_name())

def username():
	vk_ds = DB.find()
	x = np.array([])

	for label in vk_ds:
		x = np.append(x, label["username"])
	return x;
#print len(username())

def sex():
    vk_ds = DB.find()
    x = np.array([])

    for label in vk_ds:
        x = np.append(x, label["sex"])
    return x
#print sex()    

def age():
	vk_ds = DB.find()
	x = np.array([])

	for label in vk_ds:
		bdate = datetime.datetime.strptime(label["bdate"], '%d.%m.%Y')
		x = np.append(x, 2016 - int(bdate.year))
	return x
#print age()    

#string = "19 Nov 2015  18:45:00.000"
#date = datetime.datetime.strptime(string, "%d %b %Y  %H:%M:%S.%f")

def followers():
	vk_ds = DB.find()
	x = np.array([])

	for label in vk_ds:
		x = np.append(x, label["followed_by"]["count"])
	return x
#print len(followers()) 

def follows():
	vk_ds = DB.find()
	x = np.array([])

	for label in vk_ds:
		x = np.append(x, label["follows"]["count"])
	return x;
#print len(follows())

def media():
	vk_ds = DB.find()
	x = np.array([])

	for label in vk_ds:
		x = np.append(x, label["media"]["count"])
	return x;
#print len(media())

def likes():
    vk_ds = DB.find()
    x = np.array([])

    for label in vk_ds:
        try:
            person_likes = np.mean([i["likes"]["count"] for i in label["media"]["nodes"]])
            x = np.append(x, person_likes)
        except:
            x = np.append(x, 0)
    return x

def comments():
    vk_ds = DB.find()
    x = np.array([])

    for label in vk_ds:
        try:
            person_comments = np.mean([i["comments"]["count"] for i in label["media"]["nodes"]])
            x = np.append(x, person_comments)
        except:
            x = np.append(x, 0)
    return x   

def age_classification():
    ages = age()
    x = np.array([])
    
    for i in ages:
        if i <= 16:
            x = np.append(x, 1)
        if 17 <= i <= 25:
            x = np.append(x, 2)
        if 26 <= i <= 34:
            x = np.append(x, 3)
        if i >= 35:
            x = np.append(x, 4)
    return x	
#print age_classification()