# EXERCÍCIOS E-BOOK
# MENTE LÓGICA - DIA 03
# 4) SISTEMA DE ACESSO
# Para acessar uma área restrita, o usuário deve inserir
# a senha correta e não pode estar bloqueado.

# Dados:
# ● Senha inserida: "abcd1234"
# ● Senha correta: "abcd1234"
# ● Usuário bloqueado: False
# Verifique se o acesso deve ser concedido.

print('\n=====================================')
print('4) SISTEMA DE ACESSO - MINHA RESPOSTA')
print('=====================================\n')

cond_senha_sistema = 'abcd12345'

in_senha_usuario = 'abcd12345'

proc_senha = in_senha_usuario == cond_senha_sistema
proc_acesso = False

out_acesso = (proc_senha == True) and (proc_acesso == False)
out_mensagem = 'Bloqueado'

if out_acesso:
  out_mensagem = 'Liberado'

print(f'Acesso {out_mensagem}')
