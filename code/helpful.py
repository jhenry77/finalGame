import pygame
from os import walk


def importFolder(path):
    allSurfaces = []

    for folderName, subFolder, files in walk(path):
        for images in files:
            fullPath = path + '/' + images
            imageSurface = pygame.image.load(fullPath).convert_alpha()
            allSurfaces.append(imageSurface)
    return allSurfaces


def importDictFolder(path):
    surfaceDict = {}

    for folderName, subFolder, files in walk(path):
        for images in files:
            fullPath = path + '/' + images
            imageSurface = pygame.image.load(fullPath).convert_alpha()
            surfaceDict[images.split('.')[0]] = imageSurface

    return surfaceDict
