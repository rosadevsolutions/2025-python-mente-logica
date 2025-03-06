# EXERCÍCIOS E-BOOK

# 1) NÚMERO POSITIVO, NEGATIVO OU ZERO
# Solicitar um número ao usuário e verificar se é positivo, negativo ou zero.
print(f'\n=====================================')
print(f'1) NÚMERO POSITIVO, NEGATIVO OU ZERO - MINHA RESPOSTA\n')

in_numero_usuario = int(input("Informe um número: \n"))

proc_numero_negativo = in_numero_usuario < 0
proc_numero_positivo = in_numero_usuario > 0

out_mensagem = ''

if proc_numero_negativo:
  out_mensagem = 'negativo'
elif proc_numero_positivo:
  out_mensagem = 'positivo'
else:
  out_mensagem = 'igual a zero'

print(f'\n{in_numero_usuario} é um número {out_mensagem}.\n\n')

# 2) CALCULADORA SIMPLES
# Pedir ao usuário dois números e uma operação (+,-, *, /) e realizar o cálculo correspondente.
print(f'\n=====================================')
print(f'2) CALCULADORA SIMPLES - MINHA RESPOSTA\n')

in_numero_1 = int(input("Informe um número: \n"))
in_numero_2 = int(input("Informe outro número: \n"))
in_operacao = input("Informe a operação a ser realizada com os números: \n")
in_operacao = in_operacao.lower()

proc_calc_somar = in_numero_1 + in_numero_2
proc_calc_subtrair = in_numero_1 - in_numero_2
proc_calc_multiplicar = in_numero_1 * in_numero_2
proc_calc_dividir = in_numero_1 / in_numero_2

out_mensagem = ''

if in_operacao == "somar":
  out_mensagem = f'{in_numero_1} + {in_numero_2} = {proc_calc_somar}'
elif in_operacao == "subtrair":
  out_mensagem = f'{in_numero_1} - {in_numero_2} = {proc_calc_subtrair}'
elif in_operacao == "multiplicar":
  out_mensagem = f'{in_numero_1} x {in_numero_2} = {proc_calc_multiplicar}'
elif in_operacao == "dividir":
  out_mensagem = f'{in_numero_1} / {in_numero_2} = {proc_calc_dividir:.2f}'
else:
  out_mensagem = 'Informe uma operação válida'

print(out_mensagem)

# 3) CLASSIFICAÇÇÃO DE IDADE
# Criar um programa que classifica a idade de uma pessoa em:
# ● Criança: 0 a 12 anos
# ● Adolescente: 13 a 17 anos
# ● Adulto: 18 a 59 anos
# ● Idoso: 60 anos ou mais
print(f'\n=====================================')
print(f'3) CLASSIFICAÇÃO DE IDADE\n')

in_idade = int(input('Informe sua idade: '))

proc_idade_crianca = (in_idade >= 0) and (in_idade <= 12)
proc_idade_adolescente = (in_idade >= 13) and (in_idade <= 17)
proc_idade_adulto = (in_idade >= 18) and (in_idade <= 59)
proc_idade_idoso = (in_idade >= 60)

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

# 4) ANO BISSEXTO
# Verificar se um ano é bissexto.
# ● Um ano é bissexto se for divisível por 4.
# ● Não é bissexto se for divisível por 100, exceto se for divisível por 400.
print(f'\n=====================================')
print(f'4) ANO BISSEXTO\n')



# DESAFIOS EXTRAS

# 1) EMPRÉSTIMO BANCÁRIO
# Criar programa para analisar o pedido de empréstimo.
# O cliente deve informar o valor do empréstimo, renda mensal e número de parcelas.
# O empréstimo será aprovado se o valor da parcela não exceder 30% da renda mensal.
print(f'\n=====================================')
print(f'DESAFIO 1) EMPRÉSTIMO BANCÁRIO\n')

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

if(proc_cond_emprestimo_liberacao):
  out_emprestimo_status = 'EMPRÉSTIMO APROVADO.'
  out_comprometimento = f'Parcela compromete apenas {proc_emprestimo_parcela_proporcao_renda}% de sua renda mensal'

out_mensagem = f'\n{out_emprestimo_status}\n{out_comprometimento}'
print(out_mensagem)

# 2) PEDRA, PAPEL OU TESOURA
# Simular o jogo "Pedra, Papel ou Tesoura" entre o usuário e o computador.
print(f'\n=====================================')
print(f'DESAFIO 2) PEDRA, PAPEL OU TESOURA')

in_jogador1 = input('\nJogador 1 - Escolha o objeto desejado: \n').upper()
in_jogador2 = input('\nJogador 2 - Escolha o objeto desejado: \n').upper()

proc_vencedor1_pedra   = (in_jogador1 == 'pedra')   and (in_jogador2 == 'tesoura')
proc_vencedor1_papel   = (in_jogador1 == 'papel')   and (in_jogador2 == 'pedra')
proc_vencedor1_tesoura = (in_jogador1 == 'tesoura') and (in_jogador2 == 'papel')
proc_vencedor2_pedra   = (in_jogador1 == 'tesoura') and (in_jogador2 == 'pedra')
proc_vencedor2_papel   = (in_jogador1 == 'pedra')   and (in_jogador2 == 'papel')
proc_vencedor2_tesoura = (in_jogador1 == 'papel')   and (in_jogador2 == 'tesoura')

out_vencedor = ''
out_vencedor_objeto = ''
out_perdedor_objeto = ''

if proc_vencedor1_pedra:
  out_vencedor = 'Jogador 1'
  out_vencedor_objeto = "pedra"
  out_perdedor_objeto = "tesoura"
elif proc_vencedor1_papel:
  out_vencedor = 'Jogador 1'
  out_vencedor_objeto = "papel"
  out_perdedor_objeto = "pedra"
elif proc_vencedor1_tesoura:
  out_vencedor = 'Jogador 1'
  out_vencedor_objeto = "tesoura"
  out_perdedor_objeto = "papel"
elif proc_vencedor2_pedra:
  out_vencedor = 'Jogador 2'
  out_vencedor_objeto = "pedra"
  out_perdedor_objeto = "tesoura"
elif proc_vencedor2_papel:
  out_vencedor = 'Jogador 2'
  out_vencedor_objeto = "papel"
  out_perdedor_objeto = "pedra"
elif proc_vencedor2_tesoura:
  out_vencedor = 'Jogador 2'
  out_vencedor_objeto = "tesoura"
  out_perdedor_objeto = "papel"
else:
  out_mensagem_d2 = "EMPATE!"

out_mensagem_d2 = f'\nVENCEDOR: {out_vencedor} | {out_vencedor_objeto} ganha de {out_perdedor_objeto}'
print(out_mensagem_d2)




# 3) CALCULADORA DE TARIFA DE TÁXI
# Uma empresa de táxi cobra uma tarifa básica de R$4.00, mais R$0.25 por quilômetro rodado.
# Calcular o valor total da corrida com base na distância percorrida.
print(f'\n=====================================')
print(f'3) CALCULADORA DE TARIFA DE TÁXI\n')

cond_tarifa_valor = 4.00
cond_km_valor = 0.25

in_km_percorridos_quantidade = int(input('Informe a quantidade de km percorridos: \n'))

proc_km_percorridos_valor = in_km_percorridos_quantidade * cond_km_valor

out_corrida_valor = cond_tarifa_valor + proc_km_percorridos_valor

out_mensagem_d3 = f'Valor da Corrida: R$ {out_corrida_valor:.2f}'
print(out_mensagem_d3)
