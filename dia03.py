# EXERCÍCIOS E-BOOK

# 1) CALCULAR TROCO
# Você foi a uma padaria e comprou alguns itens:
# ● Pão: R$ 3.50
# ● Leite: R$ 4.20
# ● Café: R$2.80
# Você pagou com uma nota de R$ 20.
# Calcule quanto de troco você deve receber.

preco_pao = 3.50
preco_leite = 4.20
preco_cafe = 2.80
valor_compra = preco_pao + preco_leite + preco_cafe
cliente_pagamento = 20.00
is_compra_sem_troco = valor_compra == cliente_pagamento
is_compra_com_troco = cliente_pagamento - valor_compra

if is_compra_sem_troco:
  print('Sem troco. Valor da Compra é de R$ 20,00')
else:
  print(f'TROCO: R$ {is_compra_com_troco:.2f}')


# 2) VERIFICAR APROVAÇÃO EM EXAME
# Para ser aprovado em um exame, um estudante precisa ter uma nota média
# maior ou igual a 7.0 e uma frequência maior ou igual a 75%.
# Dados:
# ● Nota Média: 8.5
# ● Frequência: 80%
# Verificar se o estudante foi aprovado.
cond_media_nota_default = 7.0
cond_media_frequencia_default = 0.75
in_media_nota_estudante = .5
in_media_frequencia_estudante = 0.80
cond_media_nota_aprovacao = in_media_nota_estudante >= cond_media_nota_default
cond_media_frequencia_aprovacao = in_media_frequencia_estudante >= cond_media_frequencia_default
cond_aprovacao = cond_media_nota_aprovacao and cond_media_frequencia_aprovacao

if cond_aprovacao:
  print('Estudante Aprovado')
else:
  print('Estudante Reprovado')

# 3) OFERTA ESPECIAL
# Uma loja oferece um desconto se o cliente comprar mais de 10 itens
# ou se o valor total da compra for superior a R$100.
# Dados:
# ● Quantidade de itens: 8
# ● Valor total: R$120
# Verificar se o cliente tem direito ao desconto.


# 4) SISTEMA DE ACESSO
# Para acessar uma área restrita, o usuário deve inserir
# a senha correta e não pode estar bloqueado.
# Dados:
# ● Senha inserida: "abcd1234"
# ● Senha correta: "abcd1234"
# ● Usuário bloqueado: False
# Verifique se o acesso deve ser concedido.


# 5) DIVISÃO DE CONTA
# Três amigos vão dividir igualmente uma conta de R$ 150.
# Verificar quanto cada um deve pagar e
# se a divisão é exata (sem centavos restantes).


# DESAFIOS EXTRAS

# 1) CLASSIFICAÇÃO ETÁRIA
# Verificar se uma pessoa pode assistir a um filme classificado como "maiores de 16 anos".
# Dados:
# ● Idade da pessoa: Pergunte ao usuário


# 2) CALCULADORA IMC
# O Índice de Massa Corporal (IMC) é calculado dividindo o peso (em kg) pela altura (em metros) elevada ao quadrado.
# Calcular o IMC e verificar se a pessoa está dentro do peso ideal (IMC entre 18.5 e 24.9).


# 3) PAR OU ÍMPAR
# Solicitar um número inteiro ao usuário e verifica se ele é par ou ímpar.
