#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# CreatePlaylist.py
import fileinput
import glob
import os


#configurationsdatei
absLink = "/media/thedoctor/mydata/Music/01_Anime_Cartoon/"
#suche nur ein bestimmtes Verzeichnis
location = "/media/thedoctor/mydata/Music/01_Anime_Cartoon/"
#suche alle Verzeichnisse ab
#filenames = glob.glob("/media/thedoctor/mydata/Music/**/*.m3u",recursive=True)
filenames = glob.glob("/media/thedoctor/mydata/Music/myPlaylist.m3u")
print(filenames)
#declare Variablen
lines = []
extinf = []
pathname = []
# hoffentlich sind es nicht so viele Zeilen. ;-)
counter=0
for line in fileinput.input(filenames):
    lines.append(line.strip())
    if counter > 0 and counter % 2 != 0:
        extinf.append(line.strip())
    elif counter > 0 and counter % 2 == 0:
        pathname.append(line.strip())
    counter += 1
print("----------------------------------------------------------")
print(lines[1])
print("----------------------------------------------------------")
print(extinf[0])
print("----------------------------------------------------------")
print(pathname[0])
print("----------------------------------------------------------")

#herausnehmen des absoluten links
#relativ zur position
tmpList = ['#EXTM3U']
#tmpList.append()
counter=0
for link in pathname:
    if absLink in link:
        tmpList.append(extinf[counter])
        tmpList.append(link.replace(absLink,''))
    counter += 1

print(tmpList[0])
print(tmpList[1])
print(tmpList[2])
print(tmpList[3])

with open(absLink+"file.txt", "w") as output:
    for line in tmpList:
        output.write(line+"\n")

#os.listdir("/media/thedoctor/mydata/Music")
#print(os.listdir("/media/thedoctor/mydata/Music/*.m3u"))