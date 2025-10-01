from aima3.search import Problem


class WaterRecipientsProblem(Problem):

    def __init__(self, initial=(0, 0), goal=6, capacity=(9, 4)):
        super().__init__(initial, goal)
        self.capacity = capacity
        self.goal = goal

    # ações que podem ser executadas
    def actions(self, state):
        x, y = state
        actions = []
        if x < self.capacity[0]: actions.append("enche recipiente de 9L")
        if y < self.capacity[1]: actions.append("enche recipiente de 4L")
        if x > 0: actions.append("esvazia recipiente de 9L")
        if y > 0: actions.append("esvazia recipiente de 4L")
        if x > 0 and y < self.capacity[1]: actions.append("transfere do recipiente de 9L para o de 4L")
        if y > 0 and x < self.capacity[0]: actions.append("transfere do recipiente de 4L para o de 9L")
        return actions

    # faz as movimentações
    def result(self, state, action):
        x, y = state
        if action == "enche recipiente de 9L":
            return self.capacity[0], y
        elif action == "enche recipiente de 4L":
            return x, self.capacity[1]
        elif action == "esvazia recipiente de 9L":
            return 0, y
        elif action == "esvazia recipiente de 4L":
            return x, 0
        elif action == "transfere do recipiente de 9L para o de 4L":
            # pega o valor que retirou de um para botar em outro
            t = min(x, self.capacity[1] - y)
            return x - t, y + t
        elif action == "transfere do recipiente de 4L para o de 9L":
            # pega o valor que retirou de um para botar em outro
            t = min(y, self.capacity[0] - x)
            return x + t, y - t

    # testa se chegou no objetivo
    def goal_test(self, state):
        return state[0] == self.goal or state[1] == self.goal

    # custo até o objetivo
    # estimativa do quão perto está do objetivo
    def heuristic(self, node):
        x, y = node.state
        # diferença entre a quantidade de água no jarro de 9L e o objetivo (6 litros)
        return abs(x - self.goal)

    # função adicionada para resolver warning, mas não usada
    # serve para problemas de otimização local (como Hill Climbing ou Simulated Annealing)
    def value(self, state):
        pass
