# takes in scale percentage, object tri file, and num of shapes and will write to the newfile
# the scaled dimensions and compute the ehight, width, and depth of the new scaled object
# Also creates new file name that describes scale and num of shape

import sys

if len(sys.argv) != 4:
    print "Error: pass in script name, scale percentage, object tri file, num of shapes"

else:
    """ change_size """
    scale_index = float(sys.argv[1])
    # print "scale index= %s" %scale_index
    tri_file = sys.argv[2]
    print tri_file
    num = int(sys.argv[3])

    trifile = open(tri_file, "r+")
    newfile = open("../data/objects/newfile.tri", "w+")
    vert_count = int( trifile.readline() )
    newfile.write(str(vert_count)+"\n")
    #print "vertice count: %s" %vert_count

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
        # print "originals are: ", x, y, z

        # scaling:
        x *= scale_index
        y *= scale_index
        z *= scale_index
        # print "scaled coords are: ",x,y,z

        str_xyz = str(x) +" " + str(y) + " " + str(z)
        # print "string coords are: " + str_xyz +"\n"
        newfile.write(str_xyz + "\n")

    tri_count = int( trifile.readline() )
    newfile.write(str(tri_count)+"\n")
    # print "tri_count: %s" %tri_count

    # read line by line of triangle coords (verts) & write them
    for each in range(0, tri_count):
        tri_coord = trifile.readline()
        #print tri_coord
        newfile.write(tri_coord)
    # write out new values to file

    """ dimension finder """
    # get height
    infinit = float('inf')
    neginf = -1*infinit

    maxX = neginf
    maxY = neginf
    maxZ = neginf
    minX = infinit
    minY = infinit
    minZ = infinit

    newfile.seek(0) # need to start back reading file at beginning, cause already at end from writing
    new_vertices = []
    vert_count = int( newfile.readline().strip('\n') )
    for each in range(0, vert_count):
        vertex = newfile.readline().strip('\n')
        new_vertices.append( vertex.split() )

        x = float(new_vertices[each][0])
        y = float(new_vertices[each][1])
        z = float(new_vertices[each][2])

        if x < minX:
            minX = x
        if x > maxX:
            maxX = x

        if y < minY:
            minY = y
        if y > maxY:
            maxY = y

        if z < minZ:
            minZ = z
        if z > maxZ:
            maxZ = z

    #print "minX: %s, maxX: %s" %(minX, maxX)
    #print "minY: %s, maxY: %s" %(minY, maxY)
    #print "minZ: %s, maxZ: %s" %(minZ, maxZ)

    height = maxY-minY
    width = maxX-minX
    depth = maxZ-minZ

    print "height: %s, width: %s, depth: %s" %(height, width, depth)

    """ multiply """
    # take in num shapes

    # makes filename that tells num of and scale of new shape, so you can find the new .tri file
    prefix_len = len('../data/objects/')
    tri_len = len(tri_file)
    shape = tri_file[ prefix_len:tri_len] # i.e. "cube.tri"
    filename = str(num) + "of_" + str(scale_index) + shape
    print filename
