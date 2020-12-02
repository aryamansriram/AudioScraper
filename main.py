from youtube_transcript_api import YouTubeTranscriptApi
import json
import pafy
import os
import yaml



with open("links.txt","r") as f:
    links = f.readlines()

links = [link.rstrip("\n") for link in links]

with open("config.yml","r") as f:
    config = yaml.load(f)

speaker_name = config["speaker_name"]

SAVE_PATH = "audio/"
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],


}
dir_path=SAVE_PATH+speaker_name
#'/%(title)s.%(ext)s'
count = 1
for link in links:
    print("Downloading sound clip ",count)
    temp = links[0].split("&")[0]

    try:
        vid = pafy.new(link)
        bestaudio = vid.getbestaudio()
        if not os.path.exists(dir_path+"/"+ str(count)+"/"):
            os.makedirs(dir_path+"/"+ str(count)+"/")
        bestaudio.download(filepath=dir_path+"/"+ str(count)+"/"+str(count)+"."+bestaudio.extension)
    except:
        print("Unresolvable conn error for video", count)
        continue
    vid_id = link.split("?")[1].split("=")[1].split("&")[0]
    try:
        trans = YouTubeTranscriptApi.get_transcript(vid_id)
        with open(dir_path+"/"+str(count)+"/"+str(count)+".json","w+") as f:
            json.dump(trans,f)
    except:
        print("Could not generate Transcript here")
        print("ID: ",vid_id)
    count+=1






