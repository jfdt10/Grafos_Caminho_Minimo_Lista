# README - Cenário 1
## Descrição

Este arquivo implementa uma solução para o **Cenário 1: Estação Central**, utilizando o algoritmo Floyd-Warshall para encontrar a estação central ou vértice central de um metrô considerando que os grafos não direcionados representam os pontos de conexões de metrô.

## Características do Problema

- **Grafo não direcionado** Representa as estações de metrô e as arestas que conectam elas. 
- **Objetivo:** Encontrar a estação central que minimiza a soma das distâncias para todos os outros vértices.

## Algoritmo Utilizado: Floyd-Warshall (Justificativa da Escolha)

O algoritmo de Floyd-Warshall foi escolhido por sua capacidade de retornar a distância mínima entre todos os pares de vértices, o que é extremamente útil quando precisamos da matriz de distâncias para somar as distâncias de cada linha e identificar a estação central de maneira mais simples. Embora o Floyd-Warshall tenha uma complexidade de O(n^3), menos eficiente que o Dijkstra, que é O(n^2) para arrays e listas e O(n * log(n)) para filas de prioridade com heap, ele é mais direto e simples para este cenário. Considerando que o grafo possui apenas 12 vértices e 22 arestas, o número de iterações do Floyd-Warshall é comparável ao do Dijkstra, que precisaria ser executado para cada vértice para obter resultados semelhantes. Portanto, o uso do Floyd-Warshall é justificável nesse contexto.

### Comparação: Pseudocódigo Clássico vs Implementação Python

#### Pseudocódigo Clássico do Floyd-Warshall Do livro de Grafos: Introdução e Prática de  Paulo Oswaldo Boaventura Netto (Editora Blucher)

```Pseudo-Código

início <dados G = (V,E); matriz de valores V(G); matriz de roteamento R = [rᵢⱼ];
    rᵢⱼ ← j  ∀i; D⁰ = [dᵢⱼ] ← V(G);
    para k = 1, ..., n fazer [ k é o vértice-base da iteração ]
        início
            para todo i, j = 1, ..., n fazer
                se dᵢₖ + dₖⱼ < dᵢⱼ então
                    início
                        dᵢⱼ ← dᵢₖ + dₖⱼ;
                        rᵢⱼ ← rᵢₖ;
                    fim;
        fim;
fim.
```

#### Implementação em Python

```python
def floyd_warshall(num_vertices, distancias, roteamento):
    # Cópia das matrizes para evitar modificação da original
    dist = [list(row) for row in distancias]  # D^0 = [dij] ← V(G)
    rot = [list(row) for row in roteamento]   # R^0 =   rᵢⱼ ← j  ∀i
    
    # Algoritmo principal: para cada vértice intermediário k
    for k in range(num_vertices):              # para k = 1, ..., n fazer
        for i in range(num_vertices):          # para todo i, j = 1, ..., n fazer
            for j in range(num_vertices):      # para todo i, j = 1, ..., n fazer
                # Verifica se o caminho via k é menor
                if dist[i][k] + dist[k][j] < dist[i][j]:  # se dik + dkj < dij então
                    dist[i][j] = dist[i][k] + dist[k][j]   # dij ← dik + dkj
                    rot[i][j] = rot[i][k]                   # rij ← rik
                
    return dist, rot
```

#### Comparativo

| Aspecto | Pseudocódigo Clássico | Implementação Python |
|---------|----------------------|---------------------|
| **Inicialização** | `D^0 = [dij] ← V(G)` | `dist = [list(row) for row in distancias]` |
| **Roteamento** | `R^0 ←  rᵢⱼ ← j  ∀i` | `rot = [list(row) for row in roteamento]` |
| **Loop principal** | `para k = 1, ..., n fazer` | `for k in range(num_vertices)` |
| **Loops aninhados** | `para todo i, j = 1, ..., n fazer` | `for i in range(num_vertices)` |
| **Condição** | `se dik + dkj < dij então` | `if dist[i][k] + dist[k][j] < dist[i][j]` |
| **Atualização distância** | `dij ← dik + dkj` | `dist[i][j] = dist[i][k] + dist[k][j]` |
| **Atualização roteamento** | `rij ← rik` | `rot[i][j] = rot[i][k]` |

**Otimizações implementadas na versão Python:**
- Cópia das matrizes para preservar os dados originais
- Tratamento eficiente de memória com listas aninhadas

## Funcionalidades
 
### Principais
 
- `floyd_warshall(num_vertices, distancias, roteamento)`: Implementa o algoritmo principal
- `reconstruir_caminho(origem, destino, roteamento)`: Reconstrói o caminho mínimo
- `carregar_grafo(nome_arquivo)`: Lê grafo do arquivo de entrada
- `analisar_resultados(num_vertices, matriz_distancias)`: Analisa a matriz de distâncias para encontrar a estação central baseado no menor somatório de distâncias e a menor distância máxima como critério de desempate.
- `formatar_matriz_para_impressao(matriz, titulo)`: Formata a matriz para impressão.



## Formato do Arquivo de Entrada

```
12  22      #num_vertices num_arestas
1   2   17  # v1 v2 custo
1   3   25  # v1 v2 custo
1   5   21  # v1 v2 custo
2   4   10  # v1 v2 custo
2   6   15  # v1 v2 custo
3   7   20  # v1 v2 custo
4   6   9   # v1 v2 custo
4   8   23  # v1 v2 custo
... 
```

- **Primeira linha:** `num_vertices num_arestas`
- **Demais linhas:** `v1 v2 custo`

## Como Executar

```bash
cd Cenario1
python main.py
```

O programa automaticamente:
1. Lê o arquivo `graph1.txt` (não cria)
2. Carrega e processa o grafo
3. Executa o algoritmo Floyd-Warshall
4. Identifica a estação central baseada na menor soma de distâncias
5. Exibe os resultados conforme especificado no enunciado

## Dependências

- Python 3.x (bibliotecas padrão apenas)
