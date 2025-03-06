# EXERCÍCIOS E-BOOK
# MENTE LÓGICA - DIA 04
# DESAFIO EXTRA
# 1) EMPRÉSTIMO BANCÁRIO
# Criar programa para analisar o pedido de empréstimo.
# O cliente deve informar o valor do empréstimo, renda mensal e número de parcelas.
# O empréstimo será aprovado se o valor da parcela não exceder 30% da renda mensal.

print('\n=====================================')
print('DESAFIO 1) EMPRÉSTIMO BANCÁRIO - MINHA RESPOSTA\n')
print('=====================================\n')

in_emprestimo_valor = float(input('Valor do empréstimo desejado: \n'))
in_renda_mensal = float(input('\nSua renda mensal: \n'))
in_emprestimo_parcelas = float(input('\nQuantidade de parcelas desejadas: \n'))

in_emprestimo_valor = in_emprestimo_valor
in_renda_mensal = in_renda_mensal

proc_emprestimo_parcela_valor = in_emprestimo_valor / in_emprestimo_parcelas
proc_emprestimo_parcela_proporcao_renda = (proc_emprestimo_parcela_valor / in_renda_mensal) * 100
proc_cond_emprestimo_liberacao = proc_emprestimo_parcela_proporcao_renda <= 30

out_emprestimo_status = 'EMPRÉSTIMO NEGADO.'
out_comprometimento = f'Parcela compromete {proc_emprestimo_parcela_proporcao_renda}% de sua renda mensal.'

if proc_cond_emprestimo_liberacao:
  out_emprestimo_status = 'EMPRÉSTIMO APROVADO.'
  out_comprometimento = f'Parcela compromete apenas {proc_emprestimo_parcela_proporcao_renda}% de sua renda mensal'

out_mensagem = f'\n{out_emprestimo_status}\n{out_comprometimento}'
print(out_mensagem)
