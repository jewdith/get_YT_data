#bron: https://www.youtube.com/watch?v=5qtC-tsQ-wE
from youtube_statistics import YTstats

API_KEY = "api key here"
channel_id= "channel id here" #laatste deel van url

#maak yt object aan
yt = YTstats(API_KEY, channel_id)
yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump() #zet data in json file genaamd 'python_engineer.json' in dezelfde dir waar main.py staat

