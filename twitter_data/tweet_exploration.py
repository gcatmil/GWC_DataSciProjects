import json

file = open("tweets.json", "r")
data = json.load(file) #load from file into a json object

for d in data:
    #loop thru to a single tweet
    # for info_category, info in d.items():
    #     print(info_category, info)
    # for user_mention in d["user_mentions"]:
    #     print(user_mention["screen_name"])
    # print(d["text"])
    # print(d["user"]["favourites_count"])
    print(d["retweet_count"])

    break
