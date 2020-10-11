import pytest
import doctest

def mysqrt(y):
    '''
    :param y: the value to take the square root of
    :return: the square root of y

    Example:
    >>> mysqrt(9)
    3.0

    The argument must be non-negative:
    >>> mysqrt(-1)
    Traceback (most recent call last):
    ...
    Value Error: mysqrt(): argument must be non-negative
    
    '''
    #docstring, sollte jede Python-Funktion haben
    if y < 0:
        raise ValueError("mysqrt(): argument must be non-negative.")
    x = y / 2           #nicht mehr floor division
    #in Python 2 war normale Division 'y/2' eine floor division,
    #wenn y vom Typ 'int' war.
    #in Python 3 liefert 'y/2' immer float, auch wenn y 'int' ist
    # => Fehlerquelle beseitigt, aber schwierige Portierung
    while abs(x**2 - y) > 1e-15*x**2:
        x = (x+y / x) / 2
    return x


def test_mysqrt():      #Alle Testfunktionen muessen mit test_ anfangen
    assert mysqrt(0) == 0
    with pytest.raises(ValueError):
        mysqrt(-1)
    assert mysqrt(9) == 3
    assert mysqrt(1) == 1
    assert mysqrt(4) == 2
    assert mysqrt(1.21) == pytest.approx(1.1)


#Ausfuehrung mit pytest
#man kann doctest mit pytest ausfuehren, indem man --doctest-modules beim Ausfuehren hinzufuegt
#erst den Test schreiben und dann die Funktion: test-driven development


