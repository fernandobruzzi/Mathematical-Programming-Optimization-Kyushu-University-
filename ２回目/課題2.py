import numpy as np

def answer():
    x=[8,11,13,10,15,19,17,20]
    y= [115,124,138,120,151,186,169,193]

    x = np.array(x)
    y = np.array(y)
    n= x.size

    b_1 = np.sum(y) - ((np.sum(x*y)*np.sum(x))/np.sum(x*x))
    b_2 = n - ((np.sum(x)*np.sum(x))/np.sum(x*x)) 
    b = b_1/b_2
    a = (np.sum(x*y)-b*np.sum(x))/np.sum(x*x)
    print(f"a = {round(a,3)}, and b ={round(b,3)}")
    return

answer()