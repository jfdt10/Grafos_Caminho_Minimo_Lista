# README - Cenário 2
## Descrição

Este arquivo implementa uma solução para o **Cenário 2: Carro Elétrico com Regeneração**, utilizando o algoritmo Bellman-Ford para encontrar o caminho de menor consumo energético em um grafo direcionado com pesos negativos.

## Características do Problema

- **Grafo direcionado** com pesos positivos (consumo de energia) e negativos (regeneração)
- **Origem:** Vértice 0
- **Destino:** Vértice 6
- **Objetivo:** Minimizar o consumo líquido de energia

## Algoritmo Utilizado: Bellman-Ford

O Bellman-Ford foi escolhido por ser capaz de lidar com **pesos negativos**.

### Comparação com o Pseudocódigo Clássico vs Implementação Python

#### Pseudocódigo Clássico do Bellman-Ford Do livro de Grafos: Introdução e Prática de  Paulo Oswaldo Boaventura Netto (Editora Blucher)

```Pseudo-Código
início
   d11 ← 0;  d1i ← ∞  ∀ i ∈ V – {1};  anterior(i) ← 0  ∀ i;
   enquanto ∃ (j,i) ∈ A | d1i > d1j + vji  fazer   [ varre todos os arcos aplicando o critério ]
      início
         d1i ← d1j + vji;  anterior(i) ← j;
      fim;
fim.
```

#### Implementação em Python

```python
def bellman_ford(grafo, origem):
    """
    Recebe:
    - grafo: dicionário onde chave é vértice origem e valor é lista de (destino, peso)
    - origem: vértice de origem
    
    Retorna:
    - distancias: dicionário com distâncias mínimas
    - anteriores: dicionário para reconstruir o caminho
    - tem_ciclo_negativo: booleano indicando se há ciclo negativo
    """

    vertices = set()
    for v in grafo:
        vertices.add(v)
        for vizinho, peso in grafo[v]:
            vertices.add(vizinho)
    # Inicialização
    distancias = {v: float('inf') for v in vertices}
    # Atribuição inicial
    anteriores = {v: None for v in vertices}
    # Atualização de Origem
    distancias[origem] = 0
    
    #relaxamento das arestas
    for _ in range(len(vertices) - 1):
        atualizado = False
        for u in grafo:
            if distancias[u] != float('inf'):
                for v, peso in grafo[u]:
                    if distancias[u] + peso < distancias[v]:
                        distancias[v] = distancias[u] + peso
                        anteriores[v] = u # Atualização de Anterior
                        atualizado = True
        
        #se não tiver, para antes
        if not atualizado:
            break
    
    #ciclo negativo(detecção)
    tem_ciclo_negativo = False
    for u in grafo:
        if distancias[u] != float('inf'):
            for v, peso in grafo[u]:
                if distancias[u] + peso < distancias[v]:
                    tem_ciclo_negativo = True
                    break
        if tem_ciclo_negativo:
            break
    
    return distancias, anteriores, tem_ciclo_negativo

```
#### Comparativo
| Aspecto | Pseudocódigo Clássico | Implementação Python |
|---------|----------------------|---------------------|
| **Inicialização** | `d11 ← 0;  d1i ← ∞` | `distancias = {v: float('inf') for v in vertices}` |
| **Atribuição inicial** | `anterior(i) ← 0` | `anteriores = {v: None for v in vertices}` |
| **Atualização origem** | `d1i ← 0` | `distancias[origem] = 0` |
| **Relaxamento** | `enquanto ∃ (j,i) ∈ A | d1i > d1j + vji` | `for _ in range(len(vertices) - 1):` |
| **Ajuste de distâncias** | `d1i ← d1j + vji` | `if distancias[u] + peso < distancias[v]:` |
| **Ajuste de antecessores** | `anterior(i) ← j` | `anteriores[v] = u` |
| **Detecção de ciclo** | `d1i > d1j + vji` | `if distancias[u] + peso < distancias[v]:` |


**Otimizações implementadas:**
- Parada antecipada se nenhuma distância for atualizada
- Verificação de alcançabilidade para evitar processamento desnecessário
- Break duplo na detecção de ciclo negativo

## Funcionalidades

### Principais

- `bellman_ford(grafo, origem)`: Implementa o algoritmo principal
- `reconstruir_caminho(anteriores, origem, destino)`: Reconstrói o caminho mínimo
- `ler_grafo(nome_arquivo)`: Lê grafo do arquivo de entrada
- `calcular_custo_caminho(grafo, caminho)`: Calcula o custo total do caminho
- `resolver_cenario2()`: Função principal que executa a solução completa

### Utilitárias

- `criar_arquivo_exemplo()`: Cria automaticamente o arquivo `graph2.txt` para testes

## Formato do Arquivo de Entrada

```
7    14
0    1    25
0    2    12
0    3    -8
...
```

- **Primeira linha:** `num_vertices num_arestas`
- **Demais linhas:** `origem destino peso`

## Como Executar

```bash
python main.py
```

O programa automaticamente:
1. Cria o arquivo `graph2.txt` se não existir
2. Carrega e exibe o grafo
3. Executa o Bellman-Ford
4. Mostra o caminho mínimo e consumo energético
5. Detalha cada trecho do caminho


## Dependências

- Python 3.x (bibliotecas padrão apenas)
