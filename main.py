from aima3.search import breadth_first_tree_search, greedy_best_first_graph_search, astar_search, \
    depth_first_tree_search, iterative_deepening_search, depth_limited_search

from entities.water_recipients_problem import WaterRecipientsProblem
from helpers.interface_helper import display_solution, node_depth


def main():
    print("\n" + "╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "PROBLEMA DOS RECIPIENTES COM ÁGUA" + " " * 15 + "║")
    print("║" + " " * 15 + "Recipientes: 9L e 4L" + " " * 23 + "║")
    print("║" + " " * 15 + "Objetivo: Obter 6 litros" + " " * 19 + "║")
    print("╚" + "=" * 58 + "╝")

    problem = WaterRecipientsProblem()

    # 1. BUSCA EM LARGURA (BUSCA CEGA)
    print("\n\n┌─ EXECUTANDO BUSCA CEGA...")
    bfs_node = breadth_first_tree_search(problem)
    display_solution(bfs_node, "BUSCA EM LARGURA")

    # EXTRA-1 BUSCA EM PROFUNDIDADE (BUSCA CEGA) - teste experimental
    # print("\n\n┌─ EXECUTANDO BUSCA CEGA - BUSCA EM PROFUNDIDADE...")
    # dfs_node = depth_first_tree_search(problem)  # resultou em Memory Error sem limitar a profundidade
    # display_solution(dfs_node, "BUSCA EM PROFUNDIDADE")

    # EXTRA-2. BUSCA EM PROFUNDIDADE LIMITADA (BUSCA CEGA) - teste experimental
    # print("\n\n┌─ EXECUTANDO BUSCA CEGA - DFS LIMITADA...")
    # limit = 10 # se não escolher o adequado faz mais passos do que o necessário
    # dfs_limited_node = depth_limited_search(problem, limit) # se não escolher um limite certo, a execução falha
    # display_solution(dfs_limited_node, f"DFS LIMITADA (limite={limit})")

    # EXTRA-3 BUSCA EM PROFUNDIDADE ITERATIVA (BUSCA CEGA) - teste experimental
    # print("\n\n┌─ EXECUTANDO BUSCA CEGA - BUSCA EM PROFUNDIDADE ITERATIVA...")
    # ids_node = iterative_deepening_search(problem) # reexplora nós
    # display_solution(ids_node, "BUSCA EM PROFUNDIDADE ITERATIVA")

    # 2. BUSCA GULOSA
    # escolhe expandir sempre o nó com menor custo, o “mais promissor”
    # segue sempre o caminho que parece levar mais direto até o objetivo, mas pode se enganar
    print("\n\n┌─ EXECUTANDO BUSCA GULOSA...")
    greedy_node = greedy_best_first_graph_search(problem, problem.heuristic)
    display_solution(greedy_node, "BUSCA GULOSA")

    # 3. BUSCA A*
    # segue o caminho que parece bom, mas sem esquecer o que já foi percorrido. é mais cauteloso.
    print("\n\n┌─ EXECUTANDO BUSCA A*...")
    astar_node = astar_search(problem, problem.heuristic)
    display_solution(astar_node, "BUSCA A*")

    # COMPARAÇÃO FINAL
    print("\n\n" + "╔" + "=" * 58 + "╗")
    print("║" + " " * 18 + "COMPARAÇÃO DOS ALGORITMOS" + " " * 15 + "║")
    print("╚" + "=" * 58 + "╝")

    print("\n┌─ Busca em Largura (BFS):")
    print(f"│  Passos da solução: {node_depth(bfs_node)}")
    print(f"│  Garantia: Solução ótima ✓")

    print("\n┌─ Busca Gulosa:")
    print(f"│  Passos da solução: {node_depth(greedy_node)}")
    print(f"│  Garantia: Não garante otimalidade")

    print("\n┌─ Busca A*:")
    print(f"│  Passos da solução: {node_depth(astar_node)}")
    print(f"│  Garantia: Solução ótima ✓ (com heurística admissível)")

    print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()
