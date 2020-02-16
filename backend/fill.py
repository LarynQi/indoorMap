from openlocationcode import openlocationcode as olc

#def encode(latitude, longitude, codeLength=PAIR_CODE_LENGTH_):

loc1 = olc.encode(37.4281906, -122.1741650, 13)
loc2 = olc.encode(37.4281714, -122.1741952, 13)
print(loc1)
print(loc2)