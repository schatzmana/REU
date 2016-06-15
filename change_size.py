# takes in two arguments: scale_index and a .tri file
# scale_index = float by which to multiply all nums by to scale an object
# scale_index = +/- percentage by which to multiple all dimensional nums
# 2,4,6 w/ -.5 => -1.0,-2.0,-3.0

import sys

if len(sys.argv) != 3:
    print "Error: pass in script name, scale percentage, object tri file"

else:
    scale_index = float(sys.argv[1])
    print "scale index= %s" %scale_index
    tri_file = sys.argv[2]

    trifile = open(tri_file, "r+")
    newfile = open("../data/objects/newfile.tri", "w")
    vert_count = int( trifile.readline() )
    newfile.write(str(vert_count)+"\n")
    print "vertice count: %s" %vert_count

    # read each line for the next vert_count lines
    # parse each line into the three x,y,z values
    # multiply each of the three coordinates by scale_index
    # either save these new values or write them to a new file

    # creates list of list of vertices
    # [ vert1, vert2, vert3, etc...]
    # where vert1 = ['x', 'y', 'z']
    vertices = []
    for each in range(0, vert_count):
        coordinate = trifile.readline().strip('\n')
        vertices.append( coordinate.split() )

    for vert in range(len(vertices)):
        x = float( vertices[vert][0] )
        y = float( vertices[vert][1] )
        z = float( vertices[vert][2] )
        print "originals are: ", x, y, z

        # scaling:
        x *= scale_index
        y *= scale_index
        z *= scale_index
        print "scaled coords are: ",x,y,z

        str_xyz = str(x) +" " + str(y) + " " + str(z)
        print "string coords are: " + str_xyz +"\n"
        newfile.write(str_xyz + "\n")

    tri_count = int( trifile.readline() )
    newfile.write(str(tri_count)+"\n")
    print "tri_count: %s" %tri_count

    # read line by line of triangle coords (verts) & write them
    for each in range(0, tri_count):
        tri_coord = trifile.readline()
        print tri_coord
        newfile.write(tri_coord)
    # write out new values to file
