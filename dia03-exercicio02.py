# EXERCÍCIOS E-BOOK
# MENTE LÓGICA - DIA 03
# 2) VERIFICAR APROVAÇÃO EM EXAME
# Para ser aprovado em um exame, um estudante precisa ter uma nota média
# maior ou igual a 7.0 e uma frequência maior ou igual a 75%.
# Dados:
# ● Nota Média: 8.5
# ● Frequência: 80%
# Verificar se o estudante foi aprovado.

print('\n=====================================')
print('2) VERIFICAR APROVAÇÃO EM EXAME - MINHA RESPOSTA')
print('=====================================\n')

cond_media_nota_escola = 7.0
cond_media_frequencia_escola = 0.75

in_media_nota_estudante = 8.5
in_media_frequencia_estudante = 0.80

proc_media = in_media_nota_estudante >= cond_media_nota_escola
proc_frequencia = in_media_frequencia_estudante >= cond_media_frequencia_escola
proc_aprovacao  = proc_media and proc_frequencia

out_mensagem = 'Reprovado'

if proc_aprovacao:
  out_mensagem = 'Aprovado'

print(f'\nEstudante {out_mensagem}')
