from PIL import Image

# Open the image and ensure it's in standard RGB color mode
img = Image.open('challenge 4/2.png').convert('RGB')

# Separate the image into its three base color layers
# This creates three separate grayscale images representing Red, Green, and Blue
r, g, b = img.split()

# Save each layer as a separate file to inspect them individually
# Often, one layer will reveal a hidden pattern that the others hide
r.save('challenge 4/2_red_layer.png')
g.save('challenge 4/2_green_layer.png')
b.save('challenge 4/2_blue_layer.png')