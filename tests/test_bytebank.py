import pytest
from codigo.bytebank import Funcionario
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'  # Given-Contexto
        esperado = 23
        funcionario_teste = Funcionario('Teste', entrada, 1000)

        resultado = funcionario_teste.idade()  # When-Ação

        assert resultado == esperado  # Then-Desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = 'Lucas Carvalho'  # Given
        esperado = 'Carvalho'
        lucas = Funcionario(entrada, '11/11/2000', 1000)

        resultado = lucas.sobrenome()  # When

        assert resultado == esperado  # Then

    # @mark.skip
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # Given
        entrada_nome = 'Fulvio Taroni'
        esperado = 90000
        funcionario_teste = Funcionario(entrada_nome, '23/12/1997', entrada_salario)

        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario  # When

        assert resultado == esperado  # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000  # Given
        esperado = 100
        funcionario_teste = Funcionario('Teste', '23/12/1997', entrada_salario)

        resultado = funcionario_teste.calcular_bonus()  # When

        assert resultado == esperado  # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_excecao(self):
        with pytest.raises(Exception):
            entrada_salario = 100000  # Given
            funcionario_teste = Funcionario('Teste', '23/12/1997', entrada_salario)

            resultado = funcionario_teste.calcular_bonus()  # When

            assert resultado  # Then
