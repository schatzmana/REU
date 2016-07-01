# correctly compares x,y,z values and prints out min and max for each.
# Does not write dimensional info to a file.
# Can easily add that functionality if you just eliminate comments.
# prints height, width, and depth

import sys

if len(sys.argv) != 2:
    print "Error: pass in script name, object tri file" #, and new file name"

else:
    tri_file = sys.argv[1]
    trifile = open(tri_file, "r")
    # newfile = open(sys.argv[2], "w") # will write to the file name that user passes in

    vert_count = int( trifile.readline() )
    vertices = []
    infinit = float('inf')
    neginf = -1*infinit

    maxX = neginf
    maxY = neginf
    maxZ = neginf
    minX = infinit
    minY = infinit
    minZ = infinit

    for each in range(0, vert_count):
        coordinate = trifile.readline().strip('\n')
        vertices.append( coordinate.split() )

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

    print "minX: %s, maxX: %s" %(minX, maxX)
    print "minY: %s, maxY: %s" %(minY, maxY)
    print "minZ: %s, maxZ: %s" %(minZ, maxZ)

    height = maxY-minY
    width = maxX-minX
    depth = maxZ-minZ

    print "height: %s, width: %s, depth: %s" %(height, width, depth)

    """
    print infinit
    print neginf

    if 0 < infinit: #T
        print "0 is less than infinity"
    if 0 < neginf: #F
        print "0 is less than neg infinity"
    if 0 > neginf: #T
        print "0 is greater than neg infinity"

    if 100000 < infinit: #T
        print "100,000 is less than infinity"
    if 100000 > neginf: #T
        print "100,000 is greater than neg infinity"

    if -255 > neginf: #T
        print "-255 is greater than neg infinity"
    if -255 < neginf: #F
        print "-255 is less than neg infinity"
    if -255 > infinit: #F
        print "-255 is greater than infinity"

    print float(1.30538e-16)
    if float(1.30538e-16)<-2:
        print "compared a tiny negative exponential to a negative unsuccessfully"
    if float(1.30538e-16) < infinit:
        print "setting tiny exponential to min"
    """
