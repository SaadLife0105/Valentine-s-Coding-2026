from PIL import Image
import numpy as np

# .convert("L") transforms the image to grayscale (8-bit pixels, 0-255).
img1 = np.array(Image.open("challenge 3/moitie1.png").convert("L"))
img2 = np.array(Image.open("challenge 3/moitie2.png").convert("L"))

# Flip the second image vertically to align it for the XOR operation.
img2 = np.flipud(img2)

# Combine the two images using a bitwise XOR (Exclusive OR) operation.
# This operation compares the binary values of pixels: 
# It returns a 1 only if the bits are different, often revealing hidden 
# patterns where two partial images overlap.
combined = img1 ^ img2

# Result is currently mirrored. 
# We use np.fliplr to flip it horizontally (Left-to-Right).
final_result = np.fliplr(combined)

# Convert the resulting NumPy array back into a PIL Image object
# and open the default system image viewer to display the result.
Image.fromarray(final_result).show()