# -*- coding: utf-8 -*-
"""Importing The LIibraries

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s4dyiqvv2r_YLXjklT8B0jpWVohxvqqW
"""

dirName = 'C:\Augmented Data'
folders = listdir(dirName)

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for fol name in listOfFile:
        fullPath = os.path.join(dirName,fol_name)
        allFiles.append(fullPath)
    return allFiles

Folders = getListOfFiles(dirName)
len(Folders)
subfolders = []
for num in range(len(Folders)):
    sub_fols = getListOfFiles(Folders[num])
    subfolders+=sub_fols
subfolders