from pytube import YouTube
link = input("Masukkan URL Video : ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()