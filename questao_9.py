from funcoes import *

'''

9. Simule uma base simples contendo cidades e seus respectivos riscos (baixo, médio,
alto). Use uma lista de dicionários. Em seguida, filtre apenas as cidades com risco alto e
armazene em uma nova lista.

'''

cidades = [
    {"cidade": "São Paulo", "risco": "alto"},
    {"cidade": "Rio de Janeiro", "risco": "médio"},
    {"cidade": "Brasília", "risco": "baixo"},
    {"cidade": "Salvador", "risco": "alto"},
    {"cidade": "Fortaleza", "risco": "médio"}
]

cidades_filtradas = filtrar_cidades_por_risco(cidades)

for cidade in cidades_filtradas:
    print(f"Cidade: {cidade['cidade']} - Risco: {cidade['risco']}")
