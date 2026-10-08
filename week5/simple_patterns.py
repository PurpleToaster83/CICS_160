def mapping_filtering(coll):
    to_return = []
    for st in coll:
        if len(str) % 2 == 0 and st[0] in 'aeiouAEIOU': # filter - only changes some of collection
            to_return.append(str.upper()) # upper() function is the map
    return to_return

def other_mf(coll):
    return [st.upper() for st in coll if len(st)%2==0 and st[0] in 'aeiou'] # a comprehension of mapping & filtering

def reduce(c_s):
    # new_s = ""
    if(len(c_s)):
        new_s = type(c_s[0])() # makes an empty string too
        for s in c_s:
            new_s += s # accumulation of compponents
        return new_s
    return None

def zipper(col1, col2):
    new_c = []
    mn = min(len(col1), len(col2))
    for i in range(mn): # same length
        new_c.append((col1[i], col2[i]))
    # new_c.extend(col1[mn:])
    for i in range(mn, len(col1)): # collection 1 is longer
        new_c.append(col1[i])
    # new_c.extend(col2[mn:])
    for i in range(mn, len(col2)): # collection 2 is longer
        new_c.append(col2[i])
    return new_c