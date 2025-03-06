# EXERCÍCIOS E-BOOK
# MENTE LÓGICA - DIA 03
# 5) DIVISÃO DE CONTA
# Três amigos vão dividir igualmente uma conta de R$ 150.
# Verificar quanto cada um deve pagar e
# se a divisão é exata (sem centavos restantes).

print('\n=====================================')
print('5) DIVISÃO DE CONTA - MINHA RESPOSTA')
print('=====================================\n')

in_clientes = 3
in_valor_total = 150

proc_valor_individual = in_valor_total / in_clientes
proc_divisao_exata = (in_valor_total % in_clientes) == 0

out_mensagem = f'Divisão não é exata! Cada pessoa vai pagar aproximadamente R${proc_valor_individual:.2f}'

if proc_divisao_exata:
  out_mensagem =  f'Divisão exata. Cada pessoa vai pagar R${proc_valor_individual:.2f}'

print(out_mensagem)
