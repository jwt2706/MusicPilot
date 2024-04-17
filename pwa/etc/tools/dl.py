# download audio from youtube only using the link
# requires the pytube library to work


from pytube import YouTube
import os

while True:
    v = input("Video link: ")
    yt = YouTube(v)

    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(output_path=".")

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    with open("links.txt", "a") as links:
        links.write(v+"\n")
