class CuentaBancaria:
    # atributo de clase
    saldo = 0
    account_balance = 0
    general_cuentas = []

    def __init__(self, tasa_int, account_balance):
        # atributos de instancia
        self.tasa_int = tasa_int
        self.account_balance = account_balance
        CuentaBancaria.general_cuentas.append(self)

    # Métodos
    # Métodos de Instancia
    def deposito(self, saldo):
        self.account_balance += saldo
        return self

    def retiro(self, saldo):
        if self.account_balance >= saldo:
            self.account_balance -= saldo
        else:
            print(
                f"Fondos insuficientes: cobrando una tarifa de $5")
            self.account_balance -= 5
        return self

    def generar_interes(self):
        if self.account_balance > 0:
            self.account_balance += self.account_balance * self.tasa_int
        return self

    def transferir_dinero(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.mostrar_info_cuenta()
        user.mostrar_info_cuenta()
        return self

    def mostrar_info_cuenta(self):
        return f"{self.account_balance}"

    # Metodos de clase
    @classmethod
    def mostrar_cuentas(cls):
        for cuenta in cls.general_cuentas:
            cuenta.mostrar_info_cuenta()


class User:
    def __init__(self, name):
        self.name = name
        self.balance = {
            "checking": CuentaBancaria(.01, 0),
            "savings": CuentaBancaria(.02, 0)
        }

    def generar_balance(self):
        print(
            f"Usuario: {self.name}, Cuenta: Checking Balance: {self.balance['checking'].mostrar_info_cuenta()}")
        print(
            f"Usuario: {self.name}, Cuenta: Savings Balance: {self.balance['savings'].mostrar_info_cuenta()}")
        return self


cristina = User("Cristina")

cristina.balance["checking"].deposito(1000).deposito(20).deposito(
    40).retiro(600).generar_interes().mostrar_info_cuenta()
cristina.balance["savings"].deposito(1000).deposito(20).deposito(
    40).retiro(600).generar_interes().mostrar_info_cuenta()


cristina.generar_balance()
