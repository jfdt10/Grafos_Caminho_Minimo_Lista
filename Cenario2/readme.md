# README - cenário 2
## Descrição

Este arquivo implementa uma solução para o **Cenário 2: Carro Elétrico com Regeneração**, utilizando o algoritmo Bellman-Ford para encontrar o caminho de menor consumo energético em um grafo direcionado com pesos negativos.

## Características do Problema

- **Grafo direcionado** com pesos positivos (consumo de energia) e negativos (regeneração)
- **Origem:** Vértice 0
- **Destino:** Vértice 6
- **Objetivo:** Minimizar o consumo líquido de energia

## Algoritmo Utilizado: Bellman-Ford

O Bellman-Ford foi escolhido por ser capaz de lidar com **pesos negativos**.

### Comparação com o Pseudocódigo Clássico

A implementação segue a estrutura do algoritmo clássico:

```python
#inicialização
distancias = {v: float('inf') for v in vertices}
anteriores = {v: None for v in vertices}
distancias[origem] = 0

#relaxamento das arestas
for _ in range(len(vertices) - 1):
    for u in grafo:
        for v, peso in grafo[u]:
            if distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
                anteriores[v] = u

#detecção de ciclo negativo
for u in grafo:
    for v, peso in grafo[u]:
        if distancias[u] + peso < distancias[v]:
            tem_ciclo_negativo = True
```

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

## Saída Esperada

```
=== CENARIO 2: CARRO ELETRICO COM REGENERACAO ===
Algoritmo utilizado: Bellman-Ford
Motivo: Grafo direcionado com pesos negativos (regeneracao de energia)

Grafo carregado:
  0 -> 1: 25 Wh (consumo)
  0 -> 2: 12 Wh (consumo)
  0 -> 3: -8 Wh (regeneracao)
  ...

RESULTADOS:
Caminho minimo (vertice 0 -> vertice 6): 0 -> 3 -> 2 -> 1 -> 5 -> 6
Energia liquida consumida: -2 Wh
  > O carro chegara com 2 Wh a mais na bateria!

Detalhamento do caminho:
  0 -> 3: -8 Wh (Regeneracao)
  3 -> 2: -5 Wh (Regeneracao)
  2 -> 1: -6 Wh (Regeneracao)
  1 -> 5: -4 Wh (Regeneracao)
  5 -> 6: +5 Wh (Consumo)
```

## Tratamento de Casos Especiais

- **Ciclo negativo:** Detecta e alerta sobre ciclos de energia infinita
- **Caminho inexistente:** Verifica se existe caminho entre origem e destino
- **Erros de arquivo:** Tratamento robusto de arquivos inexistentes ou malformados

## Dependências

- Python 3.x (bibliotecas padrão apenas)
