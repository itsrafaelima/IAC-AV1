from typing import Optional


def display_solution(node: Optional[object], algorithm_name: str):
    print("\n" + "=" * 60)
    print(f"SOLUÇÃO ENCONTRADA - {algorithm_name}")
    print("=" * 60)

    if node is None:
        print("❌ Nenhuma solução foi encontrada.")

    path = []
    current = node
    while current.parent is not None:
        path.append((current.action, current.state))
        current = current.parent
    path.append(("Início", current.state))
    path.reverse()

    print(f"\nNúmero de passos: {len(path) - 1}")
    print("\nSequência de ações:\n")

    for i, (action, state) in enumerate(path):
        prefix = "┌─" if i == 0 else "├─"
        print(f"{prefix} Passo {i}: {action}")

        # Visual representation of the containers
        r9_fill = "█" * state[0] + "░" * (9 - state[0])
        r4_fill = "█" * state[1] + "░" * (4 - state[1])

        print(f"│  Recipiente 9L: [{r9_fill}] {state[0]}L")
        print(f"│  Recipiente 4L: [{r4_fill}] {state[1]}L")

        print("│")

        if state[0] == 6 or state[1] == 6:
            print(f"│ OBJETIVO ALCANÇADO! 6 litros obtidos!")

    print("└" + "─" * 58)


def node_depth(node: Optional[object]):
    if node is None:
        return "N/A"
    depth = 0
    current = node
    while current.parent is not None:
        depth += 1
        current = current.parent
    return depth
