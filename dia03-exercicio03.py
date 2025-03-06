# EXERCÍCIOS E-BOOK
# MENTE LÓGICA - DIA 03
# 3) OFERTA ESPECIAL
# Uma loja oferece um desconto se o cliente comprar mais de 10 itens
# ou se o valor total da compra for superior a R$100.

# Dados:
# ● Quantidade de itens: 8
# ● Valor total: R$120
# Verificar se o cliente tem direito ao desconto.

print('\n=====================================')
print('3) OFERTA ESPECIAL - MINHA RESPOSTA')
print('=====================================\n')

cond_quantidade_itens = 10
cond_valor_total = 100

in_quantidade_itens = 8
in_valor_total = 120

proc_itens = in_quantidade_itens >= cond_quantidade_itens
proc_valor = in_valor_total >= cond_valor_total
proc_desconto = proc_itens or proc_valor

out_mensagem = 'Desconto Indisponível para o Cliente'

if proc_desconto:
  out_mensagem = 'Desconto Disponível para o Cliente'

print(out_mensagem)
