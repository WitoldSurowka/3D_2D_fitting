# 3D-2D_fitting
Fit a series of 3D functions to match best to real-data 2D function 

Assume you have a series of 3D functions f(x,y), that mimic the behavior of a system, and you are unsure which one is the best. 
The collected data from the real system is in the form of a 2D function (for a certain y=3).
![image](https://github.com/WitoldSurowka/PYfunc_analysis/assets/115739312/283862ea-0c4c-41c4-8f5b-b84083b26662)

The data collected on the real system is only 2D red color function (for a certain y=3). 
![image](https://github.com/WitoldSurowka/PYfunc_analysis/assets/115739312/bdeac23a-89d2-4ed7-ba0a-79591e8bd490)

The goal is to take the 3D function slice (2D blue function) and scale that function, multiplying with 'a', to gain best fit to the real data (2D red function), so
a*(2D blue function) gives lowest descripancy with real-data based 2D red function. 

It's achievable with curve fitting tool from scipy.optimize package. 

Here's what to do:
The 3D function is given by an equation:

    p00 + p10*x + p01*y + p20*x^2 + p11*x*y + p02*y^2 + p30*x^3 + p21*x^2*y 
    + p12*x*y^2 + p03*y^3 + p31*x^3*y + p22*x^2*y^2 + p13*x*y^3 
    + p04*y^4 + p32*x^3*y^2 + p23*x^2*y^3 + p14*x*y^4 +p05*y^5
  
There are 6 models that differ by sets of polynominal coefficients:

        p00 = 0.9978; p10 = 9.456e-05; p01 = 0.0007055; p20 = 6.593e-06; p11 = -0.0002668; ...
        p00 = 0.9978; p10 = 9.522e-05; p01 = 0.0004516; p20 = 6.729e-06; p11 = -0.000257;...
        ...
All the above values are stored within the file 'poly_coeffs.txt'.


Let's write a pseudo-code of what the program should do:

      Load the coefficient data matrix
      Define real data
      
        Function1:
        Load the coefficient vector 
        
          Function2:
          a*(3D function) 
          return this function
          
        using scipy.optimize perform fitting of 2D function (that is actually a slice of 3D function, multiplied by scalar 'a') to the real-data 2D function (return 'a')
        calculate 'PercErr' - maximal percentage error between fitted function and real-data function
        return 'a', function, 'PercErr'
      
      Plot real-data function.
      create loop: 
        for all the models(using all the coefficient vectors), as input to the 'Function1'.
        every time, plot the fitted data, and describe 'a' and 'PercErr'.
      Show the plot.

Thanks to this script, you can make an informed decision in choosing the model that best fits the real data. 
As an alternative error estimator, the Root Mean Square Error (RMSE) calculation can also be implemented.

![image](https://github.com/WitoldSurowka/PYfunc_analysis/assets/115739312/980f3cad-bbd1-474d-9a51-253ac2de9be9)



  
  
  
  
  



