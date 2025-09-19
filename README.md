# 📌 Prática 1 - Grafos

Atividade prática da disciplina de **Grafos**, explorando algoritmos de caminho mínimo: **Dijkstra, Bellman-Ford e Floyd-Warshall**.  
A atividade será feita em dupla.

---
# Algoritmos de Caminho Mínimo em Grafos


## Algoritmo de Dijkstra

```
Algoritmo
início
   d11 ← 0; dij ← ∞ ∀ i ∈ V e V = {1};   [ origem-origem zero; distâncias infinitas a partir da origem ]
   A ← V; F ← ∅; anterior (i) ← 0 ∀ i;
   enquanto A ≠ ∅ fazer
      início
         r ← v ∈ V | dir = min{dij}
                        i∈A
              [ acha o vértice mais próximo da origem ]
         F ← F ∪ {r};  A ← A - {r};       [ o vértice r sai de Aberto para Fechado ]
         S ← A ∩ N⁺(r)                   [ S são os sucessores de r ainda abertos ]
         para todo i ∈ S fazer
            Início
               p ← min [dki-1, (dr + vri)]   [ compara o valor anterior com a nova soma ]
               se p < dki-1 então
                  início
                     dki ← p; anterior (i) ← r;   [ ganhou a nova distância ! ]
                  fim;
            fim;
      fim;
fim.
```

## Algoritmo de Bellman-Ford

```
Algoritmo
início
   d11 ← 0;  d1i ← ∞  ∀ i ∈ V – {1};  anterior(i) ← 0  ∀ i;
   enquanto ∃ (j,i) ∈ A | d1i > d1j + vji  fazer   [ varre todos os arcos aplicando o critério ]
      início
         d1i ← d1j + vji;  anterior(i) ← j;
      fim;
fim.
```
## Algoritmo de Floyd-Warshall

```
início <dados G = (V,E); matriz de valores V(G); matriz de roteamento R = [rij];
    R0 ← [ ]; D^0 = [dij] ← V(G);
    para k = 1, ..., n fazer    [ k é o vértice-base da iteração ]
        início
        para todo i, j = 1, ..., n fazer
            se dik + dkj < dij então
                início
                dij ← dik + dkj;
                rij ← rki;
                fim;
        fim;
    fim.
```

## 📂 Estrutura do Repositório

O repositório será organizado da seguinte forma:



```text
├── Cenario1/
│   ├── main.py
│   ├── graph1.txt
├── Cenario2/
│   ├── main.py
│   ├── graph2.txt
├── Cenario3/
│   ├── main.py
│   ├── grid_example.txt
└── README.md
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


👥 Autores

Jean Felipe Duarte Tenório

Alison Bruno Martires Soares

