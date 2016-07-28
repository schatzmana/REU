# Command line: python, scale_dimension_multiply.py, scale percentage float, object tri file, and int num of object

# Functionality:
# Takes object tri file and scales it to float user sends in as "scale percentage" (puts this in newfile)
# then stacks the objects num times, and puts that into a new file named to describe the num and scale of object (see "filename" variable below)
# then makes rob file with that new .tri file as the link for the grasped object bounding box.

# Limitations:
# currently only centers object correctly on hand for cubes, but not other shapes....
# need to add that capability for other shapes

# Note: need to have the Part1.txt, Part2.txt, and Part3.txt all in the Python folder as well for making the .rob file
# This file meant to be run from Klampt/Python when objects are in ../data/objects/.

import sys

if len(sys.argv) != 4:
    print "Error: pass in script name, scale percentage, object tri file, num of shapes"

else:
    """ initializes all the variables and creates file names"""
    scale_index = float(sys.argv[1])
    tri_file = sys.argv[2]
    num = int(sys.argv[3])

    trifile = open(tri_file, "r+")
    newfile = open("../data/objects/newfile.tri", "w+")     # intermediate file created which will hold scaled values of .tri file (not stacked yet, just 1)
    vert_count = int( trifile.readline() ) # number of vertices
    newfile.write(str(vert_count)+"\n")

    # makes filename that tells num of and scale of new shape, so you can find the new .tri file in data/objects folder easily
    prefix_len = len('../data/objects/')
    tri_len = len(tri_file)
    shape = tri_file[ prefix_len:(tri_len-4)] # i.e. "cube.tri"
    filename = '../data/objects/' + str(num) + "of_" + str(scale_index) + shape +".tri"
    # ^ filename of new .tri file with scaling + multipling (Stacking) done

    # makes .rob filename : .rob file with ^ filename as the link for the grasped object
    rob_filename = "../data/robots/" + str(num) + "of_" + str(scale_index) + shape +".rob"
    geom_link_filename = '../objects/' + str(num) + "of_" + str(scale_index) + shape + '.tri'   # the filename that goes in the geometry links line of .rob



    """ change_size """
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
        # scaling:
        vertices[vert][0] = float( vertices[vert][0] ) * scale_index
        vertices[vert][1] = float( vertices[vert][1] ) * scale_index
        vertices[vert][2] = float( vertices[vert][2] ) * scale_index

        x = vertices[vert][0]
        y = vertices[vert][1]
        z = vertices[vert][2]

        str_xyz = str(x) +" " + str(y) + " " + str(z)
        newfile.write(str_xyz + "\n")
        #print str_xyz

    tri_count = int( trifile.readline() )
    newfile.write(str(tri_count)+"\n")

    triangles = []  # same concept as vertices[] above
    # read line by line of triangle coords (verts) & write them
    for each in range(0, tri_count):
        tri_coord = trifile.readline().strip('\n')
        triangles.append( tri_coord.split() )

    for vert in range( len(triangles) ):
        a = int( triangles[vert][0] )
        b = int( triangles[vert][1] )
        c = int( triangles[vert][2] )

        str_abc = str(a) +" " + str(b) + " " + str(c)
        newfile.write(str_abc + "\n")



    """ finds dimensions """
    # finds height, width, and depth of object by comparing all x, y, z values to find min and max of each
    # useful because gets height so you can stack

    infinit = float('inf')
    neginf = -1*infinit

    maxX = neginf
    maxY = neginf
    maxZ = neginf
    minX = infinit
    minY = infinit
    minZ = infinit

    for each in range(0, vert_count):
        x = float(vertices[each][0])
        y = float(vertices[each][1])
        z = float(vertices[each][2])

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

    height = maxY-minY
    width = maxX-minX
    depth = maxZ-minZ

    print "height: %s, width: %s, depth: %s" %(height, width, depth)



    """ multiply (stacks) """
    # require command line to include num shapes
    writefile = open(filename, "w")     # writing the final .tri file (scaled, stacked and all)
    newfile.seek(0) # need to start back reading file at beginning, cause already at end from writing
    writefile.write( str( num * vert_count )+"\n" ) # accounts for stacking

    count = 0   # index for stacking

    # writes scaled coordinates
    for each in range(0, vert_count):
        x = float(vertices[each][0])
        y = float(vertices[each][1])
        z = float(vertices[each][2])
        str_xyz = str(x) +" " + str(y) + " " + str(z)
        writefile.write(str_xyz + "\n")
    count += 1
    #print "count is: " + str(count)
    # end of read and write for the first go through

    # now need to read through again and add vals for next stack
    """ for loop to add vertices and triangles num times """
    while count < num:
        for vert in range(len(vertices)):
            x = float( vertices[vert][0] )
            y = float( vertices[vert][1] )
            z = float( vertices[vert][2] )

            # adding additional height, only edits 1/3 coords (only y), but could edit them all here
            y += ( height * count)

            str_xyz = str(x) +" " + str(y) + " " + str(z)
            writefile.write(str_xyz + "\n")
        count += 1
        #print "count is: " + str(count)

    writefile.write(str(tri_count * num)+"\n")


    #stores them so can use later without rereading and adjusting seek()
    # read line by line of triangle coords (verts) & write them
    """ writes original triangle coords """
    count = 0
    for each in range( len(triangles) ):
        a = int( triangles[each][0] )
        b = int( triangles[each][1] )
        c = int( triangles[each][2] )

        str_abc = str(a) +" " + str(b) + " " + str(c)
        writefile.write(str_abc + "\n")
    count += 1

    """ Repeat ^ to adjust vertices by object's height """
    while count < num:
        for each in range( len(triangles) ):
            a = int( triangles[each][0] )
            b = int( triangles[each][1] )
            c = int( triangles[each][2] )

            # to make new triangles correspond to the correct vertices from the originals
            # need to just add on total count to the previous on each iter through
            a += (vert_count * count)
            b += (vert_count * count)
            c += (vert_count * count)

            str_abc = str(a) +" " + str(b) + " " + str(c)
            writefile.write(str_abc + "\n")
        count += 1


    """ write new .rob file with above constructed filename """
    # ADD FUNCTIONALITY FOR CENTERING OBJECTS ON HAND FOR OTHER OBJECTS HERE
    # only knows how to center with cubes that are NOT STACKED (num =1) thus far...
    if tri_file == "../data/objects/cube.tri": #may need to switch this later to allow access from different directories
        j = float(scale_index) * -0.5
        k = float(scale_index) * -0.5
        l = -(float(scale_index) + 0.11)
    else: #temporary, change this later!! Just a default for all shapes other than cubes
        j = 0
        k = 0
        l = 0

    # makes the .rob
    rob_newfile = open(rob_filename, "w")
    robtext = open("./Part1.txt", 'r')
    rob_newfile.write( robtext.read() )

    robtext2 = open("./Part2.txt", 'r')
    jkl = str(j)+" "+str(k)+" "+str(l)+"\n"
    last_tv = "1 0 0 0 1 0 0 0 1 "+jkl  # last translational vector (aka for the additional link, the grasped object)
    rob_newfile.write( last_tv )
    rob_newfile.write( robtext2.read() +"\n")

    robtext3 = open("./Part3.txt", 'r')
    links = str('geometry	"jaco/jaco_link_base.tri" "jaco/jaco_link_1.tri" "jaco/jaco_link_2.tri" "jaco/jaco_link_3.tri" "jaco/jaco_link_4.tri" "jaco/jaco_link_5.tri" "jaco/jaco_link_hand.tri" "jaco/jaco_link_finger_1.tri" "jaco/jaco_link_finger_2.tri" "jaco/jaco_link_finger_3.tri" ')+'"'+ geom_link_filename + '"'
    rob_newfile.write( links + "\n")
    rob_newfile.write( robtext3.read() )
