#!/usr/bin/env python3

import sys
import numpy as np

xyz = []
# Try and get the input files
try:
	infilename = sys.argv[1]; outfilename = sys.argv[2]
except:
	print( "Usage:", sys.argv[0], "infile outfile"); sys.exit(1)

ifile = open( infilename, 'r') # Open the file
ofile = open( outfilename, 'w') # write the file
#Grab xyz for atom
def point( n ):
	return np.array([xyz[n][1], xyz[n][2], xyz[n][3]])
#Distance between atoms
def dist( pt1, pt2 ):
	return np.linalg.norm(pt1-pt2)

def dot_product(vec1, vec2):
	return vec1[0]*vec2[0] + vec1[1]*vec2[1] + vec1[2]*vec2[2]

def vector(pt1, pt2):
	return [pt1[0]-pt2[0],pt1[1]-pt2[1],pt1[2]-pt2[2]]

#obtain angle between 3 atoms
def angle_3_pts( pt1, pt2, pt3 ):
	v_1Norm = dist( pt1, pt2 )
	v_2Norm = dist( pt1, pt3 )
	v_1 = vector( pt1, pt2 )
	v_2 = vector( pt1, pt3 )
	return 180*np.arccos(np.dot(v_1,v_2)/(v_1Norm*v_2Norm))/np.pi

i = 0 # Lines in input
# Parse input file
for line in ifile:
	inAt = line.split() # Split the line [ atom, x, y, z ]
	at = inAt[ 0 ]
	x = float(inAt[ 1 ])
	y = float(inAt[ 2 ])
	z = float(inAt[ 3 ])
	atom = [at, x, y, z]
	xyz.append(atom)
	i += 1
# Cycle through first atom
j = 0
while j < i:
	point1 = point(j) # Atom j is at this xyz coord
	k = 0 # Cycle through second atom
	while k < i:
		if k == j: # Ignore same atom
			pass
		else:
			point2 = point(k) # Atom k is at xyz coord
			v = dist(point1,point2) # Distance between two points
			#Write distance out to file
			ofile.write(xyz[j][0] + "_" + str(j+1) + " is " + '%.3f'%(v) + 
				" distance from " + xyz[k][0] + "_" + str(k+1) + "\n")
		k += 1
	ofile.write("\n")
	k = 0 # Now looking for angles
	while k < i:
		if k == j:
			pass
		else:
			point2 = point(k)
			l = 0
			while l < i:
				if l == k: # Cycle if same
					pass
				elif l == j: # Cycle if same
					pass
				else:
					point3 = point(l)
					angle = angle_3_pts(point1, point2, point3)
					ofile.write(" ∠ " + xyz[k][0] + "_" + str(k+1) + " " + xyz[j][0] + 
						"_" + str(j+1) + " " + xyz[l][0] + "_" + str(l+1) + " " + 
						'%.3f'%(angle) + "\n") # Print angle between 3 atoms
				l += 1
		k += 1
	ofile.write("\n")
	j += 1
ifile.close(); ofile.close()

