import youtube_dl

with youtube_dl.YoutubeDL() as ydl:
    ydl.download(['https://youtu.be/2pLT-olgUJs'])
