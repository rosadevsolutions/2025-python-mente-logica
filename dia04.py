# EXERCÍCIOS E-BOOK

# 1) NÚMERO POSITIVO, NEGATIVO OU ZERO
# Solicitar um número ao usuário e verificar se é positivo, negativo ou zero.
print(f'\n=====================================')
print(f'1) NÚMERO POSITIVO, NEGATIVO OU ZERO - MINHA RESPOSTA\n')

in_numero_usuario = int(input("Informe um número: \n"))

proc_numero_negativo = in_numero_usuario < 0
proc_numero_positivo = in_numero_usuario > 0

out_mensagem = ''

if proc_numero_negativo:
  out_mensagem = 'negativo'
elif proc_numero_positivo:
  out_mensagem = 'positivo'
else:
  out_mensagem = 'igual a zero'

print(f'\n{in_numero_usuario} é um número {out_mensagem}.\n\n')

# 2) CALCULADORA SIMPLES
# Pedir ao usuário dois números e uma operação (+,-, *, /) e realizar o cálculo correspondente.
print(f'\n=====================================')
print(f'2) CALCULADORA SIMPLES - MINHA RESPOSTA\n')

in_numero_1 = int(input("Informe um número: \n"))
in_numero_2 = int(input("Informe outro número: \n"))
in_operacao = input("Informe a operação a ser realizada com os números: \n")
in_operacao = in_operacao.lower()

proc_calc_somar = in_numero_1 + in_numero_2
proc_calc_subtrair = in_numero_1 - in_numero_2
proc_calc_multiplicar = in_numero_1 * in_numero_2
proc_calc_dividir = in_numero_1 / in_numero_2

out_mensagem = ''

if in_operacao == "somar":
  out_mensagem = f'{in_numero_1} + {in_numero_2} = {proc_calc_somar}'
elif in_operacao == "subtrair":
  out_mensagem = f'{in_numero_1} - {in_numero_2} = {proc_calc_subtrair}'
elif in_operacao == "multiplicar":
  out_mensagem = f'{in_numero_1} x {in_numero_2} = {proc_calc_multiplicar}'
elif in_operacao == "dividir":
  out_mensagem = f'{in_numero_1} / {in_numero_2} = {proc_calc_dividir:.2f}'
else:
  out_mensagem = 'Informe uma operação válida'

print(out_mensagem)

# 3) CLASSIFICAÇÇÃO DE IDADE
# Criar um programa que classifica a idade de uma pessoa em:
# ● Criança: 0 a 12 anos
# ● Adolescente: 13 a 17 anos
# ● Adulto: 18 a 59 anos
# ● Idoso: 60 anos ou mais

# 4) ANO BISSEXTO
# Verificar se um ano é bissexto.
# ● Um ano é bissexto se for divisível por 4.
# ● Não é bissexto se for divisível por 100, exceto se for divisível por 400.

# 5) CAIXA ELETRÔNICO
# O usuário deve informar o valor do saque (apenas valores inteiros)
# O programa deve informar quantas cédulas de cada valor serão fornecidas.
# Considere cédulas de R$100, R$50, R$20, R$10, R$5 e R$2.

# DESAFIOS EXTRAS

# 1) EMPRÉSTIMO BANCÁRIO
# Criar programa para analisar o pedido de empréstimo.
# O cliente deve informar o valor do empréstimo, renda mensal e número de parcelas.
# O empréstimo será aprovado se o valor da parcela não exceder 30% da renda mensal.

# 2) PEDRA, PAPEL OU TESOURA
# Simular o jogo "Pedra, Papel ou Tesoura" entre o usuário e o computador.

# 3) CALCULADORA DE TARIFA DE TÁXI
# Uma empresa de táxi cobra uma tarifa básica de R$4.00, mais R$0.25 por quilômetro rodado.
# Calcular o valor total da corrida com base na distância percorrida.
