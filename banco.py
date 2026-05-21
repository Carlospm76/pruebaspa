# 1. Definir la excepción personalizada
class InsufficientFunds(Exception):
    """Excepción lanzada cuando el saldo es insuficiente."""
    pass

class CuentaBancaria:
    # 1. Método constructor que recibe el saldo inicial
    def __init__(self, saldo=0):
        self.saldo = saldo

    # 2. Método depositar que valida que el monto no sea menor o igual a 0
    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("Monto positivo")
        self.saldo += monto
        

    # 3. Método retirar que valida que el monto no supere el saldo disponible
    def retirar(self, monto):
        if monto > self.saldo:
            raise InsufficientFunds(f"Intento de retiro: {monto}. Saldo disponible: {self.saldo}")
        self.saldo -= monto
