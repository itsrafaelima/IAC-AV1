# Problema dos Recipientes com Água (9L, 4L)

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
1. **Encher9:** (r9, r4) → (9, r4)
2. **Encher4:** (r9, r4) → (r9, 4)
3. **Esvaziar9:** (r9, r4) → (0, r4)
4. **Esvaziar4:** (r9, r4) → (r9, 0)
5. **Transferir9para4:** (r9, r4) → (r9 - t, r4 + t) onde t = min(r9, 4 - r4)
6. **Transferir4para9:** (r9, r4) → (r9 + t, r4 - t) onde t = min(r4, 9 - r9)

### Custo
- Cada ação tem custo 1 (todos os passos são equivalentes)

---

## 🔍 Algoritmos Implementados

### 1. Busca Cega: Busca em Largura (BFS)

**Justificativa da Escolha:**

A Busca em Largura foi escolhida como estratégia de busca cega pelos seguintes motivos:

✅ **Completude:** Garante encontrar uma solução se ela existir

✅ **Otimalidade:** Garante encontrar a solução com menor número de passos (todos os passos têm custo 1)

✅ **Espaço de estados pequeno:** Com apenas 50 estados possíveis, não há problema de memória

✅ **Evita loops infinitos:** Diferente da busca em profundidade, a BFS não corre o risco de seguir caminhos infinitos devido às operações cíclicas (encher/esvaziar repetidamente)

❌ **Por que NÃO usar Busca em Profundidade:**
- Risco de entrar em loops infinitos
- Pode encontrar soluções não-ótimas
- Não garante a menor sequência de ações

### 2. Busca Informada: Busca Gulosa

**Heurística:** Diferença absoluta mínima até 6 litros
```python
h(n) = min(|r9 - 6|, |r4 - 6|)
```

**Características:**
- Expande sempre o nó que parece mais próximo do objetivo
- Mais rápida que BFS
- NÃO garante solução ótima

### 3. Busca Informada: Busca A*

**Função de Avaliação:** f(n) = g(n) + h(n)
- g(n) = custo real do caminho até o nó
- h(n) = estimativa heurística até o objetivo

**Características:**
- Combina custo real com estimativa
- Garante solução ótima (com heurística admissível)
- A heurística implementada é admissível (nunca superestima)

---

## 💻 Requisitos

- Python 3.7 ou superior
- Nenhuma biblioteca externa necessária (usa apenas bibliotecas padrão)

---

## 🚀 Como Executar

### Opção 1: Execução Direta
```bash
python recipientes_agua.py
```

### Opção 2: Execução em Ambiente Virtual (Recomendado)
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Executar o programa
python recipientes_agua.py
```

---

## 📊 Saída Esperada

O programa executará os três algoritmos sequencialmente e exibirá:

1. **Para cada algoritmo:**
   - Nós expandidos
   - Nós gerados
   - Tempo de execução
   - Profundidade/custo da solução

2. **Solução encontrada:**
   - Sequência completa de ações
   - Representação visual dos recipientes em cada passo
   - Indicação do objetivo alcançado

3. **Comparação final:**
   - Comparativo entre os três algoritmos
   - Número de passos de cada solução
   - Garantias de otimalidade

### Exemplo de Visualização:
```
┌─ Passo 0: Estado Inicial
│  Recipiente 9L: [░░░░░░░░░] 0L
│  Recipiente 4L: [░░░░] 0L
│
├─ Passo 1: Encher recipiente de 9L
│  Recipiente 9L: [█████████] 9L
│  Recipiente 4L: [░░░░] 0L
│
├─ Passo 2: Transferir de 9L para 4L
│  Recipiente 9L: [█████░░░░] 5L
│  Recipiente 4L: [████] 4L
│
...
```

---

## 🧪 Testes e Validação

O código foi testado e validado para:
- ✅ Encontrar solução ótima
- ✅ Não entrar em loops infinitos
- ✅ Explorar corretamente o espaço de estados
- ✅ Implementar corretamente as heurísticas
- ✅ Comparar adequadamente os algoritmos

---

## 📝 Estrutura do Código

```
recipientes_agua.py
├── Classe Estado          # Representação de um estado
├── Classe No              # Nó na árvore de busca
├── Classe ProblemaRecipientes  # Definição do problema
├── busca_em_largura()     # Implementação BFS
├── busca_gulosa()         # Implementação Greedy
├── busca_a_estrela()      # Implementação A*
├── heuristica_diferenca_absoluta()  # Heurística h(n)
└── main()                 # Função principal
```

---

## 👥 Informações para Apresentação

### Pontos Importantes para Discussão:

1. **Por que BFS?**
   - Explique as vantagens para este problema específico
   - Compare com outras estratégias cegas

2. **Heurística Admissível:**
   - Demonstre que h(n) nunca superestima
   - Prove que |recipiente - 6| é admissível

3. **Comparação de Desempenho:**
   - Mostre métricas de cada algoritmo
   - Discuta trade-offs entre tempo e otimalidade

4. **Espaço de Estados:**
   - Explique por que o problema é tratável
   - Discuta escalabilidade para recipientes maiores

---

## 📚 Referências

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.)
- AIMA Python Implementation: https://github.com/aimacode/aima-python

---

## 📅 Entrega

- **Data:** 01/10/2025
- **Formato:** Apresentação em laboratório + código no CANVAS
- **Avaliação:** 50% apresentação + 50% código

---

## ✨ Funcionalidades Extras Implementadas

- 🎨 Interface visual amigável com emojis e formatação
- 📊 Representação gráfica dos recipientes com barras
- ⏱️ Medição de tempo de execução
- 📈 Comparação detalhada entre algoritmos
- 🔍 Métricas completas (nós expandidos, gerados, etc.)

---

## 🐛 Troubleshooting

**Problema:** Erro de import  
**Solução:** Certifique-se de usar Python 3.7+

**Problema:** Execução lenta  
**Solução:** Normal para busca exaustiva, mas deve terminar em < 1 segundo

**Problema:** Não encontra solução  
**Solução:** Verifique se o código não foi alterado, a solução existe e é encontrada

---

## 📧 Contato

Para dúvidas sobre a implementação, consulte o professor ou monitores da disciplina.

---

**Boa sorte na apresentação! 🎓**