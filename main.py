# main.py

"""
Sistema Principal de Monitoramento Climático
===========================================

Este é o arquivo principal que executa todas as questões da Global Solution.
Permite executar questões individuais através de um menu interativo.

Desenvolvido para: Global Solution - Computational Thinking with Python (2SEM2025)

Estrutura do projeto:
- risco.py: Funções de análise de riscos climáticos (4 funções)
- validacao.py: Funções de validação e verificação (2 funções)  
- analise.py: Funções de análise de dados meteorológicos (2 funções)
- alertas.py: Funções de sistema de alertas (2 funções)
- main.py: Arquivo principal com menu de execução
"""

# Importações dos módulos organizados
from bibliotecas.risco import *
from bibliotecas.validacao import *
from bibliotecas.analise import *
from bibliotecas.alertas import *

def executar_questao_1():
    """
    Questão 1: Verificar risco de inundação por chuva
    Replica o comportamento do questao_1.py
    """
    print("\n" + "="*60)
    print("QUESTÃO 1: Verificar Risco de Inundação por Chuva")
    print("="*60)
    
    perguntar_mm = float(input("Digite a quantidade de milímetros de chuva prevista para uma cidade: "))
    print(verificar_risco_inundacao_por_chuva(perguntar_mm))

def executar_questao_2():
    """
    Questão 2: Classificar risco
    Replica o comportamento do questao_2.py
    """
    print("\n" + "="*60)
    print("QUESTÃO 2: Classificar Risco")
    print("="*60)
    
    perguntar_chuva = float(input("Digite a quantidade de chuva: "))
    print(classificar_risco(perguntar_chuva))

def executar_questao_3():
    """
    Questão 3: Identificar cidades com risco alto
    Replica o comportamento do questao_3.py
    """
    print("\n" + "="*60)
    print("QUESTÃO 3: Identificar Cidades com Risco Alto")
    print("="*60)
    
    chuvas = {
        "Mumbai": 120,
        "Delhi": 45,
        "Chennai": 80,
        "Kolkata": 130,
        "Jaipur": 30
    }
    
    print(identificar_cidades_risco_alto_dict(chuvas))

def executar_questao_4():
    """
    Questão 4: Encontrar temperaturas extremas
    Replica o comportamento do questao_4.py
    """
    print("\n" + "="*60)
    print("QUESTÃO 4: Encontrar Temperaturas Extremas")
    print("="*60)
    
    temperaturas = []

    for i in range(5):
        temperatura = float(input(f"Digite a temperatura {i+1} em ( graus Celsius ): "))
        temperaturas.append(temperatura)

    print(encontrar_temperaturas_extremas(temperaturas))

def executar_questao_5():
    """
    Questão 5: Enviar alertas em lote
    Replica o comportamento do questao_5.py
    """
    print("\n" + "="*60)
    print("QUESTÃO 5: Enviar Alertas em Lote")
    print("="*60)
    
    cidades = ["Mumbai", "Delhi", "Chennai", "Kolkata", "Jaipur"]
    enviar_alertas_lote(cidades)

def executar_questao_6():
    """
    Questão 6: Calcular média semanal de chuva
    Replica o comportamento do questao_6.py
    """
    print("\n" + "="*60)
    print("QUESTÃO 6: Calcular Média Semanal de Chuva")
    print("="*60)
    
    chuvas_diarias = []

    for i in range(7):
        chuva = float(input(f"Digite a quantidade de chuva do dia {i+1} em ( mm ): "))
        chuvas_diarias.append(chuva)

    media_critica, msg_critica = calcular_media_chuva_semanal_e_alertar(chuvas_diarias)
    print(f"Média de chuva (crítica): {media_critica:.2f}mm.\nMensagem: '{msg_critica}'")

def executar_questao_7():
    """
    Questão 7: Simular contagem de dias de onda de calor
    Replica o comportamento do questao_7.py
    """
    print("\n" + "="*60)
    print("QUESTÃO 7: Simular Contagem de Dias de Onda de Calor")
    print("="*60)
    
    simular_contagem_dias_onda_calor()

