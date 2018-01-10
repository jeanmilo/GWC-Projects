#size = 599, 654
DBLUE = (0, 51, 76)
LBLUE = (112, 150, 158)
RED =  (217, 26, 33)
YLLO = (252, 227, 166)
from PIL import Image
im = Image.open("kanyey.jpg")
im.show()
print([im.getdata])
pix = im.load()
print(im.size)
pixels = im.getdata()
pixel_list =list(pixels)
pixel_list2 = [ ]
for pixel in pixel_list:
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]
      total = r + g + b
      if total < 182:
            pixel_list2.append(DBLUE)
            
      elif total > 546:
            pixel_list2.append(YLLO)
      elif total >= 182 and total <= 364:
            pixel_list2.append(RED)
      elif total > 364 and total <=546:
            pixel_list2.append(LBLUE)
new_image = Image.new("RGB", im.size)
new_image.putdata(pixel_list2)
new_image.save("insertNewImageFileName.jpg", "jpeg")
im = Image.open("insertImageFileName.jpg")
im.show()
##Image.new(mode, size) 
##Image.new(mode, size, color) 
##
##im.size ⇒ (, height)
