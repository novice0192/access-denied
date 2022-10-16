import os
import sys
from pdf2jpg import pdf2jpg
from pdf2image import convert_from_path
abs_dir_path = os.path.abspath(os.getcwd())
itr = 10 # To keep track of which pdf is being converted
while itr<=10:
    images = convert_from_path("{}\pdfs\{}.pdf".format(abs_dir_path,itr))
    for i in range(len(images)):
        images[i].save("converted-images\{}_{}.jpg".format(str(itr),str(i+1)),'JPEG')
    print("Done with {}".format(itr))
    itr+=1
