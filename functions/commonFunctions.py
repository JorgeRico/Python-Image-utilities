import time
import os
import json
import urllib
import urllib.request
from bs4 import BeautifulSoup

class CommonFunctions:

    # sets url
    def getMainSetPage(self):
        return 'https://scryfall.com/sets/'
    
    # cube url
    def getAlternativeMainPage(self):
        return 'https://scryfall.com/cubes/'

    # website url
    def getBaseUrl(self):
        return 'https://scryfall.com/'

    # cards url
    def getCardUrl(self):
        return 'https://api.scryfall.com/cards/'

    # file with abbreviation set names
    def getAbbreviationSetFolderFile(self):
        return 'dump/abbreviations/sets.txt'

    # save set info - insert folder
    def getCardsSetFolderFile(self, setName):
        return 'dump/sets/' + setName + '.txt'

    # print menu text
    def printDoneText(self):
        print(' -- Done!!')
        print('')

    # print menu text
    def printMenuText(self, text):
        print('')
        print(' -- %s ...' %text)
        print('')

    def printMenuTextSingleLine(self, text):
        print(' -- %s' %text)

    # error function
    def printMenuError(self, option):
        print(" !! error %s !!" %option)

    # wait time function
    def waitTime(self, timeToWait):
        time.sleep(timeToWait)

    # check if file is empty
    def isEmptyFile(self, fileName):
        if os.stat(fileName).st_size == 0:
            return True
        else:
            return False

    # append info on a file
    def writeFileLine(self, fileName, text):
        with open(fileName, 'a',  encoding='utf-8') as outfile:
            outfile.write(str(text))
            outfile.write("\n")

    # delete existing file
    def deleteFile(self, fileName):
        os.remove(fileName)

    def deleteIfExistis(self, fileName):
        if os.path.exists(fileName):
            self.deleteFile(fileName)

    # save info to a file
    # loop info or single json line
    def saveToFile(self, folderFile, itemData, loop = False):
        self.deleteIfExistis(folderFile)
        
        self.waitTime(5)

        if loop == True:
            for item in itemData:
                self.writeFileLine(folderFile, item)
        else:
            self.writeFileLine(folderFile, itemData)

    # get info on json format
    def convertToJson(self, item):
        return json.dumps(item)

    # load json data
    def loadJsonData(self, data):
        return json.loads(str(data))
    
    # get soup
    def getSoup(self, url):
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')

        return soup
    
    # read file lines and save to a var
    def readAbbreviationFileLines(self, fileName):
        setList = []
        file = open(fileName, "r")
        for line in file:
            setList.append(line.replace('\n', ''))

        return setList
    
    # check file errors
    def checkFileErrors(self, fileName, isSet = False):
        if os.path.exists(fileName) == False:
            self.setFileEmptyError(isSet)  
        
        if self.isEmptyFile(fileName) == True:
            self.setFileEmptyError(isSet)  

    # show error
    def setFileEmptyError(self, isSet = False):
        if isSet == True:
            self.printMenuError('empty all sets file. Fill with option 2')
        else:
            self.printMenuError('empty file.')

    # check conflux exception
    def checkAbbreviationException(self, setAbrv):
        if setAbrv == 'con':
            setAbrv = 'conflux'

        return setAbrv