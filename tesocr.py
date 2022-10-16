import pytesseract
from PIL import Image

#print(pytesseract.image_to_string(Image.open("screenshot.png")))

for x in range(6, 11):
    file = open(str(x)+".txt", "a")
    for y in range(1, 60):
        try:
            file.write(pytesseract.image_to_string(Image.open("images\\"+str(x)+"_"+str(y)+".jpg")))
        except:
            break
    file.close()
    print(x, "done")
