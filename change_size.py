    # scale_index = float by which to multiply all nums by to scale an object
    # scale_index = +/- percentage by which to multiple all dimensional nums
    # i.e. change_size(2) = make object 2^n as big (cube 2*3)
    # change_size(.5) = half the nums

import sys

if len(sys.argv) != 3:
    print "Error: pass in script name, scale percentage, object tri file"

else:
    scale_index = sys.argv[1]
    tri_file = sys.argv[2]

    if scale_index == 0:
        print "You entered zero. This will not change the size of the object"
    elif scale_index <0:
        print "You are making the object smaller"
    elif scale_index >0:
        print "You are enlarging the object"
    else:
        print "Number is not comparable to ints, may be a string"

"""
    my_file = open(tri_file, "r+")
    vertice_count = my_file.readline()

    print "vertice count: %s" %vertice_count
    print int(vertice_count)+1

    my_file.close
"""
