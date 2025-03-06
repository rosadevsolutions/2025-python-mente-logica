# EXERCÍCIOS E-BOOK
# MENTE LÓGICA - DIA 04
# DESAFIO EXTRA
# 2) CALCULADORA SIMPLES
# Pedir ao usuário dois números e uma operação (+,-, *, /) e realizar o cálculo correspondente.

print('\n=====================================')
print('DESAFIO 2) CALCULADORA SIMPLES - MINHA RESPOSTA')
print('=====================================\n')

in_numero_1 = int(input('Informe um número: \n'))
in_numero_2 = int(input('Informe outro número: \n'))
in_operacao = input('Informe a operação a ser realizada com os números: \n').lower()

proc_calc_somar       = in_numero_1 + in_numero_2
proc_calc_subtrair    = in_numero_1 - in_numero_2
proc_calc_multiplicar = in_numero_1 * in_numero_2
proc_calc_dividir     = in_numero_1 / in_numero_2

out_mensagem = ''

if in_operacao   == 'somar':
  out_mensagem = f'{in_numero_1} + {in_numero_2} = {proc_calc_somar}'
elif in_operacao == 'subtrair':
  out_mensagem = f'{in_numero_1} - {in_numero_2} = {proc_calc_subtrair}'
elif in_operacao == 'multiplicar':
  out_mensagem = f'{in_numero_1} x {in_numero_2} = {proc_calc_multiplicar}'
elif in_operacao == 'dividir':
  out_mensagem = f'{in_numero_1} / {in_numero_2} = {proc_calc_dividir:.2f}'
else:
  out_mensagem = 'Informe uma operação válida'

print(out_mensagem)
