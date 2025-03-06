# EXERCÍCIOS E-BOOK
# MENTE LÓGICA - DIA 04
# 6) SEMÁFORO
# Situação: Ao dirigir, você reage de acordo com a cor do semáforo
# Análise:
# ● O programa verifica a cor do semáforo.
# ● Executa a ação correspondente a cada cor.
# ● Se encontrar um sinal desconhecido, alerta o motorista.

print('\n=====================================')
print('6) SEMÁFORO - MINHA RESPOSTA')
print('=====================================\n')

in_sinal = input('Informe a cor do semáforo: \n').upper()

cond_amarelo = in_sinal == 'AMARELO'
cond_verde = in_sinal == 'VERDE'
cond_vermelho = in_sinal == 'VERMELHO'
cond_sinal_invalido = (not cond_amarelo) and (not cond_verde) and (not cond_vermelho)

out_sinal = in_sinal.capitalize()
out_status = ''
out_mensagem = ''

if cond_sinal_invalido:
  out_mensagem = 'COR INVÁLIDA. Escolha entre verde, vermelho ou amarelo.'
else:
  if cond_amarelo:
    out_status = 'ATENÇÃO! O motorista pode passar, mas precisa dar preferência ao pedestre.'
  elif cond_vermelho:
    out_status = 'PARE! O sinal está fechado para o motorista.'
  else:
    out_status = 'PASSE! O sinal está aberto para o motorista.'

  out_mensagem = f'\nSinal {out_sinal} | {out_status}'

print(out_mensagem)
