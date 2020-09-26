import re
import matplotlib.pyplot as plt
import sys

POINTS = 100 # 100 points to plot
spl = re.compile('[\-\+]')
coe = re.compile("(\d*)(x)\^*(\d*)")

def find_coeff_expo(axn) :
    # axn is Cx^n
    c , x , n = (coe.findall(axn))[0]
    coeff = 1
    expo = 1
    if c != '' :
        coeff = int (c)
    if n != '' :
        expo = int (n)
    return coeff , expo

 
def plot_for_xrange(poly_arr,xrange):
    
    arr = re.split("[\s\,]+",xrange)
    arr.append(POINTS) # if user did not provide, this becomes 3 rd element
    start, end , pts = float(arr[0]), float(arr[1] ), float(arr[2])

    if end <= start or pts < 0 :
        sys.exit("wrong range.. start must be less than end and steps must be +ve")

    if  end - start > pts : # the user entered steps instead of points
        step = pts
    else :
        step = ( end - start ) / pts


    x_vals = []
    fx_y_vals = []

    x = start
    while (x <= end) :
        x_vals.append(x)
        val = 0
        for coeff,expo in poly_arr :
            val += coeff * ( x ** expo)   
        fx_y_vals.append(val)

        x += step

    return x_vals,fx_y_vals

def create_coeff_exponenet_array (polynomial) :

    signs = spl.findall(polynomial)  
    vals = spl.split(polynomial)

    if vals[0] == '' or vals[0] == None or vals[0].isspace() :
        vals.pop(0)
    else :
        signs.insert(0,'+')

    poly_arr = []
    for i in range(len(signs)):
        v = vals[i]
        #print (signs[i], v)
        members = []
        sign = 1
        if signs[i] == '-' : # if + leave it as 1
            sign = -1
        
        coeff = 0
        exponent = 0

        if v.find('x') == -1 : # constant
            coeff = int(v) 
            exponent = 0 # coefficient of x^0 is v
        else :
            coeff, exponent = find_coeff_expo(vals[i])

        poly_arr.append((sign * coeff, exponent ))
    
    return poly_arr
    


polynomial = (input('enter the equation (ax^n+bx+c) : ')).strip()
if polynomial :
    poly_arr = create_coeff_exponenet_array(polynomial)

xrange = 'dummy'
while xrange :
        xrange = input('enter new range (m,n , steps/points) : ')
        Xi, Yi = plot_for_xrange(poly_arr,xrange)
        #print(Xi,"\n", Yi)
        plt.plot(Xi, Yi)
        print("successfully plotted")
        plt.show() 
        
