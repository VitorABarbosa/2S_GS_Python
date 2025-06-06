# Sistema de Monitoramento Climático - Global Solution

## 📋 Descrição

Este projeto é um sistema completo de monitoramento climático desenvolvido para a **Global Solution - Computational Thinking with Python (2SEM2025)**. O sistema analisa dados meteorológicos, identifica riscos climáticos e emite alertas automáticos para prevenção de desastres naturais.

## 🏗️ Arquitetura do Projeto

O projeto foi organizado em módulos especializados para facilitar manutenção e reutilização:

```
projeto/
│
├── main.py                    # Arquivo principal com interface de menu
├── bibliotecas/               # Pasta com módulos organizados
│   ├── risco.py              # Módulo de análise de riscos (4 funções)
│   ├── validacao.py          # Módulo de validações (2 funções)
│   ├── analise.py            # Módulo de análise de dados (2 funções)
│   └── alertas.py            # Módulo de sistema de alertas (2 funções)
└── README.md                 # Esta documentação
```

## 🚀 Como Executar

### Execução Principal
Para iniciar o sistema, execute o arquivo principal:

```bash
python main.py
```

### Interface do Sistema
O sistema apresentará um menu interativo no terminal:

```
======================================================================
SISTEMA DE MONITORAMENTO CLIMÁTICO - GLOBAL SOLUTION
======================================================================
Escolha qual questão deseja executar:

 [1]  Questão 1  - Verificar risco de inundação por chuva
 [2]  Questão 2  - Classificar risco
 [3]  Questão 3  - Identificar cidades com risco alto
 [4]  Questão 4  - Encontrar temperaturas extremas
 [5]  Questão 5  - Enviar alertas em lote
 [6]  Questão 6  - Calcular média semanal de chuva
 [7]  Questão 7  - Simular onda de calor
 [8]  Questão 8  - Validar nome da cidade
 [9]  Questão 9  - Filtrar cidades por risco
 [10] Questão 10 - Verificar nível do rio

 [0]  Sair
======================================================================
```

## 📚 Módulos e Funções

### 🌊 risco.py - Análise de Riscos Climáticos

Este módulo está localizado em `bibliotecas/risco.py` e contém **4 funções** especializadas na análise de riscos:

#### `verificar_risco_inundacao_por_chuva(milimetros_chuva: float) -> str`
- **Propósito**: Verifica risco de inundação baseado em precipitação
- **Entrada**: Quantidade de chuva em mm
- **Saída**: "ALERTA: Risco alto de inundação" (>100mm) ou "Nível de risco normal"
- **Exemplo**:
  ```python
  resultado = verificar_risco_inundacao_por_chuva(120)
  print(resultado)  # "ALERTA: Risco alto de inundação"
  ```

#### `classificar_risco(chuva: float) -> str`
- **Propósito**: Classifica risco em três níveis
- **Entrada**: Quantidade de chuva em mm
- **Saída**: "baixo" (<50mm), "médio" (50-100mm), "alto" (>100mm)
- **Exemplo**:
  ```python
  nivel = classificar_risco(75)
  print(nivel)  # "médio"
  ```

#### `identificar_cidades_risco_alto_dict(dados_chuvas: dict) -> list`
- **Propósito**: Identifica cidades em risco alto a partir de dicionário
- **Entrada**: Dicionário {cidade: precipitacao_mm}
- **Saída**: Lista de cidades com risco alto
- **Exemplo**:
  ```python
  chuvas = {"Mumbai": 120, "Delhi": 45}
  cidades = identificar_cidades_risco_alto_dict(chuvas)
  print(cidades)  # ["Mumbai"]
  ```

#### `filtrar_cidades_por_risco(lista_cidades_info: list, nivel_risco_desejado: str = "alto") -> list`
- **Propósito**: Filtra lista de cidades por nível de risco
- **Entrada**: Lista de dicionários com dados das cidades e nível de risco desejado
- **Saída**: Lista filtrada com cidades do nível especificado
- **Exemplo**:
  ```python
  cidades = [{"cidade": "São Paulo", "risco": "alto"}]
  filtradas = filtrar_cidades_por_risco(cidades, "alto")
  ```

### ✅ validacao.py - Validações e Verificações

Este módulo está localizado em `bibliotecas/validacao.py` e contém **2 funções** para validação e verificação:

#### `validar_nome_cidade(nome: str) -> bool`
- **Propósito**: Valida formato de nome de cidade
- **Critérios**: Mais de 3 caracteres E primeira letra maiúscula
- **Entrada**: Nome da cidade
- **Saída**: True se válido, False caso contrário
- **Exemplo**:
  ```python
  valido = validar_nome_cidade("São Paulo")
  print(valido)  # True
  
  invalido = validar_nome_cidade("rio")
  print(invalido)  # False
  ```

#### `verificar_nivel_rio(nivel_metros: float) -> str`
- **Propósito**: Verifica necessidade de evacuação baseado no nível do rio
- **Entrada**: Nível do rio em metros
- **Saída**: "EVACUAR ÁREA" (>5m) ou "Segurança controlada"
- **Exemplo**:
  ```python
  status = verificar_nivel_rio(6.5)
  print(status)  # "EVACUAR ÁREA"
  ```

### 📊 analise.py - Análise de Dados Meteorológicos

Este módulo está localizado em `bibliotecas/analise.py` e contém **2 funções** para análise de dados:

#### `encontrar_temperaturas_extremas(temperaturas: list) -> tuple | None`
- **Propósito**: Encontra temperaturas máxima e mínima
- **Entrada**: Lista de temperaturas
- **Saída**: String formatada com extremos ou None se lista vazia
- **Exemplo**:
  ```python
  temps = [28, 35, 22, 40, 19]
  resultado = encontrar_temperaturas_extremas(temps)
  print(resultado)
  # "A temperatura mais alta é: 40
  #  A temperatura mais baixa é: 19"
  ```

#### `calcular_media_chuva_semanal_e_alertar(chuvas_diarias: list) -> tuple`
- **Propósito**: Calcula média semanal e determina necessidade de alerta
- **Entrada**: Lista com exatamente 7 valores de precipitação diária
- **Saída**: Tupla (média, mensagem_alerta)
- **Threshold**: Média > 90mm = crítico
- **Exemplo**:
  ```python
  chuvas = [100, 120, 90, 110, 80, 130, 95]
  media, msg = calcular_media_chuva_semanal_e_alertar(chuvas)
  print(f"Média: {media:.2f}mm - {msg}")
  # "Média: 103.57mm - Semana crítica! Monitoramento intensivo necessário"
  ```

### 🚨 alertas.py - Sistema de Alertas

Este módulo está localizado em `bibliotecas/alertas.py` e contém **2 funções** para sistema de alertas:

#### `enviar_alertas_lote(lista_cidades_risco_alto: list) -> list`
- **Propósito**: Simula envio de alertas automáticos para múltiplas cidades
- **Entrada**: Lista de nomes de cidades em risco alto
- **Saída**: Lista de mensagens de alerta enviadas
- **Comportamento**: Imprime cada alerta no console
- **Exemplo**:
  ```python
  cidades = ["Mumbai", "Kolkata"]
  mensagens = enviar_alertas_lote(cidades)
  # Saída no console:
  # Enviando alerta para Mumbai: risco alto de inundação!
  # Enviando alerta para Kolkata: risco alto de inundação!
  ```

#### `simular_contagem_dias_onda_calor() -> int`
- **Propósito**: Simula monitoramento contínuo de onda de calor
- **Funcionamento**: Loop interativo que solicita temperaturas diárias
- **Critério de parada**: Temperatura < 35°C
- **Entrada**: Temperaturas via input() do usuário
- **Saída**: Número total de dias da onda de calor
- **Exemplo de uso**:
  ```
  Iniciando simulação da onda de calor. A onda cessa com temperatura < 35°C.
  Digite a temperatura registrada para o dia 1 (em °C): 38
  Dia 1: Temperatura de 38.0°C. A onda de calor continua.
  Digite a temperatura registrada para o dia 2 (em °C): 34
  Onda de calor cessou no dia 2 com temperatura de 34.0°C.
  ```

## 🎯 Questões Implementadas

### Questão 1: Verificação de Risco por Chuva
- **Entrada**: Usuário digita quantidade de chuva em mm
- **Processamento**: Verifica se > 100mm
- **Saída**: Mensagem de alerta ou normalidade

### Questão 2: Classificação de Risco
- **Entrada**: Usuário digita quantidade de chuva
- **Processamento**: Classifica em baixo/médio/alto
- **Saída**: Nível de risco

### Questão 3: Identificação de Cidades em Risco
- **Dados**: Dicionário fixo com precipitação por cidade
- **Processamento**: Identifica cidades com risco alto
- **Saída**: Lista de cidades em risco

### Questão 4: Análise de Temperaturas Extremas
- **Entrada**: Usuário digita 5 temperaturas
- **Processamento**: Encontra máxima e mínima
- **Saída**: Temperaturas extremas

### Questão 5: Sistema de Alertas em Lote
- **Dados**: Lista fixa de cidades
- **Processamento**: Envia alertas para todas
- **Saída**: Mensagens de alerta no console

### Questão 6: Análise Semanal de Precipitação
- **Entrada**: Usuário digita 7 valores de chuva diária
- **Processamento**: Calcula média e verifica criticidade
- **Saída**: Média e status (normal/crítico)

### Questão 7: Simulação de Onda de Calor
- **Entrada**: Temperaturas diárias via input
- **Processamento**: Conta dias até temperatura < 35°C
- **Saída**: Duração total da onda de calor

### Questão 8: Validação de Nomes de Cidades
- **Entrada**: Usuário digita nome da cidade
- **Processamento**: Valida critérios (>3 chars + maiúscula)
- **Saída**: True/False

### Questão 9: Filtro de Cidades por Risco
- **Dados**: Lista fixa de cidades com riscos
- **Processamento**: Filtra por risco alto
- **Saída**: Cidades filtradas formatadas

### Questão 10: Verificação de Nível de Rio
- **Entrada**: Usuário digita nível em metros
- **Processamento**: Verifica se > 5m
- **Saída**: Status de segurança ou evacuação

## 🛠️ Funcionalidades do Sistema

### Interface Interativa
- Menu numerado para seleção de questões
- Navegação simples e intuitiva
- Tratamento de erros robusto
- Opção de retorno ao menu principal

### Tratamento de Erros
- Validação de entrada numérica
- Mensagens de erro amigáveis
- Recuperação graceful de erros
- Interrupção controlada (Ctrl+C)

### Organização Modular
- Separação lógica de responsabilidades
- Reutilização de código
- Facilidade de manutenção
- Documentação detalhada

## 📖 Exemplos de Uso

### Estrutura de Importação
O `main.py` importa as funções dos módulos organizados na pasta `bibliotecas/`:

```python
from bibliotecas.risco import *
from bibliotecas.validacao import *
from bibliotecas.analise import *
from bibliotecas.alertas import *
```

### Exemplo 1: Executando Questão 1
```bash
$ python main.py

➤ Digite o número da questão que deseja executar: 1

============================================================
QUESTÃO 1: Verificar Risco de Inundação por Chuva
============================================================
Digite a quantidade de milímetros de chuva prevista para uma cidade: 120
ALERTA: Risco alto de inundação

⏸️ Pressione Enter para voltar ao menu principal...
```

### Exemplo 2: Executando Questão 4
```bash
➤ Digite o número da questão que deseja executar: 4

============================================================
QUESTÃO 4: Encontrar Temperaturas Extremas
============================================================
Digite a temperatura 1 em ( graus Celsius ): 28
Digite a temperatura 2 em ( graus Celsius ): 35
Digite a temperatura 3 em ( graus Celsius ): 22
Digite a temperatura 4 em ( graus Celsius ): 40
Digite a temperatura 5 em ( graus Celsius ): 19
A temperatura mais alta é: 40
A temperatura mais baixa é: 19
```

## 🧪 Testes

### Testes dos Módulos
Cada módulo pode ser testado independentemente:

```bash
# Teste individual dos módulos
python bibliotecas/risco.py
python bibliotecas/validacao.py
python bibliotecas/analise.py
python bibliotecas/alertas.py
```

### Teste do Sistema Completo
Para testar o sistema completo:

```bash
python main.py
```

## ⚙️ Requisitos Técnicos

### Dependências
- Python 3.6 ou superior
- Módulos padrão do Python (sem dependências externas)

### Estrutura de Arquivos
A estrutura deve seguir a organização modular:

```
projeto/
├── main.py                    # Arquivo principal - execute este
├── bibliotecas/               # Pasta com módulos
│   ├── risco.py
│   ├── validacao.py
│   ├── analise.py
│   └── alertas.py
└── README.md
```

### Testes dos Módulos
Cada módulo pode ser testado independentemente:

```bash
# Teste individual dos módulos
python bibliotecas/risco.py
python bibliotecas/validacao.py
python bibliotecas/analise.py
python bibliotecas/alertas.py
```

## 📈 Critérios e Thresholds

### Riscos de Inundação
- **Baixo**: < 50mm de chuva
- **Médio**: 50-100mm de chuva
- **Alto**: > 100mm de chuva

### Níveis de Rio
- **Segurança controlada**: ≤ 5 metros
- **Evacuação necessária**: > 5 metros

### Onda de Calor
- **Onda continua**: ≥ 35°C
- **Onda cessa**: < 35°C

### Média Semanal Crítica
- **Normal**: ≤ 90mm de média
- **Crítica**: > 90mm de média

## 👥 Autores

**Equipe de Desenvolvimento:**

- **Renato de Oliveira Barros** - RM559702
- **Guilherme Henrique Costa de Almeida** - RM559977  
- **Vitor Adauto Alves Barbosa** - RM560247

Desenvolvido para Global Solution - Computational Thinking with Python (2SEM2025)

## 📝 Licença

Este projeto é desenvolvido para fins educacionais no contexto da Global Solution.

---

**🌦️ Sistema de Monitoramento Climático - Prevenindo desastres através da tecnologia**
