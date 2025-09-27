
""" 
Algoritmo
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
"""

INF = float('inf') # ausência de aresta para conectar dois vértices

def carregar_grafo(nome_arquivo):
    """
    Lê o arquivo de entrada e cria a matriz de adjacências (distâncias)
    e a matriz de roteamento inicial.
    """
    try:
        with open(nome_arquivo, 'r') as f:
            # Lê a primeira linha para obter o número de vértices e arestas
            num_vertices, num_arestas = map(int, f.readline().split()) # lida com espaços em branco e tabs

            # Inicializa a matriz de distâncias (D) e de roteamento (R)
            distancias = [[INF] * num_vertices for _ in range(num_vertices)] # D^0 = [dij] ← V(G);
            roteamento = [[None] * num_vertices for _ in range(num_vertices)] # R^0 ← rᵢⱼ ← j ;

            for i in range(num_vertices):
                distancias[i][i] = 0 # Distância para si mesmo é zero
                roteamento[i][i] = i + 1 # Rota para si mesmo é o próprio vértice 

            # Preenche as matrizes com os dados das arestas
            for i in range(num_arestas): 
                linha = f.readline().strip()
                v1, v2, custo = map(int, linha.split())
                idx1, idx2 = v1 - 1, v2 - 1

                # Grafo não-direcionado
                distancias[idx1][idx2] = custo
                roteamento[idx1][idx2] = v2

                distancias[idx2][idx1] = custo
                roteamento[idx2][idx1] = v1
            
        return num_vertices, distancias, roteamento
        
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return None, None, None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None, None, None

def floyd_warshall(num_vertices, distancias, roteamento):
    """
    Aplica o algoritmo de Floyd-Warshall, atualizando tanto a matriz de 
    distâncias quanto a de roteamento.
    """
    dist = [list(row) for row in distancias] # D^0 = [dij] ← V(G);
    rot = [list(row) for row in roteamento] # R^0 ← rᵢⱼ ← j ;

    for k in range(num_vertices): # para k = 1, ..., n fazer    [ k é o vértice-base da iteração ]
        for i in range(num_vertices): # para todo i, j = 1, ..., n fazer
            for j in range(num_vertices): # para todo i, j = 1, ..., n fazer
                if dist[i][k] + dist[k][j] < dist[i][j]: # se dik + dkj < dij então
                    dist[i][j] = dist[i][k] + dist[k][j] # dij ← dik + dkj;
                    rot[i][j] = rot[i][k] # rij ← rik;
    return dist, rot 

def reconstruir_caminho(origem, destino, roteamento):
    """
    Usa a matriz de roteamento para encontrar o caminho completo entre dois vértices.
    """
    idx_origem, idx_destino = origem - 1, destino - 1
    
    if roteamento[idx_origem][idx_destino] is None:
        return []

    caminho = [origem]
    atual = origem
    while atual != destino:
        proximo_passo = roteamento[atual - 1][destino - 1]
        caminho.append(proximo_passo)
        atual = proximo_passo
        
    return caminho


def analisar_resultados(num_vertices, matriz_distancias):
    """
    Analisa a matriz de distâncias para encontrar a estação central,
    usando o menor somatório como critério principal e a menor
    distância máxima como desempate.
    """
    menor_soma = INF
    melhor_dist_max = INF
    estacao_central = None

    for i in range(num_vertices):
        soma_distancias_atual = sum(matriz_distancias[i])
        dist_max_atual = max(matriz_distancias[i])

        if soma_distancias_atual < menor_soma:
            menor_soma = soma_distancias_atual
            melhor_dist_max = dist_max_atual
            estacao_central = i
        elif soma_distancias_atual == menor_soma:
            if dist_max_atual < melhor_dist_max:
                melhor_dist_max = dist_max_atual
                estacao_central = i

    if estacao_central is None:
        return None, [], None, INF

    estacao_central_final = estacao_central + 1
    vetor_distancias = matriz_distancias[estacao_central]
    distancia_maxima = max(vetor_distancias)
    vertice_mais_distante = vetor_distancias.index(distancia_maxima) + 1

    return estacao_central_final, vetor_distancias, vertice_mais_distante, distancia_maxima

def formatar_matriz_para_impressao(matriz, titulo):
    """Impressão simples e alinhada da matriz de distâncias."""
    if not matriz or not matriz[0]:
        return f"\n{titulo}:\n<matriz vazia>\n"

    n = len(matriz)
    colunas = " " * 4 + " ".join(f"{i+1:>4}" for i in range(n))
    linhas = [f"\n{titulo}:", colunas]
    for i, linha in enumerate(matriz):
        itens = [ "inf" if item == INF else str(int(item)) for item in linha ]
        linhas.append(f"{i+1:2} " + " ".join(f"{it:>4}" for it in itens))
    return "\n".join(linhas) + "\n"

if __name__ == "__main__":
    nome_arquivo = "graph1.txt"
    
    num_vertices, dist_inicial, rot_inicial = carregar_grafo(nome_arquivo)

    if num_vertices:
        matriz_distancias, matriz_roteamento = floyd_warshall(num_vertices, dist_inicial, rot_inicial)
        
        central, vetor, mais_distante, dist_max = analisar_resultados(num_vertices, matriz_distancias)


        print(f"\n1. Estação Central Escolhida: {central}")
        
        print(f"\n2. Vetor de distâncias da estação {central} aos demais vértices:")
        print(f"   {vetor}")

        print(f"\n3. Vértice mais distante da estação central (e sua distância):")
        print(f"   Vértice: {mais_distante}\tDistância: {dist_max}")

        print(formatar_matriz_para_impressao(matriz_distancias, "\n4. Matriz de distâncias mínimas entre todos os pares"))
        print(formatar_matriz_para_impressao(matriz_roteamento, "\n5. Matriz de Roteamento"))
