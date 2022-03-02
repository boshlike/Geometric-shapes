from operator import length_hint
from PIL import Image
import random

# Using chaos x* (1 - x) * k to create tuples got an RGB image

# Makes an image out of a table of tuples with RGBA data in it
def make_image(values):
    image = Image.new('RGBA', (len(values[0]), len(values))) # Creates an image object with of (width, height)
    values = [item for sublist in values for item in sublist] # List comprehenstion thats flattens the values of the tuples table
    image.putdata(values) # Uses putdata method to put the pixel data into an image. Returns image object
    return image

# A function that generates values in the range 0 to 255 for x values between 0 and 1 in x_new = x * (1-x) *k
def chaos_function(iterations, initial_x, inital_k): # Iterations is the
    x = initial_x # Sets the inital value of x
    k = inital_k # sets the intial value of k
    table = [] # Initialise an empty table 
    for i in range(1,iterations):
        table.append(int(round(x*255, 0)))
        x = x * (1.0-x) * k
    return table        

# A funciton to create a line with length in pixels
def create_line(length):
    r = chaos_function(length+1, random.random(), random.uniform(0, 3.5)) # Creates the r values of the line
    g = chaos_function(length+1, random.random(), random.uniform(0, 3.5)) # Creates the g values of the line
    b = chaos_function(length+1, random.random(), random.uniform(0, 3)) # Creates the b values of the line
    a = chaos_function(length+1, random.random(), random.uniform(3.5, 4)) # Creates the alpha values of the line
    line_rgb = []
    for i in range(len(r)):
        tuple = (r[i], g[i], b[i], a[i])
        line_rgb.append(tuple)
    return line_rgb # Returns a table

# Create a list of (x,y) coordinates for a given length assuming a square
def pixels(length):
    pixel_list = [] #create the empty list that will contain the pixel tuples
    for j in range(length): # Nested loop to create the pixels from (0,0) to (length, length)
        for i in range(length):
            pixel = (j, i)
            pixel_list.append(pixel)
    return pixel_list

length = 100

pix = pixels(length)
random.shuffle(pix)

rgba_table = []
for i in range(length):
    line = create_line(length)
    rgba_table.append(line)

image = Image.new("RGBA", (len(rgba_table[0]), len(rgba_table)))
values = [item for sublist in rgba_table for item in sublist]

for i in range(len(pix)):
    image.putpixel(pix[i], values[i])
print(pix[0], values[0])
print(len(pix), len(values))
image.resize((1000,1000))
image.show()

#im = make_image(image_rgb_table).resize((1000, 1000)).rotate(90)
#im.show()