# EXERCÍCIOS E-BOOK
# MENTE LÓGICA - DIA 04
# 3) CLASSIFICAÇÇÃO DE IDADE
# Criar um programa que classifica a idade de uma pessoa em:
# ● Criança: 0 a 12 anos
# ● Adolescente: 13 a 17 anos
# ● Adulto: 18 a 59 anos
# ● Idoso: 60 anos ou mais

print(f'\n=====================================')
print(f'3) CLASSIFICAÇÃO DE IDADE')
print(f'=====================================\n')

in_idade = int(input('INFORME SUA IDADE: \n'))

proc_idade_crianca     = (in_idade >= 0) and (in_idade <= 12)
proc_idade_adolescente = (in_idade >= 13) and (in_idade <= 17)
proc_idade_adulto      = (in_idade >= 18) and (in_idade <= 59)
proc_idade_idoso       = (in_idade >= 60)

if proc_idade_crianca:
  out_classificacao = 'Criança'
elif proc_idade_adolescente:
  out_classificacao = 'Adolescente'
elif proc_idade_adulto:
  out_classificacao = 'Adulto'
elif proc_idade_idoso:
  out_classificacao = 'Idoso'
else:
  out_classificacao = 'Inválida'

out_mensagem = f'IDADE: {in_idade} | CLASSIFICAÇÃO: {out_classificacao}'
print(out_mensagem)
