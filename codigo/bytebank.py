from datetime import datetime


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    def idade(self):
        data_nascimento = datetime.strptime(self._data_nascimento, '%d/%m/%Y')
        ano_atual = datetime.today()
        return ano_atual.year - data_nascimento.year

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salário é muito alto pra receber um bônus.')
        return valor

    def sobrenome(self):
        nome_completo = self.nome.strip()
        last_name = nome_completo.split(' ')[-1]
        return last_name

    def _eh_socio(self):
        sobrenomes = ['Taroni', 'Wayne', 'Muto', 'Kaiba', 'Ptolomeu']
        return self.sobrenome() in sobrenomes and self.salario >= 100000

    def decrescimo_salario(self):
        if self._eh_socio():
            self.salario = self.salario - (self.salario * 0.1)

    def __str__(self):
        return f'Funcionario({self.nome}, {self._data_nascimento}, {self._salario})'
