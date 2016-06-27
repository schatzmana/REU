# command line : script name, object tri file, and a file to store dimensions into
import sys

if len(sys.argv) != 3:
    print "Error: pass in script name, object tri file, and new file name"

else:
    tri_file = sys.argv[1]
    trifile = open(tri_file, "r")
    newfile = open(sys.argv[2], "w") # will write to the file name that user passes in

    vert_count = int( trifile.readline() )
    vertices = []
    inf = float('inf')
    maxX = -1*inf
    maxY = -1*inf
    maxZ = -1*inf
    minX = inf
    minY = inf
    minZ = inf

    for each in range(0, vert_count):
        coordinate = trifile.readline().strip('\n')
        vertices.append( coordinate.split() )
         # appends coordinates to the vertices list, with all three coordinates in seperate nested lists
        #print "just before comparing the x val"

        if vertices[each][0] < minX:
            minX = vertices[each][0]
        elif vertices[each][0] > maxX:
            maxX = vertices[each][0]

        if vertices[each][1] < minY:
            minY = vertices[each][1]
        elif vertices[each][1] > maxY:
            maxY = vertices[each][1]


        if vertices[each][2] > maxZ:
            maxZ = vertices[each][2]
        elif vertices[each][2] < minZ:
            minZ = vertices[each][2]

    print "minX: %s, maxX: %s" %(minX, maxX)
    print "minY: %s, maxY: %s" %(minY, maxY)
    print "minZ: %s, maxZ: %s" %(minZ, maxZ)

# PROBLEM
#always picks 1 for max but 10 for min.....



'''
    for vert in range(len(vertices)):
            x = float( vertices[vert][0] )
            y = float( vertices[vert][1] )
            z = float( vertices[vert][2] )
'''
