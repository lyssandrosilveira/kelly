# Entrada dos dados
probabilidade = float(input("Digite a probabilidade de vitória em %: "))
odd = float(input("Digite a odd decimal: "))
stake = float(input("Digite o valor da sua stake: "))

# Cálculo do Critério Kelly
p = probabilidade / 100
q = 1 - p
b = odd - 1

kelly_fraction = (b * p - q) / b

# Verificação para evitar porcentagem negativa
if kelly_fraction < 0:
    kelly_fraction = 0

# Cálculo do valor em reais a ser apostado
valor_apostado = kelly_fraction * stake

# Saída do resultado
print("Porcentagem da stake a ser apostada: {:.2f}%".format(kelly_fraction * 100))
print("Valor em reais a ser apostado: R$ {:.2f}".format(valor_apostado))
