import pytest
from ejercicio_3_auditoria_web.calculos import calcular_emisiones_carbono

def test_calculo_nominal_por_defecto():
    resultado= calcular_emisiones_carbono(100)
    assert resultado == 40.0
    
def test_calculo_con_otro_factor():
    resultado= calcular_emisiones_carbono(40, factor_emision=0.6)
    assert resultado == 24.0
    
def test_calculo_consumo_negativo():
    with pytest.raises(ValueError):
        calcular_emisiones_carbono(-10)
