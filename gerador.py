import random

nove_digitos_cpf = ''

for digitos in range(9):
    nove_digitos_cpf += str(random.randint(0, 9))
cpf = nove_digitos_cpf
print(cpf)


