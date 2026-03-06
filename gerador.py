import random

nove_digitos_cpf = ''

for digitos in range(9):
    nove_digitos_cpf += str(random.randint(0, 9))
cpf = nove_digitos_cpf
print(cpf, '-> 9 primeiro digitos')

cpf_nove_digitos = cpf[:9] 

contagem_10 = 10
resultado = 0

for digito_1 in cpf_nove_digitos:
    resultado += int(digito_1 ) * contagem_10 
    contagem_10 -= 1

digito_1 = (resultado * 10) % 11
digito_1 = digito_1  if digito_1 <= 9 else 0



cpf_dez_digitos = cpf_nove_digitos + str(digito_1)

contagem_11 = 11
resultado_2 = 0

for digito_2 in cpf_dez_digitos:
    resultado_2 += int(digito_2) * contagem_11
    contagem_11 -= 1

digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerador_final = f"{nove_digitos_cpf}{digito_1}{digito_2} -> CPF COMPLET"

print(cpf_gerador_final)

