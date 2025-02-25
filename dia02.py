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


# DESAFIOS

# 1) CONVERSOR DE TEMPERATURAS
# Criar um programa que converta uma temperatura de graus Celsius para Fahrenheit.
# Fórmula: F = C * 9/5 + 32

# 2) ÁREA DE UM CÍRCULO
# Criar um programa que calcule a área de um círculo com base no raio fornecido pelo usuário.
# Fórmula: Área = π * raio²
# π = 3.14159