def executar_questao_8():
    """
    Questão 8: Validar nome da cidade
    Replica o comportamento do questao_8.py
    """
    print("\n" + "="*60)
    print("QUESTÃO 8: Validar Nome da Cidade")
    print("="*60)
    
    nome = input("Digite o nome da cidade: ")
    print(validar_nome_cidade(nome))

def executar_questao_9():
    """
    Questão 9: Filtrar cidades por risco
    Replica o comportamento do questao_9.py
    """
    print("\n" + "="*60)
    print("QUESTÃO 9: Filtrar Cidades por Risco")
    print("="*60)
    
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

def executar_questao_10():
    """
    Questão 10: Verificar nível do rio
    Replica o comportamento do questao_10.py
    """
    print("\n" + "="*60)
    print("QUESTÃO 10: Verificar Nível do Rio")
    print("="*60)
    
    nivel_rio = float(input("Digite o nível do rio em ( metros ): "))
    print(verificar_nivel_rio(nivel_rio))

def mostrar_menu():
    """Exibe o menu principal"""
    print("\n" + "="*70)
    print("SISTEMA DE MONITORAMENTO CLIMÁTICO - GLOBAL SOLUTION")
    print("="*70)
    print("Escolha qual questão deseja executar:")
    print()
    print(" [1]  Questão 1  - Verificar risco de inundação por chuva")
    print(" [2]  Questão 2  - Classificar risco")
    print(" [3]  Questão 3  - Identificar cidades com risco alto")
    print(" [4]  Questão 4  - Encontrar temperaturas extremas")
    print(" [5]  Questão 5  - Enviar alertas em lote")
    print(" [6]  Questão 6  - Calcular média semanal de chuva")
    print(" [7]  Questão 7  - Simular onda de calor")
    print(" [8]  Questão 8  - Validar nome da cidade")
    print(" [9]  Questão 9  - Filtrar cidades por risco")
    print(" [10] Questão 10 - Verificar nível do rio")
    print()
    print(" [0]  Sair")
    print("="*70)

def main():
    """Função principal que controla o menu e execução"""
    
    print("🌦️  Sistema de Monitoramento Climático - Global Solution")
    print("📁 Módulos carregados com sucesso:")
    print("   ✓ risco.py - Análise de riscos climáticos")
    print("   ✓ validacao.py - Validações e verificações")
    print("   ✓ analise.py - Análise de dados meteorológicos")
    print("   ✓ alertas.py - Sistema de alertas")
    
    while True:
        try:
            mostrar_menu()
            opcao = input("\n➤ Digite o número da questão que deseja executar: ").strip()
            
            if opcao == "1":
                executar_questao_1()
            elif opcao == "2":
                executar_questao_2()
            elif opcao == "3":
                executar_questao_3()
            elif opcao == "4":
                executar_questao_4()
            elif opcao == "5":
                executar_questao_5()
            elif opcao == "6":
                executar_questao_6()
            elif opcao == "7":
                executar_questao_7()
            elif opcao == "8":
                executar_questao_8()
            elif opcao == "9":
                executar_questao_9()
            elif opcao == "10":
                executar_questao_10()
            elif opcao == "0":
                print("\n👋 Encerrando sistema...")
                print("Obrigado por usar o Sistema de Monitoramento Climático!")
                break
            else:
                print("\n❌ Opção inválida! Digite um número de 0 a 10.")
                
        except ValueError as e:
            print(f"\n❌ Erro de entrada: {e}")
            print("Por favor, digite um valor numérico válido.")
        except KeyboardInterrupt:
            print("\n\n👋 Sistema interrompido pelo usuário. Encerrando...")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            print("Tentando continuar...")
        
        # Pausa antes de mostrar o menu novamente
        input("\n⏸️  Pressione Enter para voltar ao menu principal...")

if __name__ == "__main__":
    main()