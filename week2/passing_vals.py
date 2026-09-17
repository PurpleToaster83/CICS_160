x = 4 # 4 is imutable
def hey(y):
    y = y+15 # makes y 19
    return y # y only exist in hey
hey(x)
print(x) # x is still 4

lis = [1, 2, 3] # list is mutable
def hey2(z):
    z.append(4)
    z[0] = 0
print(hey2(lis)) # prints none because no return
print(lis) # lis is changed