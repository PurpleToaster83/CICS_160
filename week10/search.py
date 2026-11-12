def search(lis, target):
    for i in range(len(lis)):
        if(lis[i] == target):
            return i
    return -1