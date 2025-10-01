from aima3.search import breadth_first_tree_search, greedy_best_first_graph_search, astar_search

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

    # 2. BUSCA GULOSA
    # escolhe expandir sempre o nó com menor custo, o “mais promissor”
    print("\n\n┌─ EXECUTANDO BUSCA GULOSA...")
    greedy_node = greedy_best_first_graph_search(problem, problem.heuristic)
    display_solution(greedy_node, "BUSCA GULOSA")

    # 3. BUSCA A*
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
