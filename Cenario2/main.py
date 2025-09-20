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
    
    distancias = {v: float('inf') for v in vertices}
    anteriores = {v: None for v in vertices}
    distancias[origem] = 0
    
    #relaxamento das arestas
    for _ in range(len(vertices) - 1):
        atualizado = False
        for u in grafo:
            if distancias[u] != float('inf'):
                for v, peso in grafo[u]:
                    if distancias[u] + peso < distancias[v]:
                        distancias[v] = distancias[u] + peso
                        anteriores[v] = u
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

def reconstruir_caminho(anteriores, origem, destino):
    """
    Reconstrói o caminho mínimo usando o vetor de anteriores.
    """
    caminho = []
    atual = destino
    
    while atual is not None:
        caminho.append(atual)
        atual = anteriores[atual]
    
    caminho.reverse()
    
    #verifica se o caminho é válido (começa na origem)
    if caminho[0] == origem:
        return caminho
    else:
        return None  #não tem caminho

def ler_grafo(nome_arquivo):
    """
    Lê o grafo do arquivo de entrada.
    Formato: primeira linha = num_vertices num_arestas
             demais linhas = vertice_origem vertice_destino peso
    """
    grafo = {}
    
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linha = arquivo.readline().strip()
            num_vertices, num_arestas = map(int, linha.split())

            for _ in range(num_arestas):
                linha = arquivo.readline().strip()
                u, v, peso = map(int, linha.split())
                
                if u not in grafo:
                    grafo[u] = []
                grafo[u].append((v, peso))
    
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado!")
        return None
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return None
    
    return grafo

def calcular_custo_caminho(grafo, caminho):
    custo_total = 0
    
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        
        #procura a aresta
        encontrou = False
        for vizinho, peso in grafo.get(origem, []):
            if vizinho == destino:
                custo_total += peso
                encontrou = True
                break
        
        if not encontrou:
            print(f"Erro: Aresta {origem} -> {destino} não encontrada!")
            return None
    
    return custo_total

def resolver_cenario2():
    print("=== CENARIO 2: CARRO ELETRICO COM REGENERACAO ===")
    print("Algoritmo utilizado: Bellman-Ford")
    print("Motivo: Grafo direcionado com pesos negativos (regeneracao de energia)")
    print()
    
    #lê o grafo
    grafo = ler_grafo('graph2.txt')
    if grafo is None:
        return
    
    print("Grafo carregado:")
    for origem in sorted(grafo.keys()):
        for destino, peso in grafo[origem]:
            tipo_energia = "consumo" if peso > 0 else "regeneracao"
            print(f"  {origem} -> {destino}: {peso} Wh ({tipo_energia})")
    print()
    
    #chama o homem sino ford
    origem = 0
    destino = 6
    
    distancias, anteriores, tem_ciclo_negativo = bellman_ford(grafo, origem)
    
    if tem_ciclo_negativo:
        print("ATENCAO: Detectado ciclo negativo no grafo!")
        print("Isso significa que ha um ciclo que gera energia infinita.")
        return
    
    #verificação de caminho
    if distancias[destino] == float('inf'):
        print(f"Nao existe caminho do vertice {origem} para o vertice {destino}.")
        return
    
    #reconstroi o caminho
    caminho_minimo = reconstruir_caminho(anteriores, origem, destino)
    
    if caminho_minimo is None:
        print(f"Erro ao reconstruir o caminho do vertice {origem} para o vertice {destino}.")
        return
    
    #calcula o custo do caminho
    custo_total = calcular_custo_caminho(grafo, caminho_minimo)
    
    #printa os results
    print("RESULTADOS:")
    print(f"Caminho minimo (vertice 0 -> vertice 6): {' -> '.join(map(str, caminho_minimo))}")
    print(f"Energia liquida consumida: {custo_total} Wh")
    
    if custo_total < 0:
        print(f"  > O carro chegara com {abs(custo_total)} Wh a mais na bateria!")
    elif custo_total > 0:
        print(f"  > O carro consumira {custo_total} Wh da bateria.")
    else:
        print(f"  > O carro chegara com a mesma energia na bateria.")
    
    print()
    print("Detalhamento do caminho:")
    for i in range(len(caminho_minimo) - 1):
        u = caminho_minimo[i]
        v = caminho_minimo[i + 1]
        
        #encontra o peso da aresta
        peso = None
        for vizinho, p in grafo[u]:
            if vizinho == v:
                peso = p
                break
        
        tipo = "Consumo" if peso > 0 else "Regeneracao"
        print(f"  {u} -> {v}: {peso:+d} Wh ({tipo})")

#cria o graph2.txt (agilizar os processos de teste)
def criar_arquivo_exemplo():
    conteudo = """7	14
0	1	25
0	2	12
0	3	-8
1	4	-10
1	2	-6
1	5	-4
2	4	7
2	3	-5
2	5	6
3	4	9
3	5	11
4	6	8
4	5	2
5	6	5"""
    
    with open('graph2.txt', 'w') as arquivo:
        arquivo.write(conteudo)
    print("Arquivo 'graph2.txt' criado com os dados de exemplo.")

if __name__ == "__main__":
    #cria o arquivo de exemplo se não existir
    #se quiser testar com outro arquivo, só criar um graph2.txt e rodar
    import os
    if not os.path.exists('graph2.txt'):
        criar_arquivo_exemplo()
        print()
    
    chama a principal
    resolver_cenario2()
