# 📌 Prática 1 - Grafos

Atividade prática da disciplina de **Grafos**, explorando algoritmos de caminho mínimo: **Dijkstra, Bellman-Ford e Floyd-Warshall**.  
A atividade será feita em dupla.

---

## 📂 Estrutura do Repositório

O repositório será organizado da seguinte forma:

├── Cenario1/
│ ├── main.py
│ ├── graph1.txt
├── Cenario2/
│ ├── main.py
│ ├── graph2.txt
├── Cenario3/
│ ├── main.py
│ ├── grid_example.txt


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

