import os
from PIL import Image
from html2image import Html2Image

class ImageFunctions:

    def __init__(self):
        self.originalFolder   = os.getcwd() + "\\images\\original\\"
        self.compressedFolder = os.getcwd() + "\\images\\compressed\\"
        self.htmlFolder       = os.getcwd() + "\\images\\html\\"
        self.formats          = [ '.jpg', '.jpeg' ]

    def compress(self):
        verbose = True

        # looping through all the files
        # in a current directory
        for file in os.listdir(self.originalFolder):
        
            # If the file format is JPG or JPEG
            if os.path.splitext(file)[1].lower() in self.formats:
                print('  - %s' %file)
                print('      . . . compressing . . . ')
                self.compressMe(file, verbose)

        print("\n -- All images compressed successfully --\n")
    
    def compressMe(self, file, verbose = False):
  
        # Get the path of the file
        filepath = os.path.join(self.originalFolder, file)
        
        # open the image
        picture = Image.open(filepath)
        
        # Save the picture with desired quality
        # To change the quality of image,
        # set the quality variable at
        # your desired level, The more 
        # the value of quality variable 
        # and lesser the compression
        picture.save(
            self.compressedFolder + "compressed_" + file, 
            "JPEG", 
            optimize = True, 
            quality  = 10,
            verbose  = verbose
        )
        

    def htmlToImage(self, url):
        # output folder
        output_path = self.htmlFolder
        # Set the output file name
        output_file = url.replace('https://', '')
        output_file = output_file.replace('http://', '')
        output_file = output_file.replace('.', '_')
        output_file = output_file + '.png'
        
        hti = Html2Image(output_path = output_path)

        # Take a full-page screenshot
        # change height and width as needed ( width=1920px, height=2080px )
        hti.screenshot(
            url     = url,
            save_as = output_file,
            size    = (1920, 2080)
        )

        print(f"\n -- Screenshot saved as {output_file} --\n")

