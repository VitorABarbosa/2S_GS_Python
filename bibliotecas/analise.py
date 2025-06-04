# analise.py

"""
Módulo de Análise de Dados Meteorológicos
========================================

Este módulo contém funções especializadas na análise e processamento de dados
meteorológicos, incluindo análise de temperaturas extremas e cálculos de médias
de precipitação.

Funções incluídas:
- encontrar_temperaturas_extremas(): Encontra temperaturas máxima e mínima
- calcular_media_chuva_semanal_e_alertar(): Calcula média semanal e gera alertas

Desenvolvido para: Global Solution - Computational Thinking with Python (2SEM2025)
"""

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

if __name__ == '__main__':
    # Exemplos de uso das funções de análise
    print("=== Testando Módulo de Análise ===")

    # Questão 4
    print("\nQ4: Temperaturas Extremas")
    temps_q4 = [28, 35, 22, 40, 19]
    altas_baixas_q4 = encontrar_temperaturas_extremas(temps_q4)
    if altas_baixas_q4:
        print(f"Temperaturas: {temps_q4} -> Mais alta: {altas_baixas_q4[0]}, Mais baixa: {altas_baixas_q4[1]}")
    
    temps_vazia_q4 = []
    altas_baixas_vazia_q4 = encontrar_temperaturas_extremas(temps_vazia_q4)
    print(f"Temperaturas vazias: {altas_baixas_vazia_q4}")

    # Questão 6
    print("\nQ6: Média Semanal de Chuva e Alerta")
    chuvas_semana_critica_q6 = [100, 120, 90, 110, 80, 130, 95] # Média > 90
    media_critica, msg_critica = calcular_media_chuva_semanal_e_alertar(chuvas_semana_critica_q6)
    print(f"Média de chuva (crítica): {media_critica:.2f}mm. Mensagem: '{msg_critica}'")
    
    chuvas_semana_normal_q6 = [50, 60, 40, 70, 55, 65, 45] # Média < 90
    media_normal, msg_normal = calcular_media_chuva_semanal_e_alertar(chuvas_semana_normal_q6)
    print(f"Média de chuva (normal): {media_normal:.2f}mm. Mensagem: '{msg_normal}'")