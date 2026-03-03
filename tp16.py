def list_to_dict(L):
    d = {}             
    i = 0            

    for element in L:
        d[i] = element  
        i += 1         

    return d



L = [(1,2), (3,6), (9,0)]

print(list_to_dict(L))