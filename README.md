## 👤 Alunos
Daniel Rodrigues Guarilha - 06003391
Marcela de Oliveira Martins Pereira - 06008491
Rafael Pereira Lima - 06003197

# Problema dos Recipientes com Água (9L, 4L)

07 - Recipientes com Água (9, 4) - versão 1:
Sejam 2 recipientes com capacidades iguais a 9 e 4 litros e uma torneira de
água. Sabendo-se que os recipientes estão inicialmente vazios e que é possível
enchê-los na torneira, ou esvaziá-los passando a água de um para o outro ou
derramando-a no chão, o problema consiste em obter 6 litros de água.

## 📋 Descrição do Problema

**Objetivo:** Obter exatamente 6 litros de água utilizando dois recipientes com capacidades de 9 e 4 litros.

**Estado Inicial:** Ambos os recipientes vazios (0L, 0L)

**Estado Objetivo:** Um dos recipientes contendo exatamente 6 litros

**Ações Permitidas:**
1. Encher um recipiente na torneira
2. Esvaziar um recipiente (derramar no chão)
3. Transferir água de um recipiente para outro

---

## 🎯 Definição Formal do Problema

### Espaço de Estados
- **Estado:** Par ordenado (r9, r4) onde:
  - r9 = quantidade de água no recipiente de 9L (0 ≤ r9 ≤ 9)
  - r4 = quantidade de água no recipiente de 4L (0 ≤ r4 ≤ 4)
- **Cardinalidade:** 10 × 5 = 50 estados possíveis

### Estado Inicial
- (0, 0) - ambos os recipientes vazios

### Teste de Objetivo
- r9 = 6 OU r4 = 6

### Ações e Modelo de Transição
1. **Encher recipiente de 9L:** (r9, r4) → (9, r4)
2. **Encher recipiente de 4L:** (r9, r4) → (r9, 4)
3. **Esvaziar recipiente de 9L:** (r9, r4) → (0, r4)
4. **Esvaziar recipiente de 4L:** (r9, r4) → (r9, 0)
5. **Transferir do recipiente de 9L para o de 4L:** (r9, r4) → (r9 - t, r4 + t) onde t = min(r9, 4 - r4)
6. **Transferir do recipiente de 4L para o de 9L:** (r9, r4) → (r9 + t, r4 - t) onde t = min(r4, 9 - r9)

---

## 📌 Justificativa da Escolha da Busca em Largura

Escolhemos a Busca em Largura porque ela é a mais adequada para problemas de espaço de estados pequenos e finitos, como o dos recipientes de 9L e 4L, garantindo sempre a solução ótima sem sobrecarga significativa de tempo ou memória.

O problema dos recipientes de água (9L e 4L) é um clássico problema de espaço de estados finito e pequeno. Nesse contexto, a busca em largura apresenta vantagens claras em relação às outras buscas cegas:

#### 1. Busca em Profundidade

- Explora os estados indo até o limite de profundidade antes de voltar.
- Problema: pode gerar caminhos muito longos ou até entrar em ciclos se não houver controle.
- No caso dos recipientes, poderia explorar sequências pouco promissoras (por exemplo, encher e esvaziar repetidamente o mesmo recipiente) antes de chegar ao objetivo.
- Não garante encontrar a solução com menor número de passos.

#### 2.1. Busca em Profundidade Limitada

- A versão limitada tenta reduzir o problema de caminhos infinitos, mas exige definir um limite arbitrário de profundidade, que pode ser inadequado.

#### 2.2. Busca em Profundidade Iterativa

- A iterativa, cada vez que o limite de profundidade aumenta, o algoritmo reinicia desde a raiz. 
- Ela garante solução ótima, mas repete muito trabalho, sendo menos eficiente que BFS nesse espaço pequeno.

#### 3. Busca em Largura

- Explora todos os estados a uma determinada profundidade antes de avançar.
- Vantagens para este problema:
    - Garante encontrar a solução com menor número de passos (ótima em custo unitário).
    - Como o número máximo de estados possíveis é pequeno (10 x 5 = 50 estados), o custo de memória é perfeitamente viável.
    - Evita a necessidade de parâmetros extras (como limite de profundidade).

#### Resumindo:

- **Busca em Profundidade** → pode ser mais rápida em alguns casos, mas arriscada: não garante solução ótima.
- **Busca em Profundidade Limitada** → depende de limite adequado; pode falhar se o limite for mal escolhido.
- **Busca em Profundidade Iterativa** → garante encontrar a solução, mas reexplora muitos nós. 
- **Busca em Largura** → solução sempre ótima, custo computacional aceitável para este problema.

