# Gerador de CPF válido em Python

Gera um CPF aleatório com dígitos verificadores calculados seguindo o algoritmo oficial da Receita Federal.

## Como funciona

1. Gera 9 dígitos aleatórios
2. Calcula o **10º dígito** verificador usando soma ponderada (pesos de 10 a 2) e aplicando `(soma × 10) % 11`
3. Calcula o **11º dígito** verificador usando a mesma lógica com pesos de 11 a 2
4. Se o resultado for maior que 9, o dígito passa a ser `0`

## Como usar

```bash
python cpf_gerador.py
```

### Saída esperada

```
3829104756 -> 9 primeiro digitos
38291047560 9 -> CPF COMPLET
```

## Requisitos

- Python 3.x
- Biblioteca `random` (nativa, sem instalação necessária)
