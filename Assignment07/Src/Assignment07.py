#Name: Zavier DePillo
#Email: depillzj@mail.uc.edu
#Assignment Title: Assignment 07
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: Editing fonts on captchas
#Citations:
#Anything else that's relevant:

'''
Created on Feb 26, 2020

@author: nicomp
'''
import random
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random 

default_color_red = 228
default_color_green = 150
default_color_blue = 150

def generate_random_string(length):
    random_string = ""
    for i in range(0,length):
        random_string = random_string + random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVQXYZ')
    return random_string

def draw_random_ellipse(draw):
    # A random circle on the image
    a = random.randrange(10, 300, 1)
    b = random.randrange(10, 275, 1)
    c = a + random.randrange(10, 90, 1)
    d = b + random.randrange(10, 90, 1)
    draw.ellipse((a,b,c,d), fill=(default_color_red + random.randrange(-100,100,1), 
                                  default_color_green + random.randrange(-100,100,1), 
                                  default_color_blue + random.randrange(-100,100,1), 255), 
                                  outline = "black")

def generate_captcha(captchaLength, targetFileName):
    '''
    Generate a captcha
    :return: A tuple (image, captcha string encoded in the image)
    '''
    if captchaLength < 6 or captchaLength > 10:
        #We have a problem.
        captchaLength = 10
    captcha_string = generate_random_string(captchaLength)
#   print(">" + captcha_string + "<")
    captcha_image = Image.new("RGBA", (400, 200), (default_color_red,default_color_green,default_color_blue))
    draw = ImageDraw.Draw(captcha_image, "RGBA")
    for i in range(1,20):
        draw_random_ellipse(draw)

    # Arbitrary starting co-ordinates for the text we will write
    x = 10 + random.randrange(0, 100, 1)
    y = 79 + random.randrange(-10, 10, 1)
    for letter in captcha_string:
        #Select a random font from all the fonts I have
        myFonts = ["Aaargh.ttf", "Bombing.ttf", "Jurassic Park.ttf", "QuirkyRobot.ttf", "Sketch Gothic School.ttf"]
        randomFont = random.choice(myFonts)
        #print(randomFont)
        fontStyle = ImageFont.truetype(randomFont, 48)     # font must be in the same folder as the .py file. 

#       print(letter)
        draw.text((x, y), letter, (0,0,0),font=fontStyle)    # Write in black
        x = x + 35
        y = y +  random.randrange(-10, 10, 1)
    #Save the image on the disk as targetFileName
    rgb_im = captcha_image.convert("RGB")
    rgb_im.save(targetFileName)
    return (captcha_image, captcha_string)  # return a heterogeneous tuple
