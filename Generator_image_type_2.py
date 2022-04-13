# -*- coding: utf-8 -*-


from PIL import Image, ImageDraw, ImageFont
import numpy as np
import glob
import random
import cv2
import xml.etree.ElementTree as xml





dir_path = "INSERT_PATH_OF_ELEMENT_DIR/*.jpg"
Images = glob.glob(dir_path)

print(len(Images),'elements were found and loaded!')








def image_type_2(num_imgs,annotation=True):
    """Generates defined number of image type 2 images in .jpg format and PASCAL VOC annotation file in .xml format.
    
    Args:
        num_imgs (int): Amount of images to generate
        annotation (bool): Wether an annotiation file should be generated
        
    """
       
    
    k=0
    
    while (k<num_imgs):
        
        masse_hor=[]
        durch_hor=[]
        masse_ver=[]
        durch_ver=[]
        
        
        # generation of blank image
        
        img_x=random.randint(1200,1500)
        img_y=int(img_x/(2**(0.5)))
        image=Image.new('RGBA', (img_x, int(img_y)), (255,255,255))
        
        
        # number of elements
        num_elements = random.randint(130,150)
        
        
        # creation of background 
        i=0
                
        while i < num_elements:
           
                
            element_choice = random.randint(0,194)
            element_location = (random.randint(0,img_x),random.randint(0,img_y))
            element = Image.open(Images[element_choice]) 
        
            image.paste(element, element_location)
        
            i+=1
        
        
        
        
        
        # horizontal dimensions
        
        j=0                    
        
        while j < 10:
            
            font_size=16
            
            
            threshold = random.uniform(0,1)
            
            if threshold > 0.75:
                text=random.randint(0,20)
            else:
                text=round(random.uniform(1,200), 1)
                text_int = text.is_integer()
                
                if text_int == True:
                     
                     text=int(text)
            
            
            
            text=str(text)
                                   
            text = text.replace('.',',')
            font_glossar=['seguisym.ttf','osifont.ttf','isocpeui.ttf']
            font_glossar_choice=random.choice(font_glossar)
            txt_pt = (random.randint(20,img_x-70),random.randint(20,img_y-30))
            
            fonts=glob.glob(font_glossar_choice)
            
            font=ImageFont.truetype(random.choice(fonts), font_size)
            width, height=font.getsize(text) 
            
            image2=Image.new('RGBA', (width, height), (255,255,255))
            draw2=ImageDraw.Draw(image2)
            draw2.text((0, 0), text=text, font=font, fill=(0, 0, 0))
            
            if font_glossar_choice == 'seguisym.ttf':
                image2 = image2.crop((0,3,width,height))
            
            if font_glossar_choice == 'osifont.ttf':
                image2 = image2.crop((0,5,width,height))
            
            
            image2=np.array(image2)
            image2=image2[0:height, 0:width]
            image2=Image.fromarray(image2)
            
            
            
            
            txt_pt = (random.randint(20,img_x-70),random.randint(20,img_y-30))
            image.paste(image2, txt_pt , image2)
            
            if font_glossar_choice=='isocpeui.ttf':
                min_x = txt_pt[0]
                min_y = txt_pt[1]-3
                max_x = txt_pt[0]+width+1
                max_y = txt_pt[1]+height+1+3 
        
            else:
        
                min_x = txt_pt[0]
                min_y = txt_pt[1]
                max_x = txt_pt[0]+width+1
                max_y = txt_pt[1]+height+1
            
            
            b_box = (min_x, min_y, max_x, max_y)
            masse_hor.append(b_box)
                                            
            
            j+=1
        
        
        
        
        
        
        
        
        # horizontal diameter
        
        m=0
        
        while m < 10:
            
            font_size=16
            text=round(random.uniform(1,200), 1)
            
            text_int = text.is_integer()
        
            if text_int == True:
                
                text=int(text)
            
            
            text=str(text)
                        
                        
            text = text.replace('.',',')
            
            spacing_choice=['',' ','  ']
            spacing=random.choice(spacing_choice)
            
            text = '\u2300' + spacing + text
            
            font_glossar=['seguisym.ttf','osifont.ttf','isocpeui.ttf']
            font_glossar_choice=random.choice(font_glossar)
                                                                                               
            fonts=glob.glob(font_glossar_choice)
            
            font=ImageFont.truetype(random.choice(fonts), font_size)
            width, height=font.getsize(text) 
            
            image2=Image.new('RGBA', (width, height), (255,255,255))
            draw2=ImageDraw.Draw(image2)
            draw2.text((0, 0), text=text, font=font, fill=(0, 0, 0))
            
            if font_glossar_choice == 'seguisym.ttf':
                image2 = image2.crop((0,3,width,height))
            
            if font_glossar_choice == 'osifont.ttf':
                image2 = image2.crop((0,5,width,height))
            
            image2=np.array(image2)
            image2=image2[0:height, 0:width]
            image2=Image.fromarray(image2)
            
            
            
            
            txt_pt = (random.randint(20,img_x-70),random.randint(20,img_y-30))
            image.paste(image2, txt_pt , image2)
            
            
            if font_glossar_choice=='isocpeui.ttf':
                min_x = txt_pt[0]
                min_y = txt_pt[1]-3
                max_x = txt_pt[0]+width+1
                max_y = txt_pt[1]+height+1+3 
        
            else:
        
                min_x = txt_pt[0]
                min_y = txt_pt[1]
                max_x = txt_pt[0]+width+1
                max_y = txt_pt[1]+height+1
            
            
            b_box = (min_x, min_y, max_x, max_y)
            durch_hor.append(b_box)
            
                                                            
            m+=1
        
        
        
        
 
       
        # vertical dimension
        
        o=0
        while o < 10:
            
            font_size=16
            text=round(random.uniform(1,200), 1)
            
            text_int = text.is_integer()
        
            if text_int == True:
                
                text=int(text)
            
                                                            
            text = str(text)
            
            spacing_choice=['',' ','  ']
            
            spacing=random.choice(spacing_choice)
            
            text = '\u2300' + spacing + text
            text = text.replace('.',',')
            
            font_glossar=['seguisym.ttf','osifont.ttf','isocpeui.ttf']
            font_glossar_choice=random.choice(font_glossar)
            
            
            unicode_text=text.encode('utf-8')
            
            fonts=glob.glob(font_glossar_choice)
            
            font=ImageFont.truetype(random.choice(fonts), font_size)
            width, height=font.getsize(text)
            
            
            image2=Image.new('RGBA', (width, height+2), (255,255,255))
            draw2=ImageDraw.Draw(image2)
            draw2.text((0, 0), text=text, font=font, fill=(0, 0, 0))
            
            if font_glossar_choice == 'seguisym.ttf':
                image2 = image2.crop((0,3,width,height))
            
            if font_glossar_choice == 'osifont.ttf':
                image2 = image2.crop((0,5,width,height))
            
            
            image2=np.array(image2)
            image2=image2[0:height, 0:width]
            image2=Image.fromarray(image2)
            
            image2=image2.rotate(90, expand=1)
            
            
            txt_pt = (random.randint(20,img_x-70),random.randint(20,img_y-70))
            
            image.paste(image2, txt_pt , image2)
            
            
            if font_glossar_choice=='isocpeui.ttf':
                
                min_x = txt_pt[0]-3
                min_y = txt_pt[1]+2
                max_x = txt_pt[0]+height+1+3
                max_y = txt_pt[1]+width-2
        
            else:
        
                min_x = txt_pt[0]
                min_y = txt_pt[1]-2
                max_x = txt_pt[0]+height+1
                max_y = txt_pt[1]+width
            
            
            
            
    
            
            b_box = (min_x, min_y, max_x, max_y)
            durch_ver.append(b_box)
        
            o+=1
        
        
        
        
        
        # vertical diameter
        
        q=0
        while q < 10:
            
            font_size=16
            text=round(random.uniform(1,200), 1)
            
            text_int = text.is_integer()
        
            if text_int == True:
                
                text=int(text)
            
           
            text = str(text)
            
            
            text = text.replace('.',',')
            
            font_glossar=['seguisym.ttf','osifont.ttf','isocpeui.ttf']
            font_glossar_choice=random.choice(font_glossar)
            
            
            unicode_text=text.encode('utf-8')
            
            fonts=glob.glob(font_glossar_choice)
            
            font=ImageFont.truetype(random.choice(fonts), font_size)
            width, height=font.getsize(text)
            
            
            image2=Image.new('RGBA', (width, height+2), (255,255,255))
            draw2=ImageDraw.Draw(image2)
            draw2.text((0, 0), text=text, font=font, fill=(0, 0, 0))
            
            if font_glossar_choice == 'seguisym.ttf':
                image2 = image2.crop((0,3,width,height))
            
            if font_glossar_choice == 'osifont.ttf':
                image2 = image2.crop((0,5,width,height))
            
            image2=np.array(image2)
            image2=image2[0:height, 0:width]
            image2=Image.fromarray(image2)
            
            image2=image2.rotate(90, expand=1)
            
            
            txt_pt = (random.randint(20,img_x-70),random.randint(20,img_y-70))
            
            image.paste(image2, txt_pt , image2)
            
            
            if font_glossar_choice=='isocpeui.ttf':
                
                min_x = txt_pt[0]-3
                min_y = txt_pt[1]+2
                max_x = txt_pt[0]+height+1+3
                max_y = txt_pt[1]+width-2
        
            else:
        
                min_x = txt_pt[0]
                min_y = txt_pt[1]-2
                max_x = txt_pt[0]+height+1
                max_y = txt_pt[1]+width
            
            
            
            
    
            
            b_box = (min_x, min_y, max_x, max_y)
            masse_ver.append(b_box)
        
            q+=1
        
        
                                            
        
        img=np.array(image)
        cv2.imwrite('00%s.jpg'%k, img)
            
            
        
            
            
        if annotation==True:    
            
        
            xml_doc = xml.Element("annotation")
            
            folder=xml.SubElement(xml_doc,"folder")
            filename=xml.SubElement(xml_doc,"filename")
            path=xml.SubElement(xml_doc,"path")
            source=xml.SubElement(xml_doc,"source")
            database=xml.SubElement(source,"database")
            size=xml.SubElement(xml_doc,"size")
            width=xml.SubElement(size,"width")
            height=xml.SubElement(size,"height")
            depth=xml.SubElement(size,"depth")
            segment=xml.SubElement(xml_doc,"segmented")
                    
                              
            
            folder.text="Test"
            filename.text=("00%s.jpg"%k)
            path.text="Unknown"
            database.text="Unknown"
            width.text=str(img_x)
            height.text=str(img_y)
                    
            #depth grayscale=0, color=3
            depth.text="3"
            segment.text="0"
                    
            
            l=0
                    
            while l < len(masse_hor):
                xml_object=xml.SubElement(xml_doc,"object")
                name=xml.SubElement(xml_object,"name")
                pose=xml.SubElement(xml_object,"pose")
                truncated=xml.SubElement(xml_object,"truncated")
                difficult=xml.SubElement(xml_object,"difficult")        
                bndbox=xml.SubElement(xml_object,"bndbox")
                xmin=xml.SubElement(bndbox,"xmin")
                ymin=xml.SubElement(bndbox,"ymin")
                xmax=xml.SubElement(bndbox,"xmax")
                ymax=xml.SubElement(bndbox,"ymax")                        
                name.text='mass_hor'
                pose.text="Unspecified"
                truncated.text="0"
                difficult.text="0"
                xmin.text=str(int(masse_hor[l][0]))
                ymin.text=str(int(masse_hor[l][1]-2))
                xmax.text=str(int(masse_hor[l][2]))
                ymax.text=str(int(masse_hor[l][3]+2))
            
                l+=1
            
            
            n=0
                    
            while n < len(durch_hor):
                xml_object=xml.SubElement(xml_doc,"object")
                name=xml.SubElement(xml_object,"name")
                pose=xml.SubElement(xml_object,"pose")
                truncated=xml.SubElement(xml_object,"truncated")
                difficult=xml.SubElement(xml_object,"difficult")        
                bndbox=xml.SubElement(xml_object,"bndbox")
                xmin=xml.SubElement(bndbox,"xmin")
                ymin=xml.SubElement(bndbox,"ymin")
                xmax=xml.SubElement(bndbox,"xmax")
                ymax=xml.SubElement(bndbox,"ymax")                        
                name.text='mass_hor'
                pose.text="Unspecified"
                truncated.text="0"
                difficult.text="0"
                xmin.text=str(int(durch_hor[n][0]))
                ymin.text=str(int(durch_hor[n][1]-2))
                xmax.text=str(int(durch_hor[n][2]))
                ymax.text=str(int(durch_hor[n][3]+2))
            
                n+=1
                    
            p=0
                    
            while p < len(masse_ver):
                xml_object=xml.SubElement(xml_doc,"object")
                name=xml.SubElement(xml_object,"name")
                pose=xml.SubElement(xml_object,"pose")
                truncated=xml.SubElement(xml_object,"truncated")
                difficult=xml.SubElement(xml_object,"difficult")        
                bndbox=xml.SubElement(xml_object,"bndbox")
                xmin=xml.SubElement(bndbox,"xmin")
                ymin=xml.SubElement(bndbox,"ymin")
                xmax=xml.SubElement(bndbox,"xmax")
                ymax=xml.SubElement(bndbox,"ymax")                        
                name.text='mass_ver'
                pose.text="Unspecified"
                truncated.text="0"
                difficult.text="0"
                xmin.text=str(int(masse_ver[p][0]))
                ymin.text=str(int(masse_ver[p][1]-2))
                xmax.text=str(int(masse_ver[p][2]))
                ymax.text=str(int(masse_ver[p][3]+2))
            
                p+=1
            
            r=0
                    
            while r < len(durch_ver):
                xml_object=xml.SubElement(xml_doc,"object")
                name=xml.SubElement(xml_object,"name")
                pose=xml.SubElement(xml_object,"pose")
                truncated=xml.SubElement(xml_object,"truncated")
                difficult=xml.SubElement(xml_object,"difficult")        
                bndbox=xml.SubElement(xml_object,"bndbox")
                xmin=xml.SubElement(bndbox,"xmin")
                ymin=xml.SubElement(bndbox,"ymin")
                xmax=xml.SubElement(bndbox,"xmax")
                ymax=xml.SubElement(bndbox,"ymax")                        
                name.text='mass_ver'
                pose.text="Unspecified"
                truncated.text="0"
                difficult.text="0"
                xmin.text=str(int(durch_ver[r][0]))
                ymin.text=str(int(durch_ver[r][1]-2))
                xmax.text=str(int(durch_ver[r][2]))
                ymax.text=str(int(durch_ver[r][3]+2))
            
                r+=1        
            
            
            
            
            
            
            def prettify(element, intend=' '):
                queue = [(0,element)]
                while queue:
                    level, element =queue.pop(0)
                    children = [(level + 1, child)for child in list(element)]
                    if children:
                        element.text = '\n' + intend * (level+1)
                        if queue:
                            element.tail = '\n' + intend * queue[0][0]
                        else:
                            element.tail = '\n' + intend * (level-1)
                            queue[0:0] = children
                    
            
            prettify(xml_doc)
                          
                        
            tree = xml.ElementTree(xml_doc)
            tree.write('00%s.xml'%k)
        
        
        
        
        k+=1
    
    
    
    
    
image_type_2(5)    
    
    
    
    
    
    
   