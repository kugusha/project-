from pymongo import MongoClient
import numpy as np
import re

client = MongoClient()
vk = client["users"]["vk_dataset"]

def sex():
    vk_ds = vk.find()
    x = np.array([])

    for label in vk_ds:
        x = np.append(x, label["sex"])
        
    return x

print sex()    
