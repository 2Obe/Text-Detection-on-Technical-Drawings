# -*- coding: utf-8 -*-


from PIL import Image, ImageDraw, ImageFont
import numpy as np
import glob
import random
import cv2
from csv import writer


def image_type_3(num_imgs):
    """Generates defined number of image type 2 images in .jpg format and annotation file in .csv format.
    
        Args:
            num_imgs (int): Amount of images to generate
            
        
    """
    
    
    k=0
    
    while (k<num_imgs):
    
        width=random.randint(45,50)
        height=random.randint(25,35)
        
        # selvtion of fonts
        font_glossar=['seguisym.ttf','osifont.ttf','isocpeui.ttf', 'verdana.ttf', 'ARIALNB.ttf','cambria.ttc','unifont-14.0.02.ttf']
        font_glossar_choice=random.choice(font_glossar)
                    
        
        if font_glossar_choice=='seguisym.ttf':
            
            digits= ['-','+','H','x','1','2','3','4','5','6','7','8','9','0','.',',','\u2300','\u00B1'] 
           
        elif font_glossar_choice=='osifont.ttf': 
            
            digits= ['-','+','H','x','1','2','3','4','5','6','7','8','9','0','.',',','\u2300','\u00B1'] 
            
        elif font_glossar_choice=='cambria.ttc': 
            
            digits= ['-','+','H','x','1','2','3','4','5','6','7','8','9','0','.',',','\u2300','\u00B1']
            
        elif font_glossar_choice=='unifont-14.0.02.ttf': 
            
            digits= ['-','+','H','x','1','2','3','4','5','6','7','8','9','0','.',',','\u2300','\u00B1']
        
        else:
            
            digits= ['-','+','H','x','1','2','3','4','5','6','7','8','9','0','.',',']
        
        



        text=''
        word_length = random.randint(2, 4)    
        font_size=16
        

        j=0
        
        while j < word_length:
            text = text+random.choice(digits)
            j+=1
        
        
        
        fonts=glob.glob(font_glossar_choice)
        
        font=ImageFont.truetype(random.choice(fonts), font_size)
        
            
        image2=Image.new('RGBA', (width, height), (255,255,255))
        draw2=ImageDraw.Draw(image2)
        draw2.text((6, 5), text=text, font=font, fill=(0, 0, 0))
            
        
            
            
        image2=np.array(image2)                
        jpg_name = 'word00%s.jpg'%k
    
        cv2.imwrite(jpg_name, image2) 
    
        
        csv_instance = ('.\\train_digits\\word00%s.jpg'%k, None, text)
        
        
        with open('word_list.csv', 'a', newline='',encoding="utf-8") as f_object: 
            writer_object = writer(f_object)
            writer_object.writerow(csv_instance)
            f_object.close()
        
        
        k+=1



image_type_3(2)



