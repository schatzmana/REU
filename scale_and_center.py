# take in an object .tri file, & a scale float
# makes a  new file c   alled .trifile_scale.rob
# i.e. python scale_and_center.py ../data/objects/cube.tri .5 --> cube_.5.tri

import sys

if len(sys.argv) != 3:
    print "Error: pass in script name, object tri file, and scale" #, and new file name"

else:
    # sys.argv[0] = script name
    tri_file = sys.argv[1]
    scale = sys.argv[2]

    # there are 12 translational vectors in the .rob file.
    # translational vectors:
    # a b c, d e f, g h i, j k l

    if tri_file == "../data/objects/cube.tri": #may need to switch this later to allow access from different directories
        # print "sucessfully compared string to cube YAY" #verified that this form of string comp works
        name = "cube"
        j = float(scale) * -0.5
        k = float(scale) * -0.5
        l = -(float(scale) + 0.11)

    # elif tri_file == "../data/objects/cylinder_y.tri":
    # more elifs for different shapes

    filename = "../data/robots/" + name + scale + ".rob"
    print filename

    # write new .rob file with above constructed filename
    newfile = open(filename, "w")
    robtext = open("./Part1.txt", 'r')
    newfile.write( robtext.read() )

    robtext2 = open("./Part2.txt", 'r')
    jkl = str(j)+" "+str(k)+" "+str(l)+"\n"
    last_tv = "1 0 0 0 1 0 0 0 1 "+jkl
    newfile.write( last_tv )
    newfile.write( robtext2.read() )
"""
# CUBE:
j = scale * -0.5
k = scale * -0.5
l = scale + 0.11

# CYLINDER_Y:

"""
