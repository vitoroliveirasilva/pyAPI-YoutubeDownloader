# Importação do pytubefix
from pytubefix import YouTube

# Download do vídeo pela URl inserida no terminal
download = YouTube(str(input('URL: '))).streams.get_highest_resolution().download()
