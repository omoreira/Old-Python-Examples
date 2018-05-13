#!/usr/bin/env python
#99 Bottles of Beer Example.
for b in range(99,0,-1):
	if b > 2:
		print str(b), " bottles of beer on the wall, ",str(b)," bottles of beer."
		print "Take one down and pass it around, "+ str(b-1)+ " bottles of beer on the wall!"
	if b == 2:
		print "2 bottles of beer on the wall, 2 bottles of beer."
		print "Take one down and pass it around, 1 bottle of beer on the wall!"
	if b == 1:
		print "1 bottle of beer on the wall, 1 bottle of beer."
		print "Take one down and pass it around, no more beer on the wall!"
