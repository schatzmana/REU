# takes in two arguments: scale_index and a .tri file
# scale_index = float by which to multiply all nums by to scale an object
# scale_index = +/- percentage by which to multiple all dimensional nums
# 2,4,6 w/ -.5 => -1.0,-2.0,-3.0

import sys

if len(sys.argv) != 4:
    print "Error: pass in script name, cylinder_y.tri file, int of how many cylinders, scale"

else:
    tri_file = sys.argv[1]
    num = int(sys.argv[2])
    scale_index = float(sys.argv[3])


    trifile = open(tri_file, "r")
    filename = "../data/objects" + str(num) + "cylinder_y.tri"
    newfile = open(filename, "w")
    vert_count = int( trifile.readline() )
    newfile.write(str(vert_count*2)+"\n")
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
    # end of read and write for the first go through

    trifile.seek(0)     # takes read cursor back to beginning of file, so can reread vertices

    # now need to read through again and add vals
    for vert in range(len(vertices)):
        x = float( vertices[vert][0] )
        y = float( vertices[vert][1] )
        z = float( vertices[vert][2] )
        #print "originals are: ", x, y, z

        # scaling:
        x *= scale_index
        y = (y*scale_index)+2       # added 2 cause that's the height of cylinder_y
        z *= scale_index
        #print "scaled coords are: ",x,y,z

        str_xyz = str(x) +" " + str(y) + " " + str(z)
        #print "string coords are: " + str_xyz +"\n"
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

    # triangle coord lines begin on num vertices + 2 (vertices & triangle counts) + starts on line 1 (not 0)
    # num_+ tri_count + 3
    trifile.seek( (vert_count + tri_count + 3) )

    # reread triangles and add num to each vertice to account for additional set of vertices added
    triangles = []
    for each in range(0, tri_count):
        tri_coord = trifile.readline().strip('\n')
        triangles.append( tri_coord.split() )

        for coord in range( len(triangles) ):
            a = float( triangles[coord][0] )
            b = float( triangles[coord][1] )
            c = float( triangles[coord][2] )

            # scaling:
            a += vert_count
            b += vert_count
            c += vert_count

            str_abc = str(a) +" " + str(b) + " " + str(c)
            #print "string coords are: " + str_abc +"\n"
            newfile.write(str_abc + "\n")
