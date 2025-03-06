# EXERCÍCIOS E-BOOK
# MENTE LÓGICA - DIA 04
# 5) CLIMA E ROUPA
# Situação: Você olha pela janela para ver o clima e decide o que vestir.
# Análise:
# ● O programa verifica a variável clima.
# ● Dependendo do valor, ele sugere o que vestir.
# ● Se o clima não corresponder a nenhuma condição, ele sugere verificar a previsão.

print('\n=====================================')
print('5) CLIMA E ROUPA - MINHA RESPOSTA')
print('=====================================\n')

in_clima = input('Informe qual o clima para sugerirmos uma roupa: \n').upper()

proc_clima = (in_clima != 'ENSOLARADO') and (in_clima != 'CHUVOSO') and (in_clima != 'NUBLADO')
proc_ensolarado = in_clima == 'ENSOLARADO'
proc_chuvoso = in_clima == 'CHUVOSO'

out_clima = in_clima.capitalize()

if proc_clima:
  out_mensagem = 'OPÇÃO INVÁLIDA! Escolha entre ensolarado, chuvoso ou nublado.'
else:
  if proc_ensolarado:
    out_sugestao = 'Regata e Short'
  elif proc_chuvoso:
    out_sugestao = 'Camisa e Calça'
  else:
    out_sugestao = 'Camiseta e Bermuda'
  out_mensagem = f'CLIMA: {out_clima} | SUGESTÃO: {out_sugestao}'

print(out_mensagem)
