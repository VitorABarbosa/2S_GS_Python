# funcoes_solucao_global.py

"""
Módulo da Global Solution - Computational Thinking with Python (2SEM2025)

Este módulo contém um conjunto de funções desenvolvidas para atender aos requisitos
da Global Solution, focando na análise e resposta a eventos climáticos extremos,
como chuvas intensas e enchentes, no contexto de um projeto de monitoramento
climático em parceria com o governo indiano.

As funções aqui presentes simulam etapas de um pipeline de dados, desde a
entrada e classificação de riscos até o envio de alertas e validações.
Este arquivo serve como uma biblioteca Python reutilizável, com funções organizadas
e documentadas, conforme solicitado na Questão 11.
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

def encontrar_temperaturas_extremas(temperaturas: list) -> tuple | None:
    """
    Encontra a temperatura mais alta e a mais baixa em uma lista de temperaturas.
    Corresponde à Questão 4.

    Args:
        temperaturas: Uma lista de temperaturas (em graus Celsius).

    Returns:
        Uma tupla contendo (temperatura_mais_alta, temperatura_mais_baixa).
        Retorna None se a lista estiver vazia.
    """
    if not temperaturas:
        return None
    
    mais_alta = temperaturas[0]
    mais_baixa = temperaturas[0]
    
    for temp in temperaturas:
        if temp > mais_alta:
            mais_alta = temp
        if temp < mais_baixa:
            mais_baixa = temp
            
    return f"A temperatura mais alta é: {mais_alta}\nA temperatura mais baixa é: {mais_baixa}"

def enviar_alertas_lote(lista_cidades_risco_alto: list) -> list:
    """
    Simula o envio de alertas automáticos para uma lista de cidades com risco alto.
    Corresponde à Questão 5.

    Args:
        lista_cidades_risco_alto: Uma lista de nomes de cidades com risco alto.
                                     Exemplo: ["Mumbai", "Kolkata", "Patna"] 

    Returns:
        Uma lista de strings, onde cada string é a mensagem de alerta enviada
        para uma cidade.
    """
    mensagens_alerta = []
    for cidade in lista_cidades_risco_alto: 
        mensagem = f"Enviando alerta para {cidade}: risco alto de inundação!" 
        print(mensagem) # Conforme a questão pede para imprimir
        mensagens_alerta.append(mensagem)
    return mensagens_alerta

def calcular_media_chuva_semanal_e_alertar(chuvas_diarias: list) -> tuple:
    """
    Calcula a média de chuvas em 7 dias e exibe uma mensagem se a média for crítica.
    Corresponde à Questão 6.

    Args:
        chuvas_diarias: Uma lista contendo 7 valores numéricos representando
                        a precipitação diária em mm.

    Returns:
        Uma tupla contendo (media_chuva, mensagem_alerta).
        A mensagem_alerta será "Semana crítica! Monitoramento intensivo necessário"
        se a média for > 90 , ou uma string vazia caso contrário.
    """
    if len(chuvas_diarias) != 7:
        raise ValueError("A lista de chuvas diárias deve conter exatamente 7 dias.")
    
    media_chuva = sum(chuvas_diarias) / len(chuvas_diarias)
    mensagem_alerta = ""
    
    if media_chuva > 90: 
        mensagem_alerta = "Semana crítica! Monitoramento intensivo necessário" 
        print(mensagem_alerta)
    if media_chuva <= 90:
        mensagem_alerta = "Semana normal! Monitoramento normal"
        
    return (media_chuva, mensagem_alerta)

def simular_contagem_dias_onda_calor() -> int:
    """
    Simula a contagem de dias até o fim de uma onda de calor extremo.
    A onda de calor cessa quando a temperatura registrada for menor que 35°C.
    Utiliza input() para simular a entrada de dados de temperatura.
    Corresponde à Questão 7.

    Returns:
        O número de dias que a onda de calor durou.
    """
    dias_onda_calor = 0
    temperatura_atual = 0.0

    print("Iniciando simulação da onda de calor. A onda cessa com temperatura < 35°C.")
    while True:
        try:
            entrada_temp = input(f"Digite a temperatura registrada para o dia {dias_onda_calor + 1} (em °C): ")
            temperatura_atual = float(entrada_temp)
            
            if temperatura_atual < 35: # 
                print(f"Onda de calor cessou no dia {dias_onda_calor + 1} com temperatura de {temperatura_atual}°C.")
                break
            else:
                dias_onda_calor += 1
                print(f"Dia {dias_onda_calor}: Temperatura de {temperatura_atual}°C. A onda de calor continua.")
                
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a temperatura.")
            
    return dias_onda_calor + 1 # Retorna o total de dias, incluindo o dia em que cessou

def validar_nome_cidade(nome: str) -> bool:
    """
    Valida o nome de uma cidade.
    Corresponde à Questão 8.

    Args:
        nome: O nome da cidade (string).

    Returns:
        True se o nome tiver mais de 3 caracteres E começar com letra maiúscula.
        False caso contrário.
    """
    if len(nome) > 3 and nome[0].isupper(): # 
        return True
    return False # 

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

def verificar_nivel_rio(nivel_metros: float) -> str:
    """
    Verifica o nível do rio e retorna uma mensagem de ação com base nesse nível.
    Corresponde à Questão 10. 

    Args:
        nivel_metros: O nível atual do rio em metros.

    Returns:
        "EVACUAR ÁREA" se o nível estiver acima de 5 metros.
        "Segurança controlada" caso contrário.
    """
    if nivel_metros > 5: # 
        return "EVACUAR ÁREA" # 
    else:
        return "Segurança controlada" # 

if __name__ == '__main__':
    # Exemplos de uso (para teste rápido do módulo)
    print("--- Testando Funções ---")

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

    # Questão 4
    print("\nQ4: Temperaturas Extremas")
    temps_q4 = [28, 35, 22, 40, 19]
    altas_baixas_q4 = encontrar_temperaturas_extremas(temps_q4)
    if altas_baixas_q4:
        print(f"Temperaturas: {temps_q4} -> Mais alta: {altas_baixas_q4[0]}, Mais baixa: {altas_baixas_q4[1]}")
    
    temps_vazia_q4 = []
    altas_baixas_vazia_q4 = encontrar_temperaturas_extremas(temps_vazia_q4)
    print(f"Temperaturas vazias: {altas_baixas_vazia_q4}")


    # Questão 5
    print("\nQ5: Enviar Alertas em Lote")
    cidades_alerta_q5 = ["Mumbai", "Kolkata", "Patna"] # 
    enviar_alertas_lote(cidades_alerta_q5)

    # Questão 6
    print("\nQ6: Média Semanal de Chuva e Alerta")
    chuvas_semana_critica_q6 = [100, 120, 90, 110, 80, 130, 95] # Média > 90
    media_critica, msg_critica = calcular_media_chuva_semanal_e_alertar(chuvas_semana_critica_q6)
    print(f"Média de chuva (crítica): {media_critica:.2f}mm. Mensagem: '{msg_critica}'")
    
    chuvas_semana_normal_q6 = [50, 60, 40, 70, 55, 65, 45] # Média < 90
    media_normal, msg_normal = calcular_media_chuva_semanal_e_alertar(chuvas_semana_normal_q6)
    print(f"Média de chuva (normal): {media_normal:.2f}mm. Mensagem: '{msg_normal}'")

    # Questão 8
    print("\nQ8: Validar Nome da Cidade")
    print(f"Validar 'Recife': {validar_nome_cidade('Recife')}")
    print(f"Validar 'rio': {validar_nome_cidade('rio')}")
    print(f"Validar 'SP': {validar_nome_cidade('SP')}")
    print(f"Validar 'Belo Horizonte': {validar_nome_cidade('Belo Horizonte')}")

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

    # Questão 10
    print("\nQ10: Verificar Nível do Rio")
    print(f"Nível do rio 6.5m: {verificar_nivel_rio(6.5)}")
    print(f"Nível do rio 4.0m: {verificar_nivel_rio(4.0)}")


    print("\n--- Fim dos Testes ---")