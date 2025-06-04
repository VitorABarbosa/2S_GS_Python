from funcoes import *

'''

3. Dado o dicionário abaixo com dados simulados de precipitação por cidade, escreva
um código que percorra o dicionário e imprima apenas as cidades com risco alto:

'''

chuvas = {
 "Mumbai": 120,
 "Delhi": 45,
 "Chennai": 80,
 "Kolkata": 130,
 "Jaipur": 30
}

print(identificar_cidades_risco_alto_dict(chuvas))
