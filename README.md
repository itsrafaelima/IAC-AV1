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
5. **Tranferir do recipiente de 9L para o de 4L:** (r9, r4) → (r9 - t, r4 + t) onde t = min(r9, 4 - r4)
6. **Tranferir do recipiente de 4L para o de 9L:** (r9, r4) → (r9 + t, r4 - t) onde t = min(r4, 9 - r9)

