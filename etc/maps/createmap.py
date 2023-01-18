from PIL import Image
from numpy import asarray
# load the image
image = Image.open('map01.png')
# convert image to numpy array
data = asarray(image)
print(type(data))
# summarize shape
print(data.shape)

(width, height, alpha) = data.shape

f = open("map1.map", "w")
f.write("|MAP GENERATED BY createmap.py\n")
f.write("BACKGROUND Bg3\n")
f.write("SIZE " + str(height) + " " + str(width) + "\n")
f.write("GRAVITY 512\n")
f.write("DEFAULT_FRICTION 0.8 0\n")

for i in range(width):
    for j in range(height):
        pixel = data[i][j]
        if pixel[0] == 255:
            f.write("TILE 5 ")
            f.write(str(j))
            f.write(" ")
            f.write(str(i))
            f.write("\n")
            
        if pixel[0] == 91:
            f.write("PLAYER ")
            f.write(str(j*16))
            f.write(" ")
            f.write(str(i*16))
            f.write("\n")

        if pixel[1] == 255:
            f.write("ENEMY Rat ")
            f.write(str(j*16))
            f.write(" ")
            f.write(str(i*16))
            f.write("\n")


f.close()
        