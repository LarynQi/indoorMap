from openlocationcode import *

#def encode(latitude, longitude, codeLength=PAIR_CODE_LENGTH_):

loc1 = openlocationcode.encode(37.427755, -122.174244, 11)
loc2 = openlocationcode.encode(37.427769, -122.174249, 11)
print(loc1)
print(loc2)