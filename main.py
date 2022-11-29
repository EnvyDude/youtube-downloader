import os
os.system("pip install pytube")
import urllib.request
import time
from youtube_transcript_api import YouTubeTranscriptApi

def clear():
    linux = "clear"
    windows = "cls"
    os.system([linux,windows][os.name=="nt"])

clear()
from pytube import YouTube
import requests
clear()
os.system('color 4')
aryan = input("Enter Youtube Video Link ! : ")
yt = YouTube(aryan)
clear()
print('[+]Choices     \n[1]:Yt Thumbnail Download\n[2]:Yt Video Download\n[3]:Yt Audio Download\n[4]:Subtitles Download\n')
os.system('color 3')
og = input("Choice: ")
clear()

def get_filename():
    return yt.title[:10]

def thumbnail():
    sax = yt.thumbnail_url
    file_name = get_filename()
    f = open('thumbnails/'+file_name+'.jpg','wb')
    f.write(urllib.request.urlopen(sax).read())
    f.close()
    print('Image sucessfully Downloaded: ',file_name)
    time.sleep(6)

def download():
    os.system('color 7')
    print("Name : ", yt.title)
    print("Views: ", yt.views)
    print("Length: ", yt.length)
    print("Ratings!: ", yt.rating)
    phantom = yt.streams.get_highest_resolution()
    print(f"Downloading {yt.title}")
    phantom.download()
    print("Done The file has been downloaded to the folder of this script")

def audio():
    video = yt.streams.filter(only_audio=True).first()
    destination = ''
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " has been downloaded!")


def captions():
    saxo = input('Enter Yt video without (https://youtube.com/watch?v=):')
    srt = YouTubeTranscriptApi.get_transcript(saxo)
    file_name = get_filename()
    with open('captions/'+file_name+'.txt',"w") as f:
        for i in srt:
            f.write("{}\n".format(i))
            print("Downloaded Captions successfully!")

if og == '1':
    print('Downloading Thumbnail !')
    thumbnail()
elif og == '2':
    print('downloading Youtube Video!')
    download()
elif og == '3':
    print('Downloading Audio!')
    audio()
elif og == '4':
    print('Downloading Captions')
    captions()
else:
    print('Unknown Choice!')