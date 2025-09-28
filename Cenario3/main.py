import heapq
from typing import List, Tuple, Optional
class RobotPathfinder:
    """
    Baseado no pseudocódigo do Dijkstra:
    
    Pseucódigo do Dijkstra Ideal Geral:
    DIJKSTRA(G, w, s):
    1. INITIALIZE-SINGLE-SOURCE(G, s)
    2. S = ∅
    3. Q = G.V
    4. while Q ≠ ∅:
    5.    u = EXTRACT-MIN(Q)
    6.    S = S U {u}
    7.    for each vertex v ∈ G.Adj[u]:
    8.       RELAX(u, v, w)
    """
    """
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
"""
    
    def __init__(self, grid_file: str):
        """
        Inicializa o pathfinder carregando o grid do arquivo.
        
        Args:
            grid_file: Caminho para o arquivo contendo o grid
        """
        self.grid = []
        self.rows = 0
        self.cols = 0
        self.start = None
        self.goal = None
        self._load_grid(grid_file)
    
    def _load_grid(self, grid_file: str) -> None:
        """
        Carrega o grid do arquivo e identifica posicões de inicio e objetivo.
        
        Args:
            grid_file: Caminho para o arquivo do grid
        """
        with open(grid_file, 'r') as f:
            lines = f.readlines()
        
        #primeira linha contem dimensões
        self.rows, self.cols = map(int, lines[0].strip().split())
        
        #carrega o grid e encontra posicões especiais
        for i in range(1, self.rows + 1):
            row = lines[i].strip()
            self.grid.append(list(row))
            
            for j, cell in enumerate(row):
                if cell == 'S':
                    self.start = (i-1, j)  #indice
                elif cell == 'G':
                    self.goal = (i-1, j)
        
        if not self.start or not self.goal:
            raise ValueError("Grid deve conter exatamente um 'S' (start) e um 'G' (goal)")
    
    def _get_cell_cost(self, row: int, col: int) -> int:
        """
        Retorna o custo de movimento para uma celula especifica.
        
        Args:
            row, col: Coordenadas da celula
            
        Returns:
            Custo de movimento (1 para '.', 3 para '~', infinito para '#')
        """
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return float('inf')  #foora dos limites
        
        cell = self.grid[row][col]
        
        #mapeamento de custos conforme especificacao
        cost_map = {
            '.': 1,      #celula livre
            '~': 3,      #piso dificil
            'S': 1,      #inicio (tratado como celula livre)
            'G': 1,      #objetivo (tratado como celula livre)
            '#': float('inf')  #obstáculo intransponivel
        }
        
        return cost_map.get(cell, float('inf'))
    
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
    
    def print_path_on_grid(self, path: List[Tuple[int, int]]) -> None:
        """
        Imprime o grid mostrando o caminho encontrado.
        
        Args:
            path: Lista de coordenadas representando o caminho
        """
        if not path:
            print("Nenhum caminho para exibir.")
            return
        
        #dria cópia do grid para visualizacao
        display_grid = [row[:] for row in self.grid]
        
        #marca o caminho
        for i, (row, col) in enumerate(path):
            if (row, col) != self.start and (row, col) != self.goal:
                display_grid[row][col] = '*'
        
        print("\nGrid com caminho marcado (* indica o caminho):")
        print(f"Dimensoes: {self.rows}x{self.cols}")
        for row in display_grid:
            print(''.join(row))
        
        print(f"\nLegenda:")
        print("S = Inicio, G = Objetivo, * = Caminho")
        print(". = Celula livre (custo 1)")
        print("~ = Piso dificil (custo 3)")
        print("# = Obstaculo (não pode entrar)")
    
    def print_detailed_path(self, path: List[Tuple[int, int]]) -> None:
        """
        Imprime detalhes do caminho encontrado.
        
        Args:
            path: Lista de coordenadas representando o caminho
        """
        if not path:
            return
        
        print(f"\nDetalhes do caminho ({len(path)} passos):")
        total_cost = 0
        
        for i, (row, col) in enumerate(path):
            cell = self.grid[row][col]
            if cell in ['S', 'G']:
                cost = 1
            else:
                cost = self._get_cell_cost(row, col)
            
            if i > 0:  #nao conta custo da posicao inicial (dava errado por isso)
                total_cost += cost
            
            print(f"Passo {i+1}: ({row}, {col}) - Celula '{cell}' - Custo: {cost if i > 0 else 0}")
        
        print(f"\nCusto total do caminho: {total_cost}")


def main():
    """
    Funcao principal que executa a solucao do cenário 3.
    """
    try:
        #pega o arquivo
        pathfinder = RobotPathfinder('grid_example.txt')
        
        print("=== CENARIO 3: ROBO DE ARMAZEM ===")
        print("Algoritmo utilizado: Dijkstra")
        print("Motivo: Pesos nao-negativos e melhor aproveitamento da situacao do problema\n")
        
        #encontra o caminho minimo(o resto acontece nas outras funcões dentro do objeto)
        path, total_cost = pathfinder.find_shortest_path()
        
        if path:
            print(f"\n=== RESULTADOS ===")
            print(f"Caminho encontrado de S{pathfinder.start} para G{pathfinder.goal}")
            print(f"Custo total: {total_cost}")
            
            #printa detalhes do caminho
            pathfinder.print_detailed_path(path)
            
            #printa o caminho marcado do grid (mais fácil do que pareceu que ia ser)
            pathfinder.print_path_on_grid(path)
            
            #printa as coordenadas do caminho
            print(f"\nCoordenadas do caminho:")
            for i, pos in enumerate(path):
                print(f"  {i+1}: {pos}")
        
        else:
            print("Nao foi possivel encontrar um caminho válido!")
    
    except FileNotFoundError:
        print("Erro: Arquivo 'grid_example.txt' nao encontrado.")
    except Exception as e:
        print(f"Deu ruim: {e}")


if __name__ == "__main__":
    main()