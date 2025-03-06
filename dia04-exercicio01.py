# EXERCÍCIOS E-BOOK
# MENTE LÓGICA - DIA 04
# 1) NÚMERO POSITIVO, NEGATIVO OU ZERO
# Solicitar um número ao usuário e verificar se é positivo, negativo ou zero.

print('\n=====================================')
print('1) NÚMERO POSITIVO, NEGATIVO OU ZERO - MINHA RESPOSTA')
print('=====================================\n')

in_numero_usuario = int(input('INFORME UM NÚMERO: \n'))

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
