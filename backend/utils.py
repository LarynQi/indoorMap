def getKey(val, dict):
    for key in dict.keys():
        if dict[key].equals(val):
            return key
    return None