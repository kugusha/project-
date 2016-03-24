from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError
from pymongo import MongoClient

client = MongoClient()
usersDB = client["VK_users"]["users"]
mediaDB = client["Media"]["vk_media_new"]

access_token = "2206388144.9a41b0c.e3a1a62d62a040abaedc1dd89952e7b6"
client_secret = "f21605b4441040a4b4de3f42da5cb41e"

# connect to Instagram API
api = InstagramAPI(access_token = access_token, client_secret = client_secret)

for user in usersDB.find():
    try:
        if not mediaDB.find_one({"id" : user['uid']}):
            media_data, next_ = api.user_recent_media(user_id = user['uid'])
            for media in media_data:
                print media.__dict__["id"]
                mediaDB.insert({'caption' : str(media.__dict__)})

    except InstagramAPIError as e:
        print e
