# 📌 Prática 1 - Grafos

Atividade prática da disciplina de **Grafos**, explorando algoritmos de caminho mínimo: **Dijkstra, Bellman-Ford e Floyd-Warshall**.  
A atividade será feita em dupla.

---
# Algoritmos de Caminho Mínimo em Grafos


## Algoritmo de Dijkstra

```
Algoritmo
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

## Algoritmo de Bellman-Ford

```
Algoritmo
início
    d₁₁ ← 0; d₁ᵢ ← ∞ ∀ i ∈ V - {1}; anterior (i) ← 0 ∀ i;
    enquanto ∃ (j,i) ∈ A | d₁ᵢ > d₁ⱼ + vⱼᵢ fazer  < varre todos os arcos aplicando o critério >
        início
            d₁ᵢ ← d₁ⱼ + vⱼᵢ; anterior (i) ← j;
        fim;
fim.
```
## Algoritmo de Floyd-Warshall

```
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
```

## 📂 Estrutura do Repositório

O repositório será organizado da seguinte forma:



```text
|── Grafos_Caminho_Minimo_Lista/
├── Cenario1/
│   ├── main.py
│   ├── graph.png
│   ├── graph1.txt
│   ├── README.md
├── Cenario2/
│   ├── main.py
│   ├── graph2.txt 
│   ├── graph2.png
│   ├── README.md
├── Cenario3/
│   ├── main.py
│   ├── grid_example.txt
│   ├── README.md
├── README.md
```

## 📘 Cenário 1: Determinando a estação central

- **Descrição:** dado um grafo não-direcionado com pesos representando pontos e conexões de metrô, precisamos determinar qual vértice pode ser considerado a estação central.  
- **Entrada:** arquivo `graph1.txt` contendo número de vértices, número de arestas e lista de arestas com custos.  
- **Saída esperada:**  
  - Estação central escolhida.  
  - Vetor com distâncias até os demais vértices.  
  - Vértice mais distante e valor da distância.  
  - Matriz de distâncias entre todos os vértices.  

---

## 📘 Cenário 2: Otimizando caminho com regeneração

- **Descrição:** grafo direcionado representando ruas onde pesos positivos correspondem a consumo de energia e pesos negativos à regeneração.  
- **Entrada:** arquivo `graph2.txt` no mesmo formato do cenário anterior.  
- **Saída esperada:**  
  - Caminho mínimo do vértice `0` até o vértice `6`.  
  - Somatório do custo do caminho.  

---

## 📘 Cenário 3: Robô de armazém com obstáculos

- **Descrição:** dado um grid representando o mapa de um armazém, encontrar o menor caminho de custo do ponto de recarga `S` até a estação de coleta `G`.  
- **Regras do grid:**  
  - `=` célula livre (custo 1)  
  - `#` obstáculo (intransponível)  
  - `~` piso difícil (custo 3)  
  - `S` ponto inicial  
  - `G` objetivo  
  - Movimentos permitidos: 4 direções (N, S, L, O)  

- **Entrada:** arquivo `grid_example.txt` contendo dimensões e mapa do armazém.  
- **Saída esperada:**  
  - Caminho mínimo encontrado.  
  - Custo total do percurso.  

---

## ⚙️ Instruções de Uso

1. Clone este repositório:  
   ```bash
   git clone https://github.com/jfdt10/Grafos_Caminho_Minimo_Lista

2. Para executar cada cenário:
   ```bash
   cd Cenario1
   python main.py
   ```

   ```bash
   cd Cenario2
   python main.py
   ```

   ```bash
   cd Cenario3
   python main.py
   ```

-----------------------------------------

👥 Autores

Jean Felipe Duarte Tenório

Alison Bruno Martires Soares

