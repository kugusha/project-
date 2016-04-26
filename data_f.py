from pymongo import MongoClient
import numpy as np
import re

client = MongoClient()
DB = client["users"]["vk_dataset"]

def sex():
    vk_ds = DB.find()
    x = np.array([])

    for label in vk_ds:
        x = np.append(x, label["sex"])
    return x
print sex()    

def followers():
	vk_ds = DB.find()
	x = np.array([])

	for label in vk_ds:
		x = np.append(x, label["followed_by"]["count"])
	return x
print followers() 

def follows():
	vk_ds = DB.find()
	x = np.array([])

	for label in vk_ds:
		x = np.append(x, label["follows"]["count"])
	return x;
print follows()

def media():
	vk_ds = DB.find()
	x = np.array([])

	for label in vk_ds:
		x = np.append(x, label["media"]["count"])
	return x;
print media()
