# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import numpy as np
import glob
import random
import cv2
import xml.etree.ElementTree as xml
from sys import exit




def geometrie_generator(punkt,anzahl_poly=4,dicke=2,farbe='black'):
    """Generates a geometrie with dimensioning on a blank image
    
        Args:
            punkt (tuple): start point
            anzahl_poly (int): number of polygons the geometry consists of
            dicke (int): line thickness of geometry
            farbe (str): color of lines
            
        Returns:
            lower_right_pt (tuple): x and y coordinates of the lower right point of the geometry 
    """
    
    
    
    
    
    
    
    def mass_poly():
        """Sets the height and width randomly and returns it as a tuple"""
        
        
        
        width=random.randint(25,100)
        height=random.randint(50,150)
        
        mass=(width,height)
        
        return mass








                
        
    def poly_generator(point,dim):
        """ Generates a polygon.
            
            Args:
                point (tuple): Start point of polygon
                dim (tuple): width and heigth of the polygon to be generated    
            Returns:
                p0_v: coordinates of center point of line between upper right and lower right points
                p_s: coordinates of corner points
        
        """
        
        
        
        p0 = point
    
        p1 = (p0[0],int(p0[1]-dim[1]/2))
        p2 = (p1[0],p1[1]+dim[1])
        p3 = (p1[0]+dim[0],p1[1])
        p4 = (p1[0]+dim[0],p1[1]+dim[1])
        
        p0_v = (p0[0]+dim[0],p0[1])
        
        p_s = (p1,p2,p3,p4)
        
        draw.line([tuple(p1),tuple(p2)], fill=farbe, width=dicke, )
        draw.line([tuple(p1),tuple(p3)], fill=farbe, width=dicke, )
        draw.line([tuple(p2),tuple(p4)], fill=farbe, width=dicke, )
        draw.line([tuple(p3),tuple(p4)], fill=farbe, width=dicke, )

        
                                        
        return p0_v, p_s
    
    








    
    
    def symmetrielinie(pt1,pt2):
        """Generates a symmetry line between two points
        
            Args:
                pt1 (tuple): start point
                pt2 (tuple): end point
               
        """
        
        laenge_striche = 20
        laenge_short_striche = 4
        leange_gestr_linie = pt2[0]-pt1[0]+50

        m=0

        while m<leange_gestr_linie:
    
            dash_an = (pt1[0]-25+m,pt1[1])
            dash_end = (dash_an[0]+laenge_striche,dash_an[1])
    
            short_dash_an = (pt1[0]-25+m+28,pt1[1])
            short_dash_end = (short_dash_an[0]+laenge_short_striche,short_dash_an[1])
    
    
    
            draw.line([tuple(dash_an),tuple(dash_end)], fill='black', width=1, )
            draw.line([tuple(short_dash_an),tuple(short_dash_end)], fill='black', width=1, ) 
    
            m+=40
    
    
    
    
    
    
    def bemassung_geometrie_ver(punkt_liste, farbe='black',dicke=1,):
        """ Adds vertical dimensioning of the generated geometry.
        
        Args:
            punkt_liste (list):
            farbe (str): color
            dicke (int): line thickness
            
        """
    
        font_glossar=['seguisym.ttf','osifont.ttf','isocpeui.ttf']
        font_glossar_choice=random.choice(font_glossar)
    
        if font_glossar_choice=='seguisym.ttf':        
            schriftausgleich=0
    
        elif font_glossar_choice=='osifont.ttf':       
            schriftausgleich=5
        
        else:
            schriftausgleich=-4
        
       
        
        pt_1 = punkt_liste[0]
        pt_2 = punkt_liste[1]
        pt_3 = punkt_liste[2]
                
        laenge_poly = pt_3[0]-pt_1[0]
        versatz = laenge_poly*(1/6)
        
        anfangspunkt = (pt_1[0]+(laenge_poly/2)+versatz,pt_1[1])
        endpunkt = (pt_2[0]+(laenge_poly/2)+versatz,pt_2[1])
        
        abstand_an_end = endpunkt[1]-anfangspunkt[1]
        
        
        draw.line([tuple(anfangspunkt),tuple(endpunkt)], fill='black', width=1, )
        
        
        
        flanke_li_endpfeil=(endpunkt[0]+2,endpunkt[1]-10)
        flanke_re_endpfeil=(endpunkt[0]-2,endpunkt[1]-10)
        
        flanke_li_anfangspfeil=(anfangspunkt[0]+2,anfangspunkt[1]+10)
        flanke_re_anfangspfeil=(anfangspunkt[0]-2,anfangspunkt[1]+10)
        
        draw.polygon([tuple(endpunkt),tuple(flanke_li_endpfeil),tuple(flanke_re_endpfeil)],fill=farbe,)
        draw.polygon([tuple(anfangspunkt),tuple(flanke_li_anfangspfeil),tuple(flanke_re_anfangspfeil)],fill=farbe,)
        
        
        
        
        if i == 0:
            aussen_mass_anfangspunkt=(pt_1[0]-30,pt_1[1])
            aussen_mass_endpunkt = (pt_2[0]-30,pt_2[1])
        
            aussen_mass_anfangspunkt_bem=(pt_1[0]-33,pt_1[1])
            aussen_mass_endpunkt_bem=(pt_2[0]-33,pt_2[1])
            
            draw.line([tuple(aussen_mass_anfangspunkt),tuple(aussen_mass_endpunkt)], fill='black', width=1, )
            aussen_flanke_li_endpfeil=(aussen_mass_endpunkt[0]+2,aussen_mass_endpunkt[1]-10)
            aussen_flanke_re_endpfeil=(aussen_mass_endpunkt[0]-2,aussen_mass_endpunkt[1]-10)
        
            aussenflanke_li_anfangspfeil=(aussen_mass_anfangspunkt[0]+2,aussen_mass_anfangspunkt[1]+10)
            aussenflanke_re_anfangspfeil=(aussen_mass_anfangspunkt[0]-2,aussen_mass_anfangspunkt[1]+10)
        
            draw.polygon([tuple(aussen_mass_endpunkt),tuple(aussen_flanke_li_endpfeil),tuple(aussen_flanke_re_endpfeil)],fill=farbe,)
            draw.polygon([tuple(aussen_mass_anfangspunkt),tuple(aussenflanke_li_anfangspfeil),tuple(aussenflanke_re_anfangspfeil)],fill=farbe,)
        
            draw.line([tuple(aussen_mass_anfangspunkt_bem),tuple(pt_1)], fill='black', width=1, )
            draw.line([tuple(aussen_mass_endpunkt_bem),tuple(pt_2)], fill='black', width=1, )
            
            multiplikator = 0.5
            font_size=12
            text = abstand_an_end*multiplikator
    
    
            text_int = text.is_integer()
    
            if text_int == True:
                #print('True')
                text=int(text)
                puffer = 6
            else:
                text=float(text)
                puffer = 9
    
            text = str(text)
        
            spacing_choice=['',' ','  ']
        
            spacing=random.choice(spacing_choice)
        
            text = '\u2300' + spacing + text
            text = text.replace('.',',')
        
        
        
        
            
            
            fonts=glob.glob(font_glossar_choice)
            
            font=ImageFont.truetype(random.choice(fonts), font_size)
            width, height=font.getsize(text)
        
        
            image2=Image.new('RGBA', (width, height+2), (255,255,255))
            draw2=ImageDraw.Draw(image2)
            draw2.text((0, 0), text=text, font=font, fill=(0, 0, 0))
            image2=np.array(image2)
            image2=image2[0:height, 0:width]
            image2=Image.fromarray(image2)
        
            image2=image2.rotate(90, expand=1)
        
        
            txt_pt = (int(aussen_mass_anfangspunkt[0]-font_size-3-schriftausgleich),int(aussen_mass_anfangspunkt[1]+abstand_an_end/2-puffer))
        
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
            
         
            
        
        
        if i == anzahl_poly-1:
            
            aussen_mass_anfangspunkt=(pt_1[0]+laenge_poly+30,pt_1[1])
            aussen_mass_endpunkt = (pt_2[0]+laenge_poly+30,pt_2[1])
        
            aussen_mass_anfangspunkt_bem=(pt_1[0]+laenge_poly+33,pt_1[1])
            aussen_mass_endpunkt_bem=(pt_2[0]+laenge_poly+33,pt_2[1])
            
            draw.line([tuple(aussen_mass_anfangspunkt),tuple(aussen_mass_endpunkt)], fill='black', width=1, )
            aussen_flanke_li_endpfeil=(aussen_mass_endpunkt[0]+2,aussen_mass_endpunkt[1]-10)
            aussen_flanke_re_endpfeil=(aussen_mass_endpunkt[0]-2,aussen_mass_endpunkt[1]-10)
        
            aussenflanke_li_anfangspfeil=(aussen_mass_anfangspunkt[0]+2,aussen_mass_anfangspunkt[1]+10)
            aussenflanke_re_anfangspfeil=(aussen_mass_anfangspunkt[0]-2,aussen_mass_anfangspunkt[1]+10)
        
            draw.polygon([tuple(aussen_mass_endpunkt),tuple(aussen_flanke_li_endpfeil),tuple(aussen_flanke_re_endpfeil)],fill=farbe,)
            draw.polygon([tuple(aussen_mass_anfangspunkt),tuple(aussenflanke_li_anfangspfeil),tuple(aussenflanke_re_anfangspfeil)],fill=farbe,)
        
            draw.line([tuple(aussen_mass_anfangspunkt_bem),tuple(pt_1)], fill='black', width=1, )
            draw.line([tuple(aussen_mass_endpunkt_bem),tuple(pt_2)], fill='black', width=1, )
            
            multiplikator = 0.5
            font_size=12
            text = abstand_an_end*multiplikator
    
    
            text_int = text.is_integer()
    
            if text_int == True:
                
                text=int(text)
                puffer = 6
            else:
                text=float(text)
                puffer = 9
    
            text = str(text)
        
            spacing_choice=['',' ','  ']
        
            spacing=random.choice(spacing_choice)
        
            text = '\u2300' + spacing + text
            text = text.replace('.',',')
        
        
        
        
            
            
            fonts=glob.glob(font_glossar_choice)
            
            font=ImageFont.truetype(random.choice(fonts), font_size)
            width, height=font.getsize(text)
        
        
            image2=Image.new('RGBA', (width, height+2), (255,255,255))
            draw2=ImageDraw.Draw(image2)
            draw2.text((0, 0), text=text, font=font, fill=(0, 0, 0))
            image2=np.array(image2)
            image2=image2[0:height, 0:width]
            image2=Image.fromarray(image2)
        
            image2=image2.rotate(90, expand=1)
        
        
            txt_pt = (int(aussen_mass_anfangspunkt[0]-font_size-3-schriftausgleich),int(aussen_mass_anfangspunkt[1]+abstand_an_end/2-puffer))
        
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
            
        
        
        
        
        
        
        #Textbild
        
        multiplikator = 0.5
        font_size=12
        text = abstand_an_end*multiplikator
    
    
        text_int = text.is_integer()
    
        if text_int == True:
            
            text=int(text)
            puffer = 6
        else:
            text=float(text)
            puffer = 9
    
        text = str(text)
        
        spacing_choice=['',' ','  ']
        
        spacing=random.choice(spacing_choice)
        
        text = '\u2300' + spacing + text
        text = text.replace('.',',')
        
        
        
        
        
        
        fonts=glob.glob(font_glossar_choice)
        
        font=ImageFont.truetype(random.choice(fonts), font_size)
        width, height=font.getsize(text)
        
        
        image2=Image.new('RGBA', (width, height+2), (255,255,255))
        draw2=ImageDraw.Draw(image2)
        draw2.text((0, 0), text=text, font=font, fill=(0, 0, 0))
        image2=np.array(image2)
        image2=image2[0:height, 0:width]
        image2=Image.fromarray(image2)
        
        image2=image2.rotate(90, expand=1)
        
        
        txt_pt = (int(anfangspunkt[0]-font_size-3-schriftausgleich),int(anfangspunkt[1]+abstand_an_end/2-puffer))
        
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
        
        
        
        
        
        

    def bemassung_geometrie_hor(punkt_liste,farbe='black',dicke=1):
        """ Adds horizontal dimensioning of the generated geometry.
        
        Args:
            punkt_liste (list):
            farbe (str): color
            dicke (int): line thickness
            
        """
        
        
        font_glossar=['seguisym.ttf','osifont.ttf','isocpeui.ttf']
        font_glossar_choice=random.choice(font_glossar)
    
        passmass_char=['c9','d9','e7','e8','e9','f6','f7','f8','g5','g6','h5','h6','h7','h8','h9','js5','js6','k5','k6',
                       'm5','m6','n5','n6','p5','p6','r5','r6','s6','t6','u6','x6',]
        
        
        
        
        if font_glossar_choice=='seguisym.ttf':        
            schriftausgleich=0
    
        elif font_glossar_choice=='osifont.ttf':       
            schriftausgleich=4
        
        else:
            schriftausgleich=-2
        
        

        abstand=random.randint(50,100)
        
        hor_pt_1 = punkt_liste[1]
        hor_pt_2 = punkt_liste[3]
        
        anfangspunkt = (hor_pt_1[0],hor_pt_1[1]+abstand)
        endpunkt = (hor_pt_2[0],hor_pt_2[1]+abstand)
    
        abstand_an_end = hor_pt_2[0]-hor_pt_1[0]
        
       
        
        if abstand_an_end >= 30:
        
            flanke_li_endpfeil=(endpunkt[0]-10,endpunkt[1]+2)
            flanke_re_endpfeil=(endpunkt[0]-10,endpunkt[1]-2)
        
            flanke_li_anfangspfeil=(anfangspunkt[0]+10,anfangspunkt[1]-2)
            flanke_re_anfangspfeil=(anfangspunkt[0]+10,anfangspunkt[1]+2)
        
        else:
            flanke_li_endpfeil=(endpunkt[0]+10,endpunkt[1]+2)
            flanke_re_endpfeil=(endpunkt[0]+10,endpunkt[1]-2)
        
            flanke_li_anfangspfeil=(anfangspunkt[0]-10,anfangspunkt[1]-2)
            flanke_re_anfangspfeil=(anfangspunkt[0]-10,anfangspunkt[1]+2)
            
            
        
        draw.line([tuple(anfangspunkt),tuple(endpunkt)], fill=farbe, width=dicke, )
        
        
           
        bemassung_li_1=(anfangspunkt[0],anfangspunkt[1]+3)
        bemassung_li_2=(endpunkt[0],endpunkt[1]+3)
        
        draw.line([tuple(hor_pt_1),tuple(bemassung_li_1)], fill=farbe, width=dicke, )
        draw.line([tuple(hor_pt_2),tuple(bemassung_li_2)], fill=farbe, width=dicke, )
        
        
        
        
        draw.polygon([tuple(endpunkt),tuple(flanke_li_endpfeil),tuple(flanke_re_endpfeil)],fill=farbe,)
        draw.polygon([tuple(anfangspunkt),tuple(flanke_li_anfangspfeil),tuple(flanke_re_anfangspfeil)],fill=farbe,)
    
        
        rand_multiplikator= random.uniform(0.7,2.0)
        multiplikator = 0.5
        font_size=12
        text = round(abstand_an_end*multiplikator*rand_multiplikator,2)
        
        min_groesse=None
        
        text_int = text.is_integer()
    
        if text_int == True:
            
            text=int(text)
            puffer = 6
        else:
            text=float(text)
            puffer = 9
        
        if text>50:
            min_groesse=True
        
        text = str(text)
        
        text = text.replace('.',',')
        
        passmass_thresh=random.uniform(0, 1)
        
        if passmass_thresh<0.2 and min_groesse==True:
            text = text +' '+ random.choice(passmass_char)
        
        
        txt_pt = (anfangspunkt[0]+abstand_an_end/2-puffer-2,anfangspunkt[1]-font_size-3-schriftausgleich)
        
        fonts=glob.glob(font_glossar_choice)
        
        font=ImageFont.truetype(random.choice(fonts), font_size)
        width, height=font.getsize(text) 
        draw.text(txt_pt, text=text, font=font, fill=(0, 0, 0))
        
        
        
        
        # Bounding Boxes
        
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
        
        
        
    
    
    
    
    
    i=0     
    while i<anzahl_poly:
    
        groesse=mass_poly()
        
        punkt,corner_pts=poly_generator(punkt,groesse)
        
        bemassung_geometrie_hor(corner_pts)
        
        if i==0:
            symmetrielinie(pt,punkt)
        
        symmetrielinie(punkt,corner_pts[3])
        
        bemassung_geometrie_ver(corner_pts)
        
        poly_pts.append(corner_pts)
        
        i+=1
        
    
    lower_right_pt = corner_pts[3]
    
    
    
    return lower_right_pt





















def bemassung_ges(pt1,pt2):
    """ Adds horizontal dimensioning of geometries lenght.
        
        Args:
            pt1 (tuple): start point
            pt2 (tuple): end point
            
    """    
    
    
    font_glossar=['seguisym.ttf','osifont.ttf','isocpeui.ttf']
    font_glossar_choice=random.choice(font_glossar)
    
    if font_glossar_choice=='seguisym.ttf':        
        schriftausgleich=0
    
    elif font_glossar_choice=='osifont.ttf':       
        schriftausgleich=4
        
    else:
        schriftausgleich=-2
        
    
    hoehen = (pt1[1],pt2[1])
    max_hoehe = max(hoehen)
    
    anfangspunkt = (pt1[0],max_hoehe+135)
    endpunkt = (pt2[0],max_hoehe+135)
    
    abstand_an_end= endpunkt[0]-anfangspunkt[0]
       
    draw.line([tuple(anfangspunkt),tuple(endpunkt)], fill='black', width=1, )

    flanke_li_endpfeil=(endpunkt[0]-10,endpunkt[1]+2)
    flanke_re_endpfeil=(endpunkt[0]-10,endpunkt[1]-2)
        
    flanke_li_anfangspfeil=(anfangspunkt[0]+10,anfangspunkt[1]-2)
    flanke_re_anfangspfeil=(anfangspunkt[0]+10,anfangspunkt[1]+2)
    
    
    draw.polygon([tuple(endpunkt),tuple(flanke_li_endpfeil),tuple(flanke_re_endpfeil)],fill='black',)
    draw.polygon([tuple(anfangspunkt),tuple(flanke_li_anfangspfeil),tuple(flanke_re_anfangspfeil)],fill='black',)

    bemassung_li_1=(anfangspunkt[0],anfangspunkt[1]+3)
    bemassung_li_2=(endpunkt[0],endpunkt[1]+3)
        
    draw.line([tuple(pt1),tuple(bemassung_li_1)], fill='black', width=1, )
    draw.line([tuple(pt2),tuple(bemassung_li_2)], fill='black', width=1, )


    multiplikator = 0.5
    font_size=12
    text = abstand_an_end*multiplikator
    
    
    text_int = text.is_integer()
    
    if text_int == True:
        
        text=int(text)
        puffer = 6
    else:
        text=float(text)
        puffer = 9
    
    text = str(text)
    text = text.replace('.',',')

    
        
    txt_pt = (anfangspunkt[0]+abstand_an_end/2-puffer,anfangspunkt[1]-font_size-3-schriftausgleich)
        
    fonts=glob.glob(font_glossar_choice)
    #Schriftart, Groesse, index
    font=ImageFont.truetype(random.choice(fonts), font_size)
    width, height=font.getsize(text) 
    
    draw.text(txt_pt, text=text, font=font, fill=(0, 0, 0))

    #######################Bounding Box

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
    
    
    



    


    
    

def frame(padding=40,farbe='black', dicke=2):
    """ Adds a drawing frame to the image
        
        Args:
            padding (int): spacing between frame and image border
            farbe (str): color of frame
            dicke (int): line thickness
            
    """   
    
    pt1 = (0+padding,0+padding)
    pt2 = (0+padding,img_y-padding)
    pt3 = (img_x-padding,img_y-padding)  
    pt4 = (img_x-padding,0+padding)

    draw.line([tuple(pt1),tuple(pt2)], fill=farbe, width=dicke, )
    draw.line([tuple(pt2),tuple(pt3)], fill=farbe, width=dicke, )
    draw.line([tuple(pt3),tuple(pt4)], fill=farbe, width=dicke, )
    draw.line([tuple(pt4),tuple(pt1)], fill=farbe, width=dicke, )


    

def tolerance(number=3,pts=[(100,100),(200,100),(300,100)]):
    """ Adds tolerances to the geometry.
        
        Args:
            number (int): number of tolerances to be generated
            pts (list): startpoints
            
            
    """ 
    
    font_glossar=['seguisym.ttf','osifont.ttf']
    
    
    special_char_segu=['\u25B1','\u25CB','\u232D','\u2312','\u2313','\u27C2','\u2220','\u2316','\u25CE','\u232F','\u2197','\u2330']
    special_char_osiu=['\u25CB','\u232D','\u2312','\u2313','\u2220','\u2316','\u25CE','\u232F','\u2197','\u2330']
    
    dependencies_char=['A','B','C','D']
    
    font_glossar_choice=random.choice(font_glossar)
            
    if font_glossar_choice=='seguisym.ttf':
        text = random.choice(special_char_segu)
        schriftausgleich=0
    else:
        text = random.choice(special_char_osiu)
        schriftausgleich=4
    
    
    
    
    if number != len(pts):
        
        print('Error: Number does not match points!')
        exit()
    else:
        
        i=0        
        while i < number:
            
            if i%2 == 0:
                multiplikator=10*i
            else:
                multiplikator=-10*i
            
            
            anfangspunkt = pts[i]
            anfangspunkt = (anfangspunkt[0]+10,anfangspunkt[1])
            pfeil_pt1 = (anfangspunkt[0],anfangspunkt[1]-75+multiplikator)
            pfeil_pt2 = (anfangspunkt[0]+30,anfangspunkt[1]-75+multiplikator)
            
            flanke_li_anfangspfeil=(anfangspunkt[0]+2,anfangspunkt[1]-10)
            flanke_re_anfangspfeil=(anfangspunkt[0]-2,anfangspunkt[1]-10)
            
            p0 = (pfeil_pt2[0],pfeil_pt2[1]-10)
            p1 = (p0[0],p0[1]+21)
            p2 = (p0[0]+21,p0[1]+21)
            p3 = (p0[0]+21,p0[1])
        
            p4 = (p0[0]+63,p0[1])
            p5 = (p0[0]+63,p0[1]+21)
            p6 = (p4[0]+21,p4[1])
            p7 = (p4[0]+21,p4[1]+21)
            
            
            
            
            draw.line([tuple(anfangspunkt),tuple(pfeil_pt1)], fill='black', width=1, )
            draw.line([tuple(pfeil_pt1),tuple(pfeil_pt2)], fill='black', width=1, )
            
            
            draw.polygon([tuple(anfangspunkt),tuple(flanke_li_anfangspfeil),tuple(flanke_re_anfangspfeil)],fill='black',)
            
            
            
            
            draw.line([tuple(p0),tuple(p1)], fill='black', width=1, )
            draw.line([tuple(p1),tuple(p2)], fill='black', width=1, )
            draw.line([tuple(p2),tuple(p3)], fill='black', width=1, )
            draw.line([tuple(p3),tuple(p0)], fill='black', width=1, )
            draw.line([tuple(p3),tuple(p4)], fill='black', width=1, )
            draw.line([tuple(p2),tuple(p5)], fill='black', width=1, )
            draw.line([tuple(p4),tuple(p5)], fill='black', width=1, )
            draw.line([tuple(p4),tuple(p6)], fill='black', width=1, )
            draw.line([tuple(p5),tuple(p7)], fill='black', width=1, )
            draw.line([tuple(p6),tuple(p7)], fill='black', width=1, )
            
            
            
            
            if font_glossar_choice=='seguisym.ttf':
                text = random.choice(special_char_segu)
                schriftausgleich=0
            else:
                text = random.choice(special_char_osiu)
                schriftausgleich=4
            
            
            
            
            txt_pt = (p0[0]+3,p0[1]-schriftausgleich)
            
            fonts=glob.glob(font_glossar_choice)
            
            
            
            font=ImageFont.truetype(random.choice(fonts), 16)
            draw.text(txt_pt, text=text, font=font, fill=(0, 0, 0))
            
            
            
            text_2 = round(random.uniform(0, 0.1),2)
            text_2 = str(text_2)
            text_2 = text_2.replace('.',',')
            
            txt_pt2 = (p3[0]+9,p3[1]-1-schriftausgleich)
            draw.text(txt_pt2, text=text_2, font=font, fill=(0, 0, 0))
            
            text_3 = random.choice(dependencies_char)
            txt_pt3 = (p4[0]+5,p4[1]-schriftausgleich)
            draw.text(txt_pt3, text=text_3, font=font, fill=(0, 0, 0))
            
            min_x = p0[0]-2
            min_y = p0[1]-2
            max_x = p7[0]+2
            max_y = p7[1]+2

            b_box = (min_x, min_y, max_x, max_y)
            toler.append(b_box)
            
            
            
            i+=1
            
                

def augmentation(image):
    """ Augments generated image randomly
        
        Args:
            image : image to be augmented
        
        Returns:
            image : augmented image
    """     
        
    image= ImageEnhance.Sharpness(image)
    image= image.enhance(random.uniform(0.0,1.0))
        
    image= ImageEnhance.Brightness(image)
    image= image.enhance(random.uniform(0.8,1.4))
        
    image= ImageEnhance.Contrast(image)
    image= image.enhance(random.uniform(0.8,1.4))
        
    #image= ImageEnhance.Color(image)
    #image= image.enhance(random.uniform(0.5,2.0))  
        
    return image
            
#%%

num_imgs=4
annotation=True








k=0

while (k<num_imgs):
    
    img_x=random.randint(1200,1500)
    img_y=int(img_x/(2**(0.5)))
    
    masse_hor=[]
    masse_ver=[]
    toler=[]
    poly_pts=[]
    
    image=Image.new('RGBA', (img_x, int(img_y)), (255,255,255))
    
    draw = ImageDraw.Draw(image)
    
    
    delta_a = random.uniform(0.1, 0.6)
    delta_b = random.uniform(0.2, 0.75)
    
    pt = (int(img_x*(delta_a)),int(img_y*(delta_b)))
    
    
    
    
    
    frame()
    
    komma = geometrie_generator(pt,random.randint(5,7),2) 
        
    bemassung_ges(pt,komma)
    
    tolerance(3,pts=[poly_pts[0][0],poly_pts[2][0],poly_pts[4][0]])
        
    image=augmentation(image)
    
    
    
    
            
    img=np.array(image)
    cv2.imwrite('00%s.jpg'%k, img) #if you want to save the image
        
        
    #Annotation   
    
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
                
        while l < len(masse_ver):
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
            xmin.text=str(int(masse_ver[l][0]))
            ymin.text=str(int(masse_ver[l][1]-7))
            xmax.text=str(int(masse_ver[l][2]))
            ymax.text=str(int(masse_ver[l][3]+7))
        
            l+=1
        
        
        j=0
                
        while j < len(masse_hor):
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
            xmin.text=str(int(masse_hor[j][0]-7))
            ymin.text=str(int(masse_hor[j][1]))
            xmax.text=str(int(masse_hor[j][2]+7))
            ymax.text=str(int(masse_hor[j][3]))
        
            j+=1
        
        m=0
                
        while m < len(toler):
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
            name.text='toleranz'
            pose.text="Unspecified"
            truncated.text="0"
            difficult.text="0"
            xmin.text=str(int(toler[m][0]))
            ymin.text=str(int(toler[m][1]))
            xmax.text=str(int(toler[m][2]))
            ymax.text=str(int(toler[m][3]))
        
            m+=1
        
                
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



