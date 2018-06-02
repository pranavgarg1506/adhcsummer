#!/usr/bin/python3


import os,string
path = '/home/pranav/Desktop/'
#path = os.path.normpath(path)
res = []
for root,dirs,files in os.walk(path, topdown=True):
    depth = root[len(path) + len(os.path.sep):].count(os.path.sep)
    if depth == 0:	# 0 for the present directory 
        # We're currently two directories in, so all subdirs have depth 3
        res += [os.path.join(root, d) for d in dirs]
        dirs[:] = [] # Don't recurse any deeper

#for i in range(0,len(res)):
#	print(res[i])

print(len(res))
