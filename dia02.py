# EXERCÍCIO 01 - DECLARANDO VARIAVÉIS
# Criar um programa que declare as seguintes variáveis:
# nome: seu nome.
# idade: sua idade.
# altura: sua altura.
# estudante:se você é estudante ou não (true/false).
in_nome = "Romulo"
in_idade = 45
in_altura = 1.89
in_estudante = True

# EXERCÍCIO 02 - EXIBINDO INFORMAÇÕES
# Utilizar a função print() para exibir as informações das variáveis criadas no exercício anterior.
print(f'NOME: {in_nome}')
print(f'IDADE: {in_idade}')
print(f'ALTURA: {in_altura}')
print(f'ESTUDANTE: {in_estudante}')

# EXERCÍCIO 03 - OPERAÇÕES SIMPLES print(f'NOME: {in_nome}')
# Calcular o ano de nascimento com base na idade (considerando que o ano atual é 2025).
# Verificar se a pessoa é maior de idade (idade >= 18) e armazenar o resultado numa variável booleana.
ano_atual = 2025
ano_nascimento = ano_atual - in_idade
print(f'ANO DE NASCIMENTO: {ano_nascimento}')

# EXERCÍCIO 04 - MANIPULAÇÃO DE STRINGS
# Criar uma variável frase que contenha a mensagem: "Olá, meu nome é [seu nome] e eu tenho [sua idade] anos."
# DICA: Usar str(idade) para converter o número inteiro em string antes de concatenar.
mensagem = f'Olá, meu nome é {in_nome} e eu tenho {in_idade} anos.'
print(mensagem)

# EXERCÍCIO 05 - CALCULADORA SIMPLES
# Pedir ao usuário para inserir dois números e armazenar em variáveis.
# Calcular a soma, subtração, multiplicação e divisão desses números.
# Exibir os resultados.
# OBS: A função input() permite que o usuário insira dados.
# Usamos float() para converter a entrada em um número de ponto flutuante.
in_num1 = float(input('Informe um número: '))
in_num2 = float(input('Informe outro número: '))

out_soma = in_num1 + in_num2
out_subtracao = in_num1 - in_num2
out_multiplicacao = in_num1 * in_num2
out_divisao = in_num1 / in_num2

print(f'SOMA: {out_soma}')
print(f'SUBTRAÇÃO: {out_subtracao}')
print(f'MULTIPLICAÇÃO: {out_multiplicacao}')
print(f'DIVISÃO: {out_divisao}')


# DESAFIOS

# 1) CONVERSOR DE TEMPERATURAS
# Criar um programa que converta uma temperatura de graus Celsius para Fahrenheit.
# Fórmula: F = C * 9/5 + 32
in_temperatura_celsius = float(input('Informe uma temperaura em Celsius: '))
out_conversao_fahrenheit = in_temperatura_celsius * 1.8 + 32
print(f'{in_temperatura_celsius}°C equivalem a {out_conversao_fahrenheit}°F.')


# 2) ÁREA DE UM CÍRCULO
# Criar um programa que calcule a área de um círculo com base no raio fornecido pelo usuário.
# Fórmula: Área = π * raio²
# π = 3.14159
in_circulo_raio = float(input('Informe uma medida de raio para o círculo: '))
in_pi = 3.14159
out_circulo_area = in_pi * (in_circulo_raio * in_circulo_raio)
print(f'Á área de um círculo de raio de {in_circulo_raio} é de {out_circulo_area}.')
