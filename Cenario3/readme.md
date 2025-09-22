# Cenário 3: Robô de Armazém com Obstáculos

## Algoritmo Escolhido: Dijkstra

### Por que Dijkstra?
- **Pesos não-negativos**: Todos os custos são ≥ 0 (célula livre = 1, piso difícil = 3)
- **Melhor aproveitamento da situação do problema**: Dijkstra é ideal para grafos com pesos positivos
- **Garantia de otimalidade**: Encontra o caminho mínimo global
- **Eficiência**: O(V log V + E) onde V = células e E = conexões entre células

### Comparação com o Pseudocódigo da Aula

**Pseudocódigo Original:**
```
DIJKSTRA(G, w, s):
1. INITIALIZE-SINGLE-SOURCE(G, s)
2. S = ∅
3. Q = G.V
4. while Q ≠ ∅:
5.    u = EXTRACT-MIN(Q)
6.    S = S ∪ {u}
7.    for each vertex v ∈ G.Adj[u]:
8.       RELAX(u, v, w)
```

**Implementação no Código (main.py):**
1. **INITIALIZE-SINGLE-SOURCE**: Linhas 109-119 - inicializa `distances` e `predecessors`
2. **S = ∅**: Linha 113 - conjunto `visited`
3. **Q = G.V**: Linha 127 - priority queue `pq`
4. **while Q ≠ ∅**: Linha 132 - loop principal
5. **EXTRACT-MIN(Q)**: Linha 135 - `heapq.heappop(pq)`
6. **S = S ∪ {u}**: Linha 142 - `visited.add(current_pos)`
7. **RELAX**: Linhas 154-160 - atualização de distâncias e predecessores

## Regras do Grid
- `.` = célula livre (custo 1)
- `#` = obstáculo (intransponível)
- `~` = piso difícil (custo 3)
- `S` = início
- `G` = objetivo
- Movimento em 4 direções (Norte, Sul, Leste, Oeste)

## Como Executar

### Requisitos
- Python 3.6+
- Arquivo `grid_example.txt` no mesmo diretório

### Execução
```bash
python main.py
```

### Formato do Arquivo de Entrada
```
<linhas> <colunas>
<linha_1_do_grid>
<linha_2_do_grid>
...
<linha_n_do_grid>
```

### Exemplo de Saída Esperada
```
=== CENARIO 3: ROBO DE ARMAZEM ===
Algoritmo utilizado: Dijkstra
Motivo: Pesos nao-negativos e melhor aproveitamento da situacao do problema

Iniciando busca de (3, 0) para (3, 8)
Caminho encontrado com custo total: 16

=== RESULTADOS ===
Caminho encontrado de S(3, 0) para G(3, 8)
Custo total: 16

Detalhes do caminho (17 passos):
Passo 1: (3, 0) - Celula 'S' - Custo: 0
Passo 2: (4, 0) - Celula '.' - Custo: 1
...
```

## Estrutura do Código

### Classe `RobotPathfinder`
- `__init__(grid_file)`: Carrega o grid do arquivo
- `_load_grid()`: Lê arquivo e identifica S e G
- `_get_cell_cost()`: Retorna custo de uma célula
- `_get_neighbors()`: Retorna vizinhos válidos (4 direções)
- `find_shortest_path()`: Implementa Dijkstra
- `print_path_on_grid()`: Visualiza caminho no grid
- `print_detailed_path()`: Mostra detalhes do caminho

### Função `main()`
Executa a solução completa do cenário 3, tratando erros e exibindo resultados.

## Resultado Esperado com grid_example.txt

**Grid Original:**
```
~~~~~~~~.......
~~####~~~~~~...
~~#..#.~~~~....
S.#..#..G......
..#..####~~....
..#.........~~.
..######..~~...
......#.~~##...
..##..#..###...
............
```

**Caminho Encontrado (custo total: 16):**
- Início: S(3,0) 
- Fim: G(3,8)
- Passa por 12 células livres (custo 1 cada) + 1 piso difícil (custo 3) + objetivo (custo 1)
- Evita obstáculos (#) e minimiza passagem por piso difícil (~)