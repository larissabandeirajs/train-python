#Uma pessoa vai até a padaria todos os dias. A distância de sua casa até o estabelecimento é de 100 metros e todo percurso é feito em 20 segundos.

# Para calcular a velocidade média e descobrir a razão do espaço pelo  tempo, podemos dividir o espaço percorrido pelo tempo.

# Sabendo disso, a pessoa deseja criar uma função chamada velocidade, que recebe 2 parâmetros chamados espaco e tempo, realizar o cálculo e exibir uma saída semelhante ao exemplo 
# Velocidade: 5 m/s

def velocidade(espaco, tempo):
 v = espaco / tempo
 print(f'Velocidade: {v} m/s')
 velocidade(100, 20)

