# EXERCÍCIOS E-BOOK
# MENTE LÓGICA - DIA 03
# 1) CLASSIFICAÇÃO ETÁRIA
# Verificar se uma pessoa pode assistir a um filme classificado como "maiores de 16 anos".
# Dados:
# ● Idade da pessoa: Pergunte ao usuário

print('\n=====================================')
print('DESAFIO 1) CLASSIFICAÇÃO ETÁRIA - MINHA RESPOSTA')
print('=====================================\n')

cond_faixa_etaria = 16

in_faixa_etaria_user = int(input('Informe sua idade: \n'))

proc_faixa_etaria = in_faixa_etaria_user >= cond_faixa_etaria

out_status = '\nPERMITIDO.'

if(not proc_faixa_etaria):
  out_status = '\nNÃO PERMITIDO.'

out_faixa_etaria = f'\nIdade do Cliente: {in_faixa_etaria_user} anos. \nFaixa Etária do Filme: {cond_faixa_etaria} anos'
out_mensagem = out_status + out_faixa_etaria
print(out_mensagem)
