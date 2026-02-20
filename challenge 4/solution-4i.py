from PIL import Image

img = Image.open('challenge 4/1.png').convert('RGB')
r, g, b = img.split()

r.save('challenge 4/1_red_layer.png')
g.save('challenge 4/1_green_layer.png') 
b.save('challenge 4/1_blue_layer.png')