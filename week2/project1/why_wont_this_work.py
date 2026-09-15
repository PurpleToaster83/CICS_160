#Name: William Van Uitert

def my_quadratic(a,b,c):
    # y1 = -b + √(b^2 - 4ac) / 2a
    # y2 = -b - √(b^2 - 4ac) / 2a
    # on error: print out error, and return warning values
    try:
        plus = ((-1*b)+((b*b-4*a*c))**(0.5))/(2*a)
        minus = (-b-((b**2-4*a*c))**(.5))/(2*a)
    except (ValueError, ZeroDivisionError) as e:
        print(e, "- Function is not Quadratic")
        print("Divided by zero")
        plus = None
        minus = None
    return plus,minus

#####################################
if __name__ == '__main__':
    ## MY TESTS ##
    ## TEST 1: ##
    #y = x^2 + 8x + 16
    #should be: y1 = -8, y2 = -8
    y1,y2 = my_quadratic(1,8,16)
    print(y1,y2)

    ## TEST 2: ##
    #y = x^2 + 10x + 2
    #should ~ be: y1 = -5.2041..., y2 = -14.7958... 
    y1,y2 = my_quadratic(1,10,2)
    print(y1,y2)

    ## TEST 3: ##
    #y = x^2
    #should be: y1 = 0.0, y2 = 0.0 
    y1,y2 = my_quadratic(1,0,0)
    print(y1,y2)

    ## TEST 4: ##
    #y = x^2 + 4
    #give two imaginary values
    y1,y2 = my_quadratic(1,0,4)
    print(y1,y2)