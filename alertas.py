# alertas.py

"""
Módulo de Sistema de Alertas e Notificações
==========================================

Este módulo contém funções especializadas no sistema de alertas automáticos
e simulações de eventos climáticos críticos. Responsável por gerenciar
notificações em massa e monitoramento contínuo de eventos extremos.

Funções incluídas:
- enviar_alertas_lote(): Envia alertas automáticos para lista de cidades
- simular_contagem_dias_onda_calor(): Simula monitoramento de onda de calor

Desenvolvido para: Global Solution - Computational Thinking with Python (2SEM2025)
"""

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

if __name__ == '__main__':
    # Exemplos de uso das funções de alertas
    print("=== Testando Módulo de Alertas ===")

    # Questão 5
    print("\nQ5: Enviar Alertas em Lote")
    cidades_alerta_q5 = ["Mumbai", "Kolkata", "Patna"] # 
    enviar_alertas_lote(cidades_alerta_q5)

    # Questão 7 - Comentado para não interromper os testes automáticos
    print("\nQ7: Simulação de Onda de Calor")
    print("Função disponível: simular_contagem_dias_onda_calor()")
    print("Execute separadamente para testar a interação com input()")
    # simular_contagem_dias_onda_calor()