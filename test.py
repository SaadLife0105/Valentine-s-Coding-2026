from PIL import Image

img = Image.open('challenge 4/2.png').convert('RGB')

r, g, b = img.split()

r.save('challenge 4/2_red_layer.png')
g.save('challenge 4/2_green_layer.png')
b.save('challenge 4/2_blue_layer.png')