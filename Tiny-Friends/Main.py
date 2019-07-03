import tweepy
import random
import emoji
import names
import time
from EmList import ALL_ANIMALS
from EmList import SETTING

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



myTweet = [["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""]]

rareNum = random.randint(0,40)

if rareNum == 12:
    num = len(ALL_ANIMALS)-1
elif rareNum%2 == 0:
    num = 0
else:
    num = random.randint(1,len(ALL_ANIMALS)-2) #get category by number

animalCategory = ALL_ANIMALS[num] #access animal array for the random category
settingCategory = SETTING[num] #access setting array for the random category

i = 0
j = 0
k = 0
h = 0
settingBefore = settingCategory[0] #random.randint(0,len(settingCategory)-1)
settingAfter = emoji.emojize(settingBefore, use_aliases=True)

while i < len(myTweet[0]):
    myTweet[0][i] = settingAfter
    i+= 1

while j < len(myTweet[0]):
    myTweet[len(myTweet)-1][j] = settingAfter
    j+= 1

n = 0
numSettingEmojis = random.randint(2,4)
while n <= numSettingEmojis:
    randomR = random.randint(1,len(myTweet)-2)
    randomC = random.randint(0,len(myTweet[0])-1)

    pickOneSetting = random.randint(0,len(settingCategory)-1)
    while pickOneSetting == settingAfter:
        random.randint(0,len(settingCategory)-1)
    settingBefore = SETTING[num][pickOneSetting]
    myTweet[randomR][randomC] = emoji.emojize(settingBefore, use_aliases=True) + " "
    n+= 1

pickOne = random.randint(0,len(animalCategory)-1) #pick an animal emoji from that category by number
emojiBefore = ALL_ANIMALS[num][pickOne] #get emoji
animal = emoji.emojize(emojiBefore, use_aliases=True)

randomR = random.randint(3,len(myTweet)-3)
randomC = random.randint(3,len(myTweet[0])-3)
myTweet[randomR][randomC] = animal

for r in range(len(myTweet)):
    for c in range(len(myTweet[0])):
        if myTweet[r][c] == "":
            myTweet[r][c] = "    "

gender = random.randint(0,2)
if gender == 0:
    description = " This is "  +names.get_first_name(gender='female') +"."
elif gender == 1:
    description = " This is "  +names.get_first_name(gender='male') +"."
elif gender == 2:
    description = " This is "  +names.get_first_name() +"."

finalTweet = '\n'.join(map(''.join, myTweet)) + "\n" + description

user = api.me()
print ("Successfully posted to "+user.name)

api.update_status(finalTweet)
interval = 60 * 60 * 6
time.sleep(interval)
