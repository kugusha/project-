from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError
import json
from pymongo import MongoClient

client = MongoClient()
usersDB = client["UsersInstagram"]["public"]
mediaDB = client["UsersInstagram"]["media"]
# access_token = "2206388144.9a41b0c.e3a1a62d62a040abaedc1dd89952e7b6"
# client_secret = "f21605b4441040a4b4de3f42da5cb41e"

# connect to Instagram API
api = InstagramAPI(access_token = access_token, client_secret = client_secret)

for user in usersDB:
        try:
                info = api.user(user_id = user.id)
                #recent_media 
                    if not media.find_one({"id" : user.id}):
                            media.insert(#hz smth like info.media_id)
                            print "MEDIA ADDED"
                    else:
                            print "ALREADY IN"
        except InstagramAPIError as e:
            print e

        print ''
# check counters and set to Mongo (50)