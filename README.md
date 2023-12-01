# PYfunc_analysis
Interpolate a series of 3D function to fit best to one 2D function 

Assume having a series of 3D f(x,y) functions that imitate the behavior of a system, and you don't know which one is the best.
![image](https://github.com/WitoldSurowka/PYfunc_analysis/assets/115739312/283862ea-0c4c-41c4-8f5b-b84083b26662)

The data collected on the real system is only 2D function (for a certain y=3). 
![image](https://github.com/WitoldSurowka/PYfunc_analysis/assets/115739312/11397723-494f-4190-a053-3ca3632f6566)

The goal is to take the 3D function slice (2D blue function) and scale that function with 'a', to gain best fit to the real data (2D red function), so
a*(2D blue function) gives lowest descripancy with real-data based 2D red function.

It's achievable with curve fitting tool from scipy.optimize package. 




