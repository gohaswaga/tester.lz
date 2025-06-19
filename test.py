import math as m

def equalize(x):
    try:
        y = (m.sin(x)/(x - 2 * m.cos(x))) + (m.sqrt((2 * m.tan(x) - 1) / x))
    except ZeroDivisionError:
        result = "problem with (x - 2 * m.cos(x)) or x = 0"
    except ValueError:
        result = "pricol"
    except TypeError:
        result = "not number"
    else:
        result = y
    return(result)

