import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import linspace

# Load the coefficient data matrix
A = np.loadtxt('poly_coeffs.txt', delimiter=',')

#  Define real data
RV= [0.8957, 0.8996, 0.9175, 0.9232]
Rx = [0, 23, 40, 60]
y = 3

#Function1 transform 3D model to 2D model for certain y=3. Scale it with 'a' to fit real data best and return the fitted parameters and error.
def fitting (An,RV,y):
    # Load the coefficient vector
    p00, p10, p01, p20, p11, p02, p30, p21, p12, p03, p31, p22, p13, p04, p32, p23, p14, p05=An

    # Function2 - given polynomial model of 3D function
    def function_model(x,a):
        #define 3D function, scaled by 'a'
        fpp= (a*(p00 + p10*x + p01*y + p20*x**2 + p11*x*y + p02*y**2 + p30*x**3 + p21*x**2*y
                    + p12*x*y**2 + p03*y**3 + p31*x**3*y + p22*x**2*y**2 + p13*x*y**3
                    + p04*y**4 + p32*x**3*y**2 + p23*x**2*y**3 + p14*x*y**4 +
                     p05*y**5))
        # return it
        return fpp

    # perform fitting of scaled function fpp to the real-data 2D function, x, f(x) (return 'a')
    param, _ = curve_fit(function_model, Rx, RV)


    a_fit = param
    fpp=function_model

    PercErr=round(max(100*abs(function_model(np.array(Rx),a_fit)-RV)/RV), ndigits=2)
    return a_fit,fpp, PercErr




plt.plot(Rx, RV, c='r',label=f'Real data')

#Create densit space of arguments
x2 = linspace(0, 60, 601)
#prepare lists to memorize all the scalars 'a' and functions fpp
an=[]
fppn=[]

#   Consequently pass all the coefficient vectors to the 'Function1'.
#   plot the fitted data, and save 'a' as well as 'PercErr' for every instance.
for i in range (1,7):
    #current coefficients vector
    An=A[i-1,:]
    #pass it to function1 'fitting'
    a,fpp,PercErr=fitting(An,RV,y)
    #round a
    a=round(a[0],ndigits=3)
    # save 'a' as well as 'PercErr'
    an.append(a)
    fppn.append(fpp)
    print(An,a, PercErr)
    #assign the values to the coefficients to be able to plot the function with prepared arguments 'x2'
    p00, p10, p01, p20, p11, p02, p30, p21, p12, p03, p31, p22, p13, p04, p32, p23, p14, p05 = An
    plt.plot(x2, fpp(x2,a), label=f'Fitted 2D silce of 3D model{i} a={a}, Max error={PercErr} %')


#save the plot and show it
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.savefig('fitting.png', dpi=300)
plt.show()

