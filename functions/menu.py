from consolemenu import *
from consolemenu.items import *
from functions.imageFunctions import ImageFunctions
from functions.commonFunctions import CommonFunctions

class Menu:

    def __init__(self):
        self.common = CommonFunctions()

    # menu
    def showMenu(self):
        menu = ConsoleMenu("Image functions", "Options")

        menu.append_item(FunctionItem("compressImage", self.compressImage))
        # menu.append_item(FunctionItem("resizeImage", self.resizeImage))
        # menu.append_item(FunctionItem("cropImage", self.cropImage))
        # menu.append_item(FunctionItem("convertToJPGImage", self.convertToJPGImage))
        # menu.append_item(FunctionItem("convertFromJPGImage", self.convertFromJPGImage))
        # menu.append_item(FunctionItem("editImage", self.editImage))
        # menu.append_item(FunctionItem("zoomImage", self.zoomImage))
        # menu.append_item(FunctionItem("clearBgImage", self.clearBgImage))
        # menu.append_item(FunctionItem("watermarkImage", self.watermarkImage))
        # menu.append_item(FunctionItem("memeImage", self.memeImage))
        # menu.append_item(FunctionItem("rotateImage", self.rotateImage))
        menu.append_item(FunctionItem("htmlToImage", self.htmlToImage))
        # menu.append_item(FunctionItem("pixelfaceImage", self.pixelfaceImage))


        # Finally, we call show to show the menu and allow the user to interact
        menu.start()
        menu.join()
        # menu.show()
        # return menu


    def compressImage(self):
        self.common.printMenuText('Compress images')

        try:
            img = ImageFunctions()
            img.compress()
        except Exception as e:
            self.common.printMenuError(e)
        
        self.promptContinueLine()

    # def resizeImage(self):
    #     self.promptContinueLine()
    # def cropImage(self):
    #     self.promptContinueLine()
    # def convertToJPGImage(self):
    #     self.promptContinueLine()
    # def convertFromJPGImage(self):
    #     self.promptContinueLine()
    # def editImage(self):
    #     self.promptContinueLine()
    # def zoomImage(self):
    #     self.promptContinueLine()
    # def clearBgImage(self):
    #     self.promptContinueLine()
    # def watermarkImage(self):
    #     self.promptContinueLine()
    # def memeImage(self):
    #     self.promptContinueLine()
    # def rotateImage(self):
    #     self.promptContinueLine()
    
    def htmlToImage(self):
        self.common.printMenuText('HTML url to image')

        try:
            url = input(" -- Enter the URL of the webpage you want to capture: ")

            img = ImageFunctions()
            img.htmlToImage(str(url).strip())
        except Exception as e:
            self.common.printMenuError(e)

        self.promptContinueLine()
    
    # def pixelfaceImage(self):
    #     self.promptContinueLine()



    # continue line
    def promptContinueLine(self):
        pu = PromptUtils(Screen())
        pu.enter_to_continue()

    # ask for input
    def promptInputValue(self, text):
        pu = PromptUtils(Screen())
        result = pu.input(" -- %s" %text)

        return result.input_string