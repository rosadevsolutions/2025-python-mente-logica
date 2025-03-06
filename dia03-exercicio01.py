# EXERCÍCIOS E-BOOK
# EXERCÍCIOS E-BOOK
# MENTE LÓGICA - DIA 04
# 1) CALCULAR TROCO
# Você foi a uma padaria e comprou alguns itens:
# ● Pão: R$ 3.50
# ● Leite: R$ 4.20
# ● Café: R$2.80
# Você pagou com uma nota de R$ 20.
# Calcule quanto de troco você deve receber.

print('\n=====================================')
print('1) CALCULAR TROCO - MINHA RESPOSTA')
print('=====================================\n')

cond_preco_pao = 3.50
cond_preco_leite = 4.20
cond_preco_cafe = 2.80

in_cliente_compra = cond_preco_pao + cond_preco_leite + cond_preco_cafe
in_cliente_pagamento = 20.00

proc_compra_sem_troco = in_cliente_compra == in_cliente_pagamento
proc_compra_com_troco = in_cliente_compra - in_cliente_pagamento

out_mensagem = f'Sem troco. Valor da Compra é de R${in_cliente_pagamento:.2f}'

if (not proc_compra_sem_troco):
  out_mensagem = f'TROCO: R${proc_compra_com_troco:.2f}'

print(out_mensagem)
