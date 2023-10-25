import numpy as np
import math

# Função para encontrar o conjunto de um elemento i
def encontrar(conjunto, i):
    if conjunto[i] == i:
        return i
    return encontrar(conjunto, conjunto[i])

# Função para unir dois C u e v
def unir(conjunto, rank, u, v):
    u_raiz = encontrar(conjunto, u)
    v_raiz = encontrar(conjunto, v)
    
    # Anexar a árvore menor à raiz da árvore maior (união por rank)
    if rank[u_raiz] < rank[v_raiz]:
        conjunto[u_raiz] = v_raiz
    elif rank[u_raiz] > rank[v_raiz]:
        conjunto[v_raiz] = u_raiz
    else:
        # Se as classificações são iguais, faça um nó como raiz e incremente sua classificação em um
        conjunto[v_raiz] = u_raiz
        rank[u_raiz] += 1

def kruskal(matriz):
        
        V = list(range(np.shape(matriz)[0])) # lista de vértices
        T = [] # lista de Es da árvore geradora mínima
        A = [] # lista de Es do grafo
        
        for i in range(np.shape(matriz)[0]):
            for j in range(np.shape(matriz)[0]):
                if matriz[i][j] > 0:
                    A.append((i,j,matriz[i][j]))
                    
        A.sort(key = lambda x: x[2])
        
        # Cria V C disjuntos com elementos únicos
        C = [i for i in range(len(V))]
        rank = [0 for i in range(len(V))]
        
        while len(T) < len(V)-1:
            E = A.pop(0)
            u = E[0]
            v = E[1]
            
            u_conjunto = encontrar(C, u)
            v_conjunto = encontrar(C, v)
            
            # Se incluir esta E não causar um ciclo, inclua-a no resultado e marque o peso.
            if u_conjunto != v_conjunto:
                T.append((u,v))
                unir(C, rank, u_conjunto, v_conjunto)
                
        custo = 0
        for par in T:
            custo += matriz[par[0]][par[1]]
            
        print(T, custo)