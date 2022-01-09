from pytube import YouTube 

class MyClass(object):
    def __init__(self):
        self.urlinput = input('Ссылка на видео: ')
        self.xx = int(input('Качество видео:\n144р - 1\n360р - 2\n480 - 3\n720p - 4\n1080p - 5\n: '))
        self.location = input('Куда скачивать видео: ')
        self.p = ['144p', '360p', '480p', '720p', '1080p']

        self.download()
        
    def setUrl(self):
        url = self.urlinput
        self.yt = YouTube(url)

        self.videos = self.yt.streams.filter(mime_type = 'video/mp4').all()

    def download(self):
        while len(self.urlinput) < 10:
            self.urlinput = input('Ведена неверная ссылка: ')
        
        quality = self.videos[self.p[self.xx - 1]]
        location = self.location
        quality.download(location)
    

    
    def browse(self):
        location_download = self.location



        

MyClass()

