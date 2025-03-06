# EXERCÍCIOS E-BOOK
# MENTE LÓGICA - DIA 03
# DESAFIO EXTRA
# 2) CALCULADORA IMC
# O Índice de Massa Corporal (IMC) é calculado dividindo o peso (em kg) pela altura (em metros) elevada ao quadrado.
# Calcular o IMC e verificar se a pessoa está dentro do peso ideal (IMC entre 18.5 e 24.9).

print('\n=====================================')
print('DESAFIO 2) CALCULADORA IMC')
print('=====================================\n')

in_peso = int(input('INFORME PESO: \n'))
in_altura = float(input('\nINFORME ALTURA: \n'))

proc_imc = in_peso / (in_altura**2)
proc_imc_ideal = (proc_imc >= 18.5) and (proc_imc <= 24.9)

out_status = '\nPARABÉNS!!! IMC ESTÁ DENTRO DA FAIXA DE PESO IDEAL.'

if(not proc_imc_ideal):
  out_status = '\nALERTA!!! IMC ESTÁ FORA DA FAIXA DE PESO IDEAL.'

out_valor = f'\nSEU IMC: {proc_imc:.1f} \nIMC - PESO IDEAL: Entre 18.5 e 24.9\n'

out_mensagem = out_status + out_valor
print(out_mensagem)
