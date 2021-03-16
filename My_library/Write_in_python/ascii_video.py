from PIL import Image, ImageDraw, ImageFont
import math
import cv2  
import os


#Video capture 
cap = cv2.VideoCapture(0)


chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

# chars = "#Wo- "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256
fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)
scaleFactor = 0.09
oneCharWidth = 10
oneCharHeight = 18

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

#text_file = open("Output.txt", "w")

#im = Image.open("car.jpg")



while True:

    ret, frame = cap.read()
    im = Image.fromarray(frame)
    width, height = im.size
    im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
    width, height = im.size
    pix = im.load()


    #print a video
    for i in range(height):
        for j in range(width):
            r, g, b = pix[j, i]
            h = int(r/3 + g/3 + b/3)
            pix[j, i] = (h, h, h)
            print(getChar(h))
            print('\n')
        
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

