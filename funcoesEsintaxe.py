def verificarcao_se_pode_dirigir_conversao_de_string_para_inteiro():
  idadee = input('Qual sua idade: ')
  idadee = int(idadee)
  if idadee < 18:
     print('Não tem permissão')
  else:
    print("Tem permissão")

verificarcao_se_pode_dirigir_conversao_de_string_para_inteiro()