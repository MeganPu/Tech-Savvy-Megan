import math
def quadratic(a,b,c):
    """solves quadratic equations of the form
        aX^2+bX+c, inputs a,b,c, where a, b and c are real numbers 
        and a ≠ 0
        works for all roots(real or complex)"""
    root=b**2-4*a*c
    if root <0:
        root=abs(complex(root))
        j=complex(0,1)
        x1=(-b+j+math.sqrt(root))/2*a
        x2=(-b-j+math.sqrt(root))/2*a
        return x1,x2
    else:
        x1=(-b+math.sqrt(root))/2*a
        x2=(-b-math.sqrt(root))/2*a
        return x1,x2
#example
print(quadratic(1,0,4))
