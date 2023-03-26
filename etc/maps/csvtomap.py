import csv
import os
def createMapFile(map_name, csvFileName, isBackground, bg_name, music_name, width, height):

    if(not isBackground):
        fileName = map_name + ".map"

        f = open(fileName, "w")
        f.write("|MAP GENERATED BY csvmap.py\n")
        f.write("BACKGROUND " + bg_name + "\n")
        f.write("MUSIC " + music_name + "\n")
        f.write("SIZE " + str(width) + " " + str(height) + "\n")
        f.write("GRAVITY 512\n")
        f.write("DEFAULT_FRICTION 0.8 0\n")

    else:
        fileName = map_name + ".map.background"
        f = open(fileName, "w")
        f.write("|BACKGROUND MAP GENERATED BY csvmap.py\n")


    csvFile = open(csvFileName)

    csvreader = csv.reader(csvFile)

    for i,row in enumerate(csvreader):
        for j,tile in enumerate(row):
            #print(tile,type(tile),j)
            if(tile=='-1'):
                continue
            else:
                if(tile=='1842'):
                    f.write("ENEMY Skeleton ")
                    f.write(str(j*32))
                    f.write(" ")
                    f.write(str(i*32))
                    f.write("\n")
                elif(tile=='1843'):
                    f.write("ENEMY Goblin ")
                    f.write(str(j*32))
                    f.write(" ")
                    f.write(str(i*32))
                    f.write("\n")
                elif(tile=='1844'):
                    f.write("ENEMY FlyingEye ")
                    f.write(str(j*32))
                    f.write(" ")
                    f.write(str(i*32))
                    f.write("\n")
                elif(tile=='1845'):
                    f.write("ENEMY Mushroom ")
                    f.write(str(j*32))
                    f.write(" ")
                    f.write(str(i*32))
                    f.write("\n")
                elif(tile=='1763'):
                    f.write("PLAYER ")
                    f.write(str(j*32))
                    f.write(" ")
                    f.write(str(i*32))
                    f.write("\n")
                elif(tile=='683'):
                    f.write("TILE ")
                    f.write(tile)
                    f.write(" ")
                    f.write(str(j))
                    f.write(" ")
                    f.write(str(i))
                    f.write(" WARP")
                    f.write("\n")
                else:
                    f.write("TILE ")
                    f.write(tile)
                    f.write(" ")
                    f.write(str(j))
                    f.write(" ")
                    f.write(str(i))
                    f.write("\n")
                

    csvFile.close()
    f.close()

    return fileName


# input files
layer1 = "map1_1.csv"
layer2 = "map1_2.csv"

# output
map_name = "map1"

# map parameters (no SPACEs)
bg_name = "Eg"
music_name = "TheDesert.wav"
width = 60
height = 60

fileMain = createMapFile(map_name, layer1, False, bg_name, music_name, width, height)

fileBackground = createMapFile(map_name, layer2, True, "", "", width, height)

commandMain = 'mv ' + fileMain + ' ../../Resources/media/Maps'

commandBackground = 'mv ' + fileBackground + ' ../../Resources/media/Maps'

os.system(commandMain)
os.system(commandBackground)
