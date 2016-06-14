    # scale_index = float by which to multiply all nums by to scale an object
    # scale_index = +/- percentage by which to multiple all dimensional nums
    # i.e. change_size(2) = make object 2^n as big (cube 2*3)
    # change_size(.5) = half the nums

import sys

if len(sys.argv) != 3:
    print "Error: pass in script name, scale percentage, object tri file"

else:
    scale_index = float(sys.argv[1])
    tri_file = sys.argv[2]

    myfile = open(tri_file)
    vert_count = int( myfile.readline() )
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
        coordinate = myfile.readline().strip('\n')
        vertices.append( coordinate.split() )
    #print vertices

    for vert in range(len(vertices)):
        x = int( vertices[vert][0] )
        y = int( vertices[vert][1] )
        z = int( vertices[vert][2] )
        print x,y,z

        x *= scale_index
        y *= scale_index
        z *= scale_index
        print x,y,z

"""
        str_xyz = str(x) +" " + str(y) + " " + str(y)
        print str_xyz
        myfile.write(str_xyz)
"""
    tri_count = int( myfile.readline() )
    print "tri_count: %s" %tri_count
    # maybe parse triangles and scale them too?

    #


"""
    if scale_index == 0:
        print "You entered zero. This will not change the size of the object"
    elif scale_index <0:
        print "You are making the object smaller"
    elif scale_index >0:
        print "You are enlarging the object"
    else:
        print "Number is not comparable to ints, may be a string"
"""
"""
    my_file = open(tri_file, "r+")
    vertice_count = my_file.readline()

    print "vertice count: %s" %vertice_count
    print int(vertice_count)+1

    my_file.close
"""
# added a comment
