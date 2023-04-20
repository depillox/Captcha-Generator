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

from Src.Assignment07 import generate_captcha

result = generate_captcha(6, "test.jpg")
myCaptcha = result[0]
captcha_string = result[1]
print(">" + captcha_string + "<")
myCaptcha.show()

