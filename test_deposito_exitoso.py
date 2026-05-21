import pytest 
from banco import CuentaBancaria, InsufficientFunds 

def test_deposito_exitoso(): 
    # Arrange 
    cuenta = CuentaBancaria(100) 
    # Act 
    cuenta.depositar(50) 
    # Assert 
    assert cuenta.saldo == 150 

def test_retiro_sin_fondos(): 
    cuenta = CuentaBancaria(50) 
    with pytest.raises(InsufficientFunds, match="Intento de retiro: 100. Saldo disponible: 50"): 
        cuenta.retirar(100) 