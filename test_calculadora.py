import pytest
from main import suma, resta, multiplicacion, division

@pytest.mark.criticos
@pytest.mark.parametrize("a,b,resultado", [
    (10,5,15),
    (-6,3,-3),
    (2,4,6)
])
def test_suma(a,b,resultado):
    assert suma(a,b) == resultado
    
def test_division_decimal():
    assert (10,3) == pytest.approx(3.3333, rel=1e-3)  
    
def test_division_cero():
    with pytest.raises(ZeroDivisionError):
        division(10,0) 
        
@pytest.mark.skip(reason="funcionalidad aun no implementada")
def test_resta():
    assert resta(2,3) == 5
    