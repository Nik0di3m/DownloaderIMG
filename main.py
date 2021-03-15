import wget
import os
import urllib.request
from art import tprint

tprint("ReSizer", "rand")
print("Made By NiCodi3m V0.1")


#Zapis plików pod nazwą kodu EAN

#Lista linków pobierana z pliku
linki = open("linki.txt").readlines()
#Zapisywanie zdjęć nazwą z pliku
filename = open("ean.txt").readlines()
#Zapis w oddzielnym folderze
os.mkdir("Download")
os.chdir("./Download")
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)')]
urllib.request.install_opener(opener)



for i in range(len(linki)):
    image_url = linki[i]
    nazwa = filename[i]
    print(image_url)
    nazwa = nazwa.rstrip("\n")
    nazwa = nazwa + ".jpg"
    #Zapis plików pod nazwą kodu EAN
    urllib.request.urlretrieve(image_url, nazwa)
    print("Sukces" + nazwa)

print("Sukces")
exit()