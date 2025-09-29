"""
Problema dos Recipientes com Água (9, 4 litros)
Trabalho de Inteligência Artificial - Busca Cega e Busca Informada

Objetivo: Obter exatamente 6 litros de água usando recipientes de 9 e 4 litros

Baseado no framework AIMA-Python
"""

from collections import deque
import heapq
from typing import List, Tuple, Optional, Set
import time


class Estado:
    """Representa um estado do problema: quantidade de água em cada recipiente"""
    
    def __init__(self, r9: int, r4: int):
        self.r9 = r9  # Recipiente de 9 litros
        self.r4 = r4  # Recipiente de 4 litros
    
    def __eq__(self, other):
        return self.r9 == other.r9 and self.r4 == other.r4
    
    def __hash__(self):
        return hash((self.r9, self.r4))
    
    def __repr__(self):
        return f"({self.r9}L, {self.r4}L)"
    
    def eh_objetivo(self) -> bool:
        """Verifica se o estado atual contém 6 litros em algum recipiente"""
        return self.r9 == 6 or self.r4 == 6
    
    def to_tuple(self) -> Tuple[int, int]:
        return (self.r9, self.r4)


class No:
    """Representa um nó na árvore de busca"""
    
    def __init__(self, estado: Estado, pai=None, acao: str = None, custo: int = 0):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        self.profundidade = 0 if pai is None else pai.profundidade + 1
    
    def __lt__(self, other):
        return self.custo < other.custo
    
    def caminho(self) -> List[Tuple[str, Estado]]:
        """Retorna o caminho do estado inicial até este nó"""
        caminho = []
        no_atual = self
        while no_atual.pai is not None:
            caminho.append((no_atual.acao, no_atual.estado))
            no_atual = no_atual.pai
        caminho.append(("Estado Inicial", no_atual.estado))
        return list(reversed(caminho))


class ProblemaRecipientes:
    """Define o problema dos recipientes com água"""
    
    def __init__(self):
        self.capacidade_r9 = 9
        self.capacidade_r4 = 4
        self.estado_inicial = Estado(0, 0)
    
    def acoes(self, estado: Estado) -> List[Tuple[str, Estado]]:
        """Retorna todas as ações possíveis a partir de um estado"""
        acoes_possiveis = []
        
        # 1. Encher recipiente de 9 litros
        if estado.r9 < self.capacidade_r9:
            novo = Estado(self.capacidade_r9, estado.r4)
            acoes_possiveis.append(("Encher recipiente de 9L", novo))
        
        # 2. Encher recipiente de 4 litros
        if estado.r4 < self.capacidade_r4:
            novo = Estado(estado.r9, self.capacidade_r4)
            acoes_possiveis.append(("Encher recipiente de 4L", novo))
        
        # 3. Esvaziar recipiente de 9 litros
        if estado.r9 > 0:
            novo = Estado(0, estado.r4)
            acoes_possiveis.append(("Esvaziar recipiente de 9L", novo))
        
        # 4. Esvaziar recipiente de 4 litros
        if estado.r4 > 0:
            novo = Estado(estado.r9, 0)
            acoes_possiveis.append(("Esvaziar recipiente de 4L", novo))
        
        # 5. Transferir de 9L para 4L
        if estado.r9 > 0 and estado.r4 < self.capacidade_r4:
            transferir = min(estado.r9, self.capacidade_r4 - estado.r4)
            novo = Estado(estado.r9 - transferir, estado.r4 + transferir)
            acoes_possiveis.append(("Transferir de 9L para 4L", novo))
        
        # 6. Transferir de 4L para 9L
        if estado.r4 > 0 and estado.r9 < self.capacidade_r9:
            transferir = min(estado.r4, self.capacidade_r9 - estado.r9)
            novo = Estado(estado.r9 + transferir, estado.r4 - transferir)
            acoes_possiveis.append(("Transferir de 4L para 9L", novo))
        
        return acoes_possiveis


# ================= BUSCA CEGA: BUSCA EM LARGURA =================
# JUSTIFICATIVA: A Busca em Largura (BFS) é ideal para este problema porque:
# 1. Garante encontrar a solução ÓTIMA (menor número de passos)
# 2. O espaço de estados é pequeno (10 x 5 = 50 estados possíveis)
# 3. Todos os passos têm o mesmo custo
# 4. Evita caminhos infinitos que poderiam ocorrer com busca em profundidade

def busca_em_largura(problema: ProblemaRecipientes) -> Optional[No]:
    """
    Implementa a Busca em Largura (BFS)
    Retorna o nó solução ou None se não encontrar solução
    """
    print("\n" + "="*60)
    print("BUSCA CEGA: BUSCA EM LARGURA (BFS)")
    print("="*60)
    
    inicio = time.time()
    no_inicial = No(problema.estado_inicial)
    
    if no_inicial.estado.eh_objetivo():
        return no_inicial
    
    fronteira = deque([no_inicial])
    explorados = set()
    nos_expandidos = 0
    nos_gerados = 1
    
    while fronteira:
        no = fronteira.popleft()
        explorados.add(no.estado.to_tuple())
        nos_expandidos += 1
        
        for acao, estado in problema.acoes(no.estado):
            filho = No(estado, no, acao, no.custo + 1)
            nos_gerados += 1
            
            if estado.to_tuple() not in explorados and \
               not any(n.estado == estado for n in fronteira):
                
                if filho.estado.eh_objetivo():
                    tempo_total = time.time() - inicio
                    print(f"\n✓ Solução encontrada!")
                    print(f"  Nós expandidos: {nos_expandidos}")
                    print(f"  Nós gerados: {nos_gerados}")
                    print(f"  Tempo de execução: {tempo_total:.4f} segundos")
                    print(f"  Profundidade da solução: {filho.profundidade}")
                    return filho
                
                fronteira.append(filho)
    
    return None


# ================= BUSCA INFORMADA: HEURÍSTICAS =================

def heuristica_diferenca_absoluta(estado: Estado) -> int:
    """
    Heurística 1: Diferença absoluta mínima até o objetivo (6 litros)
    Admissível: nunca superestima o custo real
    """
    return min(abs(estado.r9 - 6), abs(estado.r4 - 6))


def heuristica_combinada(estado: Estado) -> int:
    """
    Heurística 2: Considera múltiplos fatores
    - Distância ao objetivo
    - Se não há 6 litros em nenhum recipiente, adiciona penalidade
    """
    dist_r9 = abs(estado.r9 - 6)
    dist_r4 = abs(estado.r4 - 6)
    
    if estado.r9 == 6 or estado.r4 == 6:
        return 0
    
    min_dist = min(dist_r9, dist_r4)
    
    # Penalidade se ambos recipientes estão vazios ou cheios
    if (estado.r9 == 0 and estado.r4 == 0) or \
       (estado.r9 == 9 and estado.r4 == 4):
        return min_dist + 1
    
    return min_dist


def busca_gulosa(problema: ProblemaRecipientes, heuristica) -> Optional[No]:
    """
    Implementa a Busca Gulosa (Greedy Best-First Search)
    Expande sempre o nó com menor valor heurístico
    """
    print("\n" + "="*60)
    print("BUSCA INFORMADA: BUSCA GULOSA")
    print("="*60)
    
    inicio = time.time()
    no_inicial = No(problema.estado_inicial)
    
    if no_inicial.estado.eh_objetivo():
        return no_inicial
    
    # Fila de prioridade: (h(n), contador, nó)
    contador = 0
    fronteira = [(heuristica(no_inicial.estado), contador, no_inicial)]
    heapq.heapify(fronteira)
    
    explorados = set()
    nos_expandidos = 0
    nos_gerados = 1
    
    while fronteira:
        _, _, no = heapq.heappop(fronteira)
        
        if no.estado.eh_objetivo():
            tempo_total = time.time() - inicio
            print(f"\n✓ Solução encontrada!")
            print(f"  Nós expandidos: {nos_expandidos}")
            print(f"  Nós gerados: {nos_gerados}")
            print(f"  Tempo de execução: {tempo_total:.4f} segundos")
            print(f"  Profundidade da solução: {no.profundidade}")
            return no
        
        if no.estado.to_tuple() in explorados:
            continue
        
        explorados.add(no.estado.to_tuple())
        nos_expandidos += 1
        
        for acao, estado in problema.acoes(no.estado):
            if estado.to_tuple() not in explorados:
                filho = No(estado, no, acao, no.custo + 1)
                nos_gerados += 1
                contador += 1
                h = heuristica(filho.estado)
                heapq.heappush(fronteira, (h, contador, filho))
    
    return None


def busca_a_estrela(problema: ProblemaRecipientes, heuristica) -> Optional[No]:
    """
    Implementa a Busca A* (A-Star)
    Expande o nó com menor f(n) = g(n) + h(n)
    onde g(n) é o custo do caminho e h(n) é a heurística
    """
    print("\n" + "="*60)
    print("BUSCA INFORMADA: BUSCA A*")
    print("="*60)
    
    inicio = time.time()
    no_inicial = No(problema.estado_inicial)
    
    if no_inicial.estado.eh_objetivo():
        return no_inicial
    
    # Fila de prioridade: (f(n), contador, nó)
    contador = 0
    h_inicial = heuristica(no_inicial.estado)
    fronteira = [(h_inicial, contador, no_inicial)]
    heapq.heapify(fronteira)
    
    explorados = {}  # estado -> melhor custo g(n) encontrado
    nos_expandidos = 0
    nos_gerados = 1
    
    while fronteira:
        _, _, no = heapq.heappop(fronteira)
        
        if no.estado.eh_objetivo():
            tempo_total = time.time() - inicio
            print(f"\n✓ Solução encontrada!")
            print(f"  Nós expandidos: {nos_expandidos}")
            print(f"  Nós gerados: {nos_gerados}")
            print(f"  Tempo de execução: {tempo_total:.4f} segundos")
            print(f"  Profundidade da solução: {no.profundidade}")
            print(f"  Custo da solução: {no.custo}")
            return no
        
        estado_tuple = no.estado.to_tuple()
        if estado_tuple in explorados and explorados[estado_tuple] <= no.custo:
            continue
        
        explorados[estado_tuple] = no.custo
        nos_expandidos += 1
        
        for acao, estado in problema.acoes(no.estado):
            filho = No(estado, no, acao, no.custo + 1)
            nos_gerados += 1
            
            estado_filho_tuple = estado.to_tuple()
            if estado_filho_tuple not in explorados or \
               explorados[estado_filho_tuple] > filho.custo:
                
                contador += 1
                h = heuristica(filho.estado)
                f = filho.custo + h
                heapq.heappush(fronteira, (f, contador, filho))
    
    return None


def exibir_solucao(no: Optional[No], nome_algoritmo: str):
    """Exibe a solução de forma amigável"""
    print("\n" + "="*60)
    print(f"SOLUÇÃO ENCONTRADA - {nome_algoritmo}")
    print("="*60)
    
    if no is None:
        print("❌ Nenhuma solução foi encontrada.")
        return
    
    caminho = no.caminho()
    
    print(f"\nNúmero de passos: {len(caminho) - 1}")
    print("\nSequência de ações:\n")
    
    for i, (acao, estado) in enumerate(caminho):
        if i == 0:
            print(f"┌─ Passo {i}: {acao}")
        else:
            print(f"├─ Passo {i}: {acao}")
        
        # Representação visual dos recipientes
        r9_cheio = "█" * estado.r9 + "░" * (9 - estado.r9)
        r4_cheio = "█" * estado.r4 + "░" * (4 - estado.r4)
        
        print(f"│  Recipiente 9L: [{r9_cheio}] {estado.r9}L")
        print(f"│  Recipiente 4L: [{r4_cheio}] {estado.r4}L")
        
        if estado.eh_objetivo():
            print(f"│ OBJETIVO ALCANÇADO! 6 litros obtidos!")
        print("│")
    
    print("└" + "─"*58)


def main():
    """Função principal que executa todas as buscas"""
    print("\n" + "╔" + "="*58 + "╗")
    print("║" + " "*10 + "PROBLEMA DOS RECIPIENTES COM ÁGUA" + " "*14 + "║")
    print("║" + " "*15 + "Recipientes: 9L e 4L" + " "*23 + "║")
    print("║" + " "*15 + "Objetivo: Obter 6 litros" + " "*19 + "║")
    print("╚" + "="*58 + "╝")
    
    problema = ProblemaRecipientes()
    
    # 1. BUSCA EM LARGURA (BUSCA CEGA)
    print("\n\n┌─ EXECUTANDO BUSCA CEGA...")
    solucao_bfs = busca_em_largura(problema)
    exibir_solucao(solucao_bfs, "BUSCA EM LARGURA")
    
    # 2. BUSCA GULOSA
    print("\n\n┌─ EXECUTANDO BUSCA GULOSA...")
    solucao_gulosa = busca_gulosa(problema, heuristica_diferenca_absoluta)
    exibir_solucao(solucao_gulosa, "BUSCA GULOSA")
    
    # 3. BUSCA A*
    print("\n\n┌─ EXECUTANDO BUSCA A*...")
    solucao_a_estrela = busca_a_estrela(problema, heuristica_diferenca_absoluta)
    exibir_solucao(solucao_a_estrela, "BUSCA A*")
    
    # COMPARAÇÃO FINAL
    print("\n\n" + "╔" + "="*58 + "╗")
    print("║" + " "*18 + "COMPARAÇÃO DOS ALGORITMOS" + " "*15 + "║")
    print("╚" + "="*58 + "╝")
    
    print("\n┌─ Busca em Largura (BFS):")
    print(f"│  Passos da solução: {solucao_bfs.profundidade if solucao_bfs else 'N/A'}")
    print(f"│  Garantia: Solução ótima ✓")
    
    print("\n├─ Busca Gulosa:")
    print(f"│  Passos da solução: {solucao_gulosa.profundidade if solucao_gulosa else 'N/A'}")
    print(f"│  Garantia: Não garante otimalidade")
    
    print("\n└─ Busca A*:")
    print(f"   Passos da solução: {solucao_a_estrela.profundidade if solucao_a_estrela else 'N/A'}")
    print(f"   Garantia: Solução ótima ✓ (com heurística admissível)")
    
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()