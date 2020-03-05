# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 23:46:15 2020

@author: imran
"""
from PIL import Image, ImageTk, ImageDraw

class Filtre:
    def __init__(self,img):
        self.img = img
        
    def binary(self,x1,y1,x2,y2):
        largeur , hauteur=self.img.size         
        for y in range(x1,y1):
            for x in range(x1,y2):
                p=self.img.getpixel((x,y))
                avg = (p[0]+p[1]+p[2])/3
                if avg>=128:
                    avg=256
                else:
                    avg=0
                q=(avg,avg,avg)
                self.img.putpixel((x,y),q)
                
        return self.img
    
    def graylevel(self):
        largeur , hauteur=self.img.size  
        for y in range(hauteur):
            for x in range(largeur):
                p=self.img.getpixel((x,y))
                avg = int((p[0]+p[1]+p[2])/3)
                q=(avg,avg,avg)
                self.img.putpixel((x,y),q)
        return self.img
    
    def brightness(self,value):
        largeur , hauteur=self.img.size         
        for y in range(hauteur):
            for x in range(largeur):
                p=self.img.getpixel((x,y))
                q=(p[0]+value,p[1]+value,p[2]+value)
                self.img.putpixel((x,y),q)
        return self.img
    
    def reverse(self):
        largeur , hauteur=self.img.size         
        for y in range(hauteur):
            for x in range(largeur):
                p=self.img.getpixel((x,y))
                q=(255-p[0],255-p[1],255-p[2])
                self.img.putpixel((x,y),q)
        return self.img
    
    def mirror(self):
        largeur , hauteur=self.img.size
        imgr = Image.new('RGB',(largeur,hauteur))        
        for y in range(hauteur):
            for x in range(largeur):
                p=self.img.getpixel((x,y))
                imgr.putpixel((largeur-x-1,y),p)
        return imgr
    
    def rotation(self):
        largeur , hauteur=self.img.size
        imgr = Image.new('RGB',(hauteur,largeur))          
        for y in range(hauteur):
            for x in range(largeur):
                p=self.img.getpixel((x,y))
                imgr.putpixel((y,x),p)
        return imgr
    
    def cut_color(self,color):
        largeur , hauteur=self.img.size
        for y in range(hauteur):
            for x in range(largeur):
                p=self.img.getpixel((x,y))
                if(color=="red"):
                    q=(0,p[1],p[2])
                if(color=="green"):
                    q=(p[0],0,p[2])
                if(color=="blue"):
                    q=(p[0],p[1],0)
                self.img.putpixel((x,y),q)
        return self.img
    
    def red_plus(self,value):
        largeur , hauteur=self.img.size
        for y in range(hauteur):
            for x in range(largeur):
                p=self.img.getpixel((x,y))
                q=(p[0]+value,p[1],p[2])
                self.img.putpixel((x,y),q)
        return self.img
    
    def green_plus(self,value):
        largeur , hauteur=self.img.size
        for y in range(hauteur):
            for x in range(largeur):
                p=self.img.getpixel((x,y))
                q=(p[0],p[1]+value,p[2])
                self.img.putpixel((x,y),q)
        return self.img
    
    def blue_plus(self,value):
        largeur , hauteur=self.img.size
        for y in range(hauteur):
            for x in range(largeur):
                p=self.img.getpixel((x,y))
                q=(p[0],p[1],p[2]+value)
                self.img.putpixel((x,y),q)
        return self.img
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    