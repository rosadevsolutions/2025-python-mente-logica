# EXERCÍCIOS E-BOOK

# 1) CALCULAR TROCO
# Você foi a uma padaria e comprou alguns itens:
# ● Pão: R$ 3.50
# ● Leite: R$ 4.20
# ● Café: R$2.80
# Você pagou com uma nota de R$ 20.
# Calcule quanto de troco você deve receber.
print(f'=====================================')
print(f'1) CALCULAR TROCO - MINHA RESPOSTA')

cond_preco_pao = 3.50
cond_preco_leite = 4.20
cond_preco_cafe = 2.80

in_valor_compra = cond_preco_pao + cond_preco_leite + cond_preco_cafe
in_cliente_pagamento = 20.00

ver_compra_sem_troco = in_valor_compra == in_cliente_pagamento
calc_compra_com_troco = in_cliente_pagamento - in_valor_compra

out_mensagem = f'Sem troco. Valor da Compra é de R${in_cliente_pagamento:.2f}'

if (not ver_compra_sem_troco):
  out_mensagem = f'TROCO: R${calc_compra_com_troco:.2f}'

print(out_mensagem)


# 2) VERIFICAR APROVAÇÃO EM EXAME
# Para ser aprovado em um exame, um estudante precisa ter uma nota média
# maior ou igual a 7.0 e uma frequência maior ou igual a 75%.
# Dados:
# ● Nota Média: 8.5
# ● Frequência: 80%
# Verificar se o estudante foi aprovado.
print(f'=====================================')
print(f'2) VERIFICAR APROVAÇÃO EM EXAME - MINHA RESPOSTA')

cond_media_nota = 7.0
cond_media_frequencia = 0.75

in_media_nota_estudante = 8.5
in_media_frequencia_estudante = 0.80

ver_media = in_media_nota_estudante >= cond_media_nota
ver_frequencia = in_media_frequencia_estudante >= cond_media_frequencia
ver_aprovacao  = ver_media and ver_frequencia

out_mensagem = 'Estudante Reprovado'

if ver_aprovacao:
  out_mensagem = 'Estudante Aprovado'

print(out_mensagem)

# 3) OFERTA ESPECIAL
# Uma loja oferece um desconto se o cliente comprar mais de 10 itens
# ou se o valor total da compra for superior a R$100.
# Dados:
# ● Quantidade de itens: 8
# ● Valor total: R$120
# Verificar se o cliente tem direito ao desconto.
print(f'=====================================')
print(f'3) OFERTA ESPECIAL - MINHA RESPOSTA')

cond_quantidade_itens = 10
cond_valor_total = 100

in_quantidade_itens = 8
in_valor_total = 120

ver_itens = in_quantidade_itens >= cond_quantidade_itens
ver_valor = in_valor_total >= cond_valor_total
ver_desconto = ver_itens or ver_valor

out_mensagem = 'Desconto Indisponível para o Cliente'

if ver_desconto:
  out_mensagem = 'Desconto Disponível para o Cliente'

print(out_mensagem)

# 4) SISTEMA DE ACESSO
# Para acessar uma área restrita, o usuário deve inserir
# a senha correta e não pode estar bloqueado.
# Dados:
# ● Senha inserida: "abcd1234"
# ● Senha correta: "abcd1234"
# ● Usuário bloqueado: False
# Verifique se o acesso deve ser concedido.
print(f'=====================================')
print(f'4) SISTEMA DE ACESSO - MINHA RESPOSTA')

in_senha_usuario = "abcd12345"
def_senha_sistema = "abcd1235"
check_senha = in_senha_usuario == def_senha_sistema
check_acesso = False
out_acesso = check_senha == True and check_acesso == False
out_mensagem = "Acesso Bloqueado"

if(out_acesso):
  out_mensagem = "Acesso Liberado"

print(f'{out_mensagem}')



# 5) DIVISÃO DE CONTA
# Três amigos vão dividir igualmente uma conta de R$ 150.
# Verificar quanto cada um deve pagar e
# se a divisão é exata (sem centavos restantes).
print(f'=====================================')
print(f'5) DIVISÃO DE CONTA - MINHA RESPOSTA')

in_clientes = 2
in_valor_total = 120
calc_valor_individual = in_valor_total / in_clientes
out_divisao_exata = in_valor_total % in_clientes
out_mensagem = f'Divisão não é exata! Cada pessoa vai pagar aproximadamente R${calc_valor_individual:.2f}'

if (out_divisao_exata == 0):
  out_mensagem =  f'Divisão exata. Cada pessoa vai pagar R${calc_valor_individual:.2f}'

print(out_mensagem)


# DESAFIOS EXTRAS

# 1) CLASSIFICAÇÃO ETÁRIA
# Verificar se uma pessoa pode assistir a um filme classificado como "maiores de 16 anos".
# Dados:
# ● Idade da pessoa: Pergunte ao usuário
print(f'=====================================')
print(f'DESAFIO 1) CLASSIFICAÇÃO ETÁRIA - MINHA RESPOSTA')

cond_faixa_etaria = 16

in_faixa_etaria_user = int(input('Informe sua idade: \n'))

ver_faixa_etaria = in_faixa_etaria_user >= cond_faixa_etaria

out_status = '\nPERMITIDO.'

if(not ver_faixa_etaria):
  out_status = '\nNÃO PERMITIDO.'

out_faixa_etaria = f'\nFaixa Etária do Filme: {cond_faixa_etaria} anos. \nIdade do Cliente: {in_faixa_etaria_user} anos.\n'
out_mensagem = out_status + out_faixa_etaria
print(out_mensagem)

# 2) CALCULADORA IMC
# O Índice de Massa Corporal (IMC) é calculado dividindo o peso (em kg) pela altura (em metros) elevada ao quadrado.
# Calcular o IMC e verificar se a pessoa está dentro do peso ideal (IMC entre 18.5 e 24.9).
print(f'=====================================')
print(f'DESAFIO 2) CALCULADORA IMC')

in_peso = int(input('Informe seu peso: \n'))
in_altura = float(input('\nInforme sua altura: \n'))
proc_imc = in_peso / (in_altura**2)

proc_imc_ideal = (proc_imc >= 18.5) and (proc_imc <= 24.9)

out_status = '\nPARABÉNS!!! IMC DENTRO DA FAIXA DE PESO IDEAL.'

if(not proc_imc_ideal):
  out_status = '\nALERTA!!! IMC FORA DA FAIXA DE PESO IDEAL.'

out_valor = f'\nSEU IMC: {proc_imc:.1f} \nIMC - PESO IDEAL: Entre 18.5 e 24.9\n'

out_mensagem = out_status + out_valor
print(out_mensagem)

# 3) PAR OU ÍMPAR
# Solicitar um número inteiro ao usuário e verifica se ele é par ou ímpar.
print('=====================================')
print('3) PAR OU ÍMPAR')

in_numero = int(input('\nInforme um número: \n'))
proc_numero_par = (in_numero % 2) == 0
out_mensagem = '\nNÚMERO PAR\n'

if(not proc_numero_par):
  out_mensagem = '\nNÚMERO ÍMPAR\n'

print(out_mensagem)
