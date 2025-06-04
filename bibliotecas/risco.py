# risco.py

"""
Módulo de Análise de Riscos Climáticos
=====================================

Este módulo contém funções especializadas na análise e classificação de riscos
relacionados a eventos climáticos extremos, especialmente chuvas e inundações.

Funções incluídas:
- verificar_risco_inundacao_por_chuva(): Verifica risco baseado em mm de chuva
- classificar_risco(): Classifica risco em baixo/médio/alto
- identificar_cidades_risco_alto_dict(): Identifica cidades em risco alto
- filtrar_cidades_por_risco(): Filtra cidades por nível de risco

Desenvolvido para: Global Solution - Computational Thinking with Python (2SEM2025)
"""

def verificar_risco_inundacao_por_chuva(milimetros_chuva: float) -> str:
    """
    Verifica o risco de inundação com base na previsão de chuva.
    Corresponde à Questão 1.

    Args:
        milimetros_chuva: A quantidade de chuva prevista em milímetros.

    Returns:
        Uma string indicando "ALERTA: Risco alto de inundação" se a chuva
        for maior que 100 mm, ou "Nível de risco normal" caso contrário.
    """
    if milimetros_chuva > 100: # 
        return "ALERTA: Risco alto de inundação" # 
    else:
        return "Nível de risco normal" # 

def classificar_risco(chuva: float) -> str:
    """
    Classifica o nível de risco com base na quantidade de chuva.
    Corresponde à Questão 2.

    Args:
        chuva: A quantidade de chuva em milímetros.

    Returns:
        Uma string indicando o nível de risco ("baixo", "médio" ou "alto").
        - "baixo" se for menor que 50 mm.
        - "médio" se estiver entre 50 mm e 100 mm (inclusive).
        - "alto" se for acima de 100 mm.
    """
    if chuva < 50:
        return "baixo"
    elif 50 <= chuva <= 100:
        return "médio"
    else:  # chuva > 100
        return "alto"

def identificar_cidades_risco_alto_dict(dados_chuvas: dict) -> list:
    """
    Identifica cidades com risco alto de inundação a partir de um dicionário de precipitação.
    Utiliza a função classificar_risco para determinar o nível de risco.
    Corresponde à Questão 3.

    Args:
        dados_chuvas: Um dicionário onde as chaves são nomes de cidades (str)
                      e os valores são a precipitação em mm (float ou int).
                      Exemplo: {"Mumbai": 120, "Delhi": 45}

    Returns:
        Uma lista contendo os nomes das cidades com risco "alto".
    """
    cidades_risco_alto = []
    for cidade, precipitacao in dados_chuvas.items():
        if classificar_risco(precipitacao) == "alto":
            cidades_risco_alto.append(cidade)
    return cidades_risco_alto

def filtrar_cidades_por_risco(lista_cidades_info: list, nivel_risco_desejado: str = "alto") -> list:
    """
    Filtra uma lista de dicionários de cidades para incluir apenas aquelas com um nível de risco específico.
    Corresponde à Questão 9. 

    Args:
        lista_cidades_info: Uma lista de dicionários, onde cada dicionário
                            contém informações da cidade, incluindo uma chave 'risco'.
                            Exemplo: [{'cidade': 'Mumbai', 'risco': 'alto'},
                                      {'cidade': 'Delhi', 'risco': 'baixo'}] 
        nivel_risco_desejado: O nível de risco para filtrar (padrão: "alto").

    Returns:
        Uma nova lista contendo apenas os dicionários das cidades que correspondem
        ao nível_risco_desejado.
    """
    cidades_filtradas = []
    for cidade_info in lista_cidades_info:
        if cidade_info.get('risco', '').lower() == nivel_risco_desejado.lower():
            cidades_filtradas.append(cidade_info)
    return cidades_filtradas

if __name__ == '__main__':
    # Exemplos de uso das funções de risco
    print("=== Testando Módulo de Risco ===")

    # Questão 1
    print("\nQ1: Verificar Risco por Chuva")
    print(f"Chuva de 120mm: {verificar_risco_inundacao_por_chuva(120)}")
    print(f"Chuva de 80mm: {verificar_risco_inundacao_por_chuva(80)}")

    # Questão 2
    print("\nQ2: Classificar Risco")
    print(f"Chuva de 30mm: Risco {classificar_risco(30)}")
    print(f"Chuva de 75mm: Risco {classificar_risco(75)}")
    print(f"Chuva de 150mm: Risco {classificar_risco(150)}")

    # Questão 3
    print("\nQ3: Identificar Cidades com Risco Alto (Dicionário)")
    chuvas_q3 = {
        "Mumbai": 120, "Delhi": 45, "Chennai": 80, "Kolkata": 130, "Jaipur": 30
    }
    print(f"Cidades com risco alto: {identificar_cidades_risco_alto_dict(chuvas_q3)}")

    # Questão 9
    print("\nQ9: Filtrar Cidades por Risco")
    dados_cidades_q9 = [
        {"cidade": "Mumbai", "risco": "alto"},
        {"cidade": "Delhi", "risco": "baixo"},
        {"cidade": "Chennai", "risco": "médio"},
        {"cidade": "Kolkata", "risco": "alto"},
        {"cidade": "Jaipur", "risco": "baixo"}
    ] # 
    print(f"Cidades com risco 'alto': {filtrar_cidades_por_risco(dados_cidades_q9, 'alto')}")
    print(f"Cidades com risco 'médio': {filtrar_cidades_por_risco(dados_cidades_q9, 'médio')}")