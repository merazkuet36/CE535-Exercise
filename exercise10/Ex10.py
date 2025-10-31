
def simpson_rule (fx, a:float, b:float, n:int, *args, **kwargs):
    '''
    simpson_rule(fx, a=float, b=float, n=int, *args, **kwargs) 
    a is a float lower limit integration 
    b ia a float upper limit integration 
    n ia an integer number of subintervals
    '''
    # input checks
    #define and internal function 
    
    
    # input check
    if not isinstance(a, float) or not isinstance(b, float):
        return 0.0
    if b <= a:
        return 0.0
    if not isinstance(n, int) or n <= 0 or n % 2 != 0:
        return 0.0

    #compute deltax
    dx = (b - a) / n
    Sum = 0.0
    #loop through n+1
    for i in range(n + 1):
        x= a + i * dx
        fxi = fx(x, *args, **kwargs)
        

        # factors for function
        if i == 0 or i == n:
            factor = 1.0
        elif i % 2 == 1:
            factor= 4.0
        else:
            factor = 2.0

        Sum += factor * fxi

    Sn = Sum * dx / 3.0
    return Sn 