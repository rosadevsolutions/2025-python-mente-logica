# EXERCÍCIOS E-BOOK
# MENTE LÓGICA - DIA 03
# DESAFIO EXTRA
# 3) PAR OU ÍMPAR
# Solicitar um número inteiro ao usuário e verifica se ele é par ou ímpar.

print('\n=====================================')
print('DESAFIO 3) PAR OU ÍMPAR - MINHA RESPOSTA')
print('=====================================\n')

in_numero = int(input('\nInforme um número: \n'))

proc_numero_par = (in_numero % 2) == 0

out_mensagem = '\nNÚMERO PAR\n'

if(not proc_numero_par):
  out_mensagem = '\nNÚMERO ÍMPAR\n'

print(out_mensagem)
