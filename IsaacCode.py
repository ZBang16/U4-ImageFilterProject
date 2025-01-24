# Isaac Zhao
# Period 5 AP CSP
# Unit 4 Image Filter Project


# Before running any code, please run the following in the shell :
# pip install -r requirement.txt

# importing PIL.Image library and os library
from PIL import Image #from PIL import Image 
import os

# Deletes old created images if they exist
images = ["combinedFilters.jpg","filter1.jpg","filter2.jpg","filter3.jpg","grey.jpg"]
for i in images:
  if os.path.exists(i):
    os.remove(i)

# Adds two blank lines before any output
print("\n\n")

# Opens image - upload a Local File into repl.it
img = Image.open('image.jpg')

# Rescale image size down, if original is too large
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
  scale = mwidth
else:
  scale = mheight
if scale != 0:
  img = img.resize( (width // scale, height // scale) )

# Negative Filter

def negative():
  # Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # For every pixel from our original image, it saves
  # a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results to a new red, green and blue components
    # For this particular filter (negative), the original r, g, and b components are subtracted from 255
    # This subtraction inverts the colors of the picture
    newr = 255 - r
    newg = 255 - g
    newb = 255 - b
    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original 
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  # Sends the newImage back to the main portion of program
  return newImage
# Saturation Filter

def saturation(saturationlevel):
# Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # For every pixel from our original image, it saves a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results to a new red, green and blue components
    # For this particular filter (saturation), the user's inputted saturation level is multiplied
    # by the original r, g, and b components to saturate the photo
    newr = r * saturationlevel
    newg = g * saturationlevel
    newb = b * saturationlevel
  # Assigns new red, green and blue components to the pixel at that specific location
    new_pixels[location] = (newr, newg, newb)
  # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  # Sends the newImage back to the main portion of program
  return newImage

# Brightness Filter

def brightness(brightnesslevel):
# Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # For every pixel from our original image, it saves a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results to a new red, green and blue components
    # For this particular filter (brightness), the user's inputted
    # brightness is added to the original r, g, and b components
    newr = r + brightnesslevel
    newg = g + brightnesslevel
    newb = b + brightnesslevel
    # Assigns new red, green and blue components to the pixel at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  # Sends the newImage back to the main portion of program
  return newImage

# Image filter names for use below
f1 = "negative"
f2 = "saturation"
f3 = "brightness"

# Creates the three filter images and saves them to our files
a = negative()
a.save("negative.jpg")
b = saturation(2)
b.save("saturation.jpg")
c = brightness(100)
c.save("brightness.jpg")

# Apply multiple filters through prompts with the user
answer = input("\nWhich filter do you want me to apply?\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
while answer != f1 and answer != f2 and answer != f3 and answer != "none":
  answer = input("\nIncorrect filter, please enter:\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")

# This loop constantly runs until user inputs "none" to end the filter processes
while answer == f1 or answer == f2 or answer == f3:
  if answer == f1:
   img = negative()
  elif answer == f2:
   satlvl = int(input("How much would you like to saturate your photo? Please enter a value between 0 and 2: "))
   while satlvl < 0 or satlvl > 2:
     satlvl = int(input("Invalid answer. Please enter a value between 0 and 2: "))
   img = saturation(satlvl)
  elif answer == f3:
   brightlvl = int(input("How much brightness would you like? Please enter a value from -100 to 100: "))
   while brightlvl < -100 or brightlvl > 100:
     brightlvl = int(input("Invalid answer. Please enter a value between -100 and 100: "))
   img = brightness(brightlvl)
  else:
    break
  print("Filter \"" + answer + "\" applied...")
  answer = input("\nWhich filter do you want me to apply next?\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
  while answer != f1 and answer != f2 and answer != f3 and answer != "none":
    answer = input("\nIncorrect filter, please enter:\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
# Once the user inputs something else, the loop ends and image is created
print("Image being created...Done")

# Create the combined filter image and saves it to our files
img.save("combinedFilters.jpg")