# validacao.py

"""
Módulo de Validações e Verificações de Segurança
===============================================

Este módulo contém funções especializadas na validação de dados de entrada
e verificação de condições de segurança críticas do sistema de monitoramento
climático.

Funções incluídas:
- validar_nome_cidade(): Valida nomes de cidades conforme critérios específicos
- verificar_nivel_rio(): Verifica níveis críticos de rios para evacuação

Desenvolvido para: Global Solution - Computational Thinking with Python (2SEM2025)
"""

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
    # Exemplos de uso das funções de validação
    print("=== Testando Módulo de Validação ===")

    # Questão 8
    print("\nQ8: Validar Nome da Cidade")
    print(f"Validar 'Recife': {validar_nome_cidade('Recife')}")
    print(f"Validar 'rio': {validar_nome_cidade('rio')}")
    print(f"Validar 'SP': {validar_nome_cidade('SP')}")
    print(f"Validar 'Belo Horizonte': {validar_nome_cidade('Belo Horizonte')}")

    # Questão 10
    print("\nQ10: Verificar Nível do Rio")
    print(f"Nível do rio 6.5m: {verificar_nivel_rio(6.5)}")
    print(f"Nível do rio 4.0m: {verificar_nivel_rio(4.0)}")