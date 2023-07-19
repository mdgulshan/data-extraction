from PIL import Image
from pytesseract import pytesseract
import pandas as pd
import os
import re
from tabulate import tabulate
path_to_tesseract = r"C:\Users\gm67149\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Defining paths to tesseract.exe
# and the image we would be using
def extract_informartion(document_type,image_path):
    # Opening the image & storing it in an image object
    img = Image.open(image_path)
# Providing the tesseract executable
# location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract
# Passing the image object to image_to_string() function
# This function will extract the text from the image
    text = pytesseract.image_to_string(img)
    #text = pytesseract.image_to_string(img)
    processed_dict = {}
    if document_type=="PAN":
        text = text.split("\n\n")
        print(text)
        print("\n\n")
        processed_text = []
        for line in text:
            if line.count('Permanent') or line.count('Name'):
                processed_text.append(line)
                for line in processed_text:
                    data = line.split('\n')
                    key = data[0].split('/')[1] if len(data[0].split('/'))>1 else data[0]
                    processed_dict[key]=data[1]
        print(processed_dict)
    if document_type=="Aadhar":
        print(text)
        text = text.split("\n\n")
        print(text)
        print("\n\n")
        processed_text = []
        for line in text:
            names = re.findall(r'(?<=[a-z,][ ])([A-Z][a-z]*)', line)
            numbers = re.findall(r'\b\d\d\d\d\b',line)
            if len(names)>0 and len(names[0])>2:
                processed_dict['Name'] = "".join(names)
            if len(numbers)>2:
                processed_dict['Aadhar No'] = " ".join(numbers[:3])
            if line.count('DOB'):
                dob_text = line.split(':')
                processed_dict[dob_text[0].split('/')[1]] = dob_text[1].split('\n')[0]
        print(processed_dict)
    return processed_dict


#C:\Users\gm67149\AppData\Local\Programs\Tesseract - OCR\tesseract.exe

 


