# EXERCÍCIOS E-BOOK
# MENTE LÓGICA - DIA 04
# DESAFIO EXTRA
# 3) CALCULADORA DE TARIFA DE TÁXI
# Uma empresa de táxi cobra uma tarifa básica de R$4.00, mais R$0.25 por quilômetro rodado.
# Calcular o valor total da corrida com base na distância percorrida.

print('\n=====================================')
print('DESAFIO 3) CALCULADORA DE TARIFA DE TÁXI')
print('=====================================\n')

cond_tarifa_valor = 4.00
cond_km_valor = 0.25

in_km_percorridos_quantidade = int(input('Informe a quantidade de km percorridos: \n'))

proc_km_percorridos_valor = in_km_percorridos_quantidade * cond_km_valor

out_corrida_valor = cond_tarifa_valor + proc_km_percorridos_valor

out_mensagem = 'Informe uma distância a partir de 1km para calcular o valor da corrida.'

if in_km_percorridos_quantidade >= 1:
  out_mensagem = f'Valor da Corrida: R$ {out_corrida_valor:.2f}'

print(out_mensagem)
