# Cenário 3: Robô de Armazém com Obstáculos

## Algoritmo Escolhido: Dijkstra

### Por que Dijkstra?
- **Pesos não-negativos**: Todos os custos são ≥ 0 (célula livre = 1, piso difícil = 3)
- **Melhor aproveitamento da situação do problema**: Dijkstra é ideal para grafos com pesos positivos
- **Garantia de otimalidade**: Encontra o caminho mínimo global
- **Eficiência**: O(V log V + E) onde V = células e E = conexões entre células

### Comparação com o Pseudocódigo da Aula

**Pseudocódigo Ideal Geral:**
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

**Pseudocódigo Livro Grafos Introdução e Prática:**
```
Algoritmo (Pseudocódigo Clássico do Dijkstra Do livro de Grafos: Introdução e Prática de  Paulo Oswaldo Boaventura Netto (Editora Blucher))
início
    d₁₁ ← 0; d₁ᵢ ← ∞ ∀ i ∈ V - {1};  < distância origem-origem zero; distâncias a partir da origem infinitas >
    A ← V; F ← ∅; anterior (i) ← 0 ∀ i;
    enquanto A ≠ ∅ fazer
        início
            r ← v ∈ V | d₁ᵣ = min[d₁ⱼ]      < acha o vértice mais próximo da origem >
                              i∈A
            F ← F ∪ {r}; A ← A - {r};      < o vértice r sai de Aberto para Fechado >
            S ← A ∩ N⁺(r)                   < S são os sucessores de r ainda abertos >
            para todo i ∈ S fazer
                início
                    p ← min [d₁ᵢᵏ⁻¹, (d₁ᵣ + vᵣᵢ)]  < compara o valor anterior com a nova soma >
                    se p < d₁ᵢᵏ⁻¹ então
                        início
                            d₁ᵢᵏ ← p; anterior (i) ← r;  < ganhou a nova distância ! >
                        fim;
                fim;
        fim;
fim.
```

**Implementação no Código (main.py):**

```python
   def _get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Retorna vizinhos válidos de uma posicao (movimento em 4 direcões: N,S,L,O).
        
        Args:
            pos: Tupla (row, col) da posicao atual
            
        Returns:
            Lista de posicões vizinhas válidas
        """
        row, col = pos
        #movimento em 4 direcões: Norte, Sul, Leste, Oeste
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        neighbors = []
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            #verifica limites do grid
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                # Verifica se nao e obstáculo
                if self.grid[new_row][new_col] != '#':
                    neighbors.append((new_row, new_col))
        
        return neighbors
    
    def find_shortest_path(self) -> Tuple[Optional[List[Tuple[int, int]]], int]:
        """
        Segue o pseudocódigo:
        1. Inicializa distâncias (INITIALIZE-SINGLE-SOURCE)
        2. Usa priority queue para extrair vertice com menor distância (EXTRACT-MIN)
        3. Para cada vizinho, tenta relaxar a aresta (RELAX)
        
        Returns:
            Tupla contendo (caminho_como_lista_de_coordenadas, custo_total)
            Retorna (None, -1) se nao houver caminho
        """
        #INITIALIZE-SINGLE-SOURCE
        distances = {} # d₁ᵢ (dicionário de distâncias)
        predecessors = {} # anterior(i)
        visited = set() # F (conjunto de vértices fechados)
        
        #inicializa todas as posicões com distância infinita # d₁ᵢ ← ∞ ∀ i ∈ V
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] != '#':  # nao acessa obstáculos
                    distances[(i, j)] = float('inf')
                    predecessors[(i, j)] = None
        
        # distância da origem para si mesma e zero # d₁₁ ← 0
        distances[self.start] = 0
        
        # Priority queue (heap) - equivale ao conjunto Q no pseudocódigo (usei heap para melhorar eficiência, LEMBRAR DE PERGUNTAR AO PROFESSOR)
        #ordenar por distancia
        pq = [(0, self.start)] # A ← V (conjunto de vértices abertos)
        
        print(f"Iniciando busca de {self.start} para {self.goal}")
        
        #loop principal do Dijkstra 
        while pq:  #while Q ≠ ∅ ou A ≠ ∅
                   

            # EXTRACT-MIN(Q):extrai vertice com menor distância
            current_dist, current_pos = heapq.heappop(pq) # r ← v ∈ V | d₁ᵣ = min[d₁ⱼ]
            
            #se já visitamos esta posicao, pula (pode ter repeticao)
            if current_pos in visited:
                continue
            
            #S = S ∪ {u}:adiciona ao conjunto de vertices visitados
            visited.add(current_pos) # F ← F ∪ {r}; A ← A - {r};
            
            #se chegamos ao objetivo, podemos parar
            if current_pos == self.goal:
                break
            # S ← A ∩ N⁺(r)  (vizinhos ainda não visitados)
            # para todo i ∈ S fazer
            #para cada vizinho do vertice atual
            for neighbor_pos in self._get_neighbors(current_pos):
                if neighbor_pos in visited:
                    continue
                
                # p ← min[d₁ᵢᵏ⁻¹, (d₁ᵣ + vᵣᵢ)]
                #calcula nova distância atraves do caminho atual
                edge_weight = self._get_cell_cost(neighbor_pos[0], neighbor_pos[1])
                new_distance = current_dist + edge_weight
                
                 # se p < d₁ᵢᵏ⁻¹ então
                #RELAX(u, v, w): relaxamento da aresta
                if new_distance < distances[neighbor_pos]:
                    # d₁ᵢᵏ ← p; anterior(i) ← r
                    distances[neighbor_pos] = new_distance
                    predecessors[neighbor_pos] = current_pos
                    heapq.heappush(pq, (new_distance, neighbor_pos))
        
        #reconstrói o caminho usando os predecessores
        if self.goal not in distances or distances[self.goal] == float('inf'):
            print("Nao foi possivel encontrar caminho para o objetivo!")
            return None, -1
        
        #reconstrói caminho do objetivo ate a origem
        path = []
        current = self.goal
        
        while current is not None:
            path.append(current)
            current = predecessors[current]
        
        #inverte o caminho para melhorear print
        path.reverse()
        
        total_cost = distances[self.goal]
        
        print(f"Caminho encontrado com custo total: {total_cost}")
        return path, int(total_cost)
```

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