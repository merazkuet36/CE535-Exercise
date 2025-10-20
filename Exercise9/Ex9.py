import math

def simpson_rule(fx, a=1.0, b=2.0, n=20, *args, **kwargs):
    """
    Simpson's Rule for numerical integration.
    
    Approximates the integral of the function `fx` over the interval [a, b] using Simpson's Rule.
    
    Arguments:
    fx : function
        The function to be integrated.
    a  : float, (d=1.0)
        The lower bound of the integration interval.
    b  : float, (d=2.0)
        The upper bound of the integration interval.
    n  : int, (d=20)
        The number of subdivisions. 
    *args, **kwargs : arbitrary arguments
        Additional arguments passed to the function `fx`.
    
    Returns:
    float
        The approximate value of the integral.
    """
    
    # Validate inputs
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return 0.0  # If a or b are not numbers, return 0.0
    if b <= a:
        return 0.0  # If b is not greater than a, return 0.0
    if n <= 0 or n % 2 != 0:
        return 0.0  # If n is not positive or is not even, return 0.0

    # Calculate h (step size)
    h = (b - a) / n
    
    # Initialize result with the function values at the endpoints
    result = fx(a, *args, **kwargs) + fx(b, *args, **kwargs)

    # Add terms with factor 4 for odd indices
    for i in range(1, n, 2):
        result += 4 * fx(a + i * h, *args, **kwargs)

    # Add terms with factor 2 for even indices
    for i in range(2, n, 2):
        result += 2 * fx(a + i * h, *args, **kwargs)

    # Multiply by h/3 to get the final result
    result *= h / 3
    
    return result
