# 🧠 AI Tag — Multi-Agent Reinforcement Learning

Um ambiente 2D desenvolvido em **Python + Pygame** para estudar **Reinforcement Learning (RL)** através de uma simulação de pega-pega entre dois agentes autônomos.

O projeto possui dois agentes controlados por redes neurais independentes:

* 🔴 **Perseguidor:** aprende a diminuir a distância até o fugitivo.
* 🔵 **Fugitivo:** aprende a aumentar a distância do perseguidor.

O objetivo é estudar como comportamentos competitivos podem surgir através do aprendizado por reforço.

---

## 🚀 Tecnologias

* **Python**
* **Pygame** — ambiente e visualização 2D
* **PyTorch** — redes neurais
* **Deep Q-Network (DQN)** — aprendizado por reforço
* **Replay Buffer** — armazenamento de experiências
* **Adam** — otimização da rede neural

---

As quatro ações disponíveis são:

| Ação | Movimento |
| ---- | --------- |
| `0`  | Baixo     |
| `1`  | Cima      |
| `2`  | Direita   |
| `3`  | Esquerda  |

A ação é escolhida utilizando uma estratégia **ε-greedy**, permitindo que o agente explore diferentes comportamentos durante o treinamento.

---

## 🔄 Ciclo de aprendizado

A cada interação com o ambiente:

```text
Estado
  ↓
Rede Neural
  ↓
Escolha da ação
  ↓
Movimento
  ↓
Novo estado
  ↓
Recompensa
  ↓
Replay Buffer
  ↓
Treinamento da DQN
  ↓
Atualização dos pesos
```

### Perseguidor 🔴

O perseguidor recebe:

* `+1` quando diminui a distância;
* `-1` quando aumenta a distância;
* `+100` ao capturar o fugitivo.

### Fugitivo 🔵

O fugitivo recebe:

* `+1` quando aumenta a distância;
* `-1` quando diminui a distância;
* `-100` quando é capturado.

---

## 📁 Estrutura

```text
ai-tag/
│
├── src/
│   ├── main.py
│   ├── agent.py
│   ├── dqn.py
│   ├── trainer.py
│   └── replay_buffer.py
│
├── .gitignore
└── README.md
```

### Responsabilidade dos arquivos

**`agent.py`**

Implementa o agente e sua interação com o ambiente:

* posição;
* velocidade;
* movimentação;
* colisão com bordas;
* estado;
* ações;
* recompensas.

**`dqn.py`**

Implementa a rede neural utilizada pelo DQN.

**`trainer.py`**

Responsável pelo treinamento:

* seleção de ações;
* ε-greedy;
* replay;
* cálculo do target;
* backpropagation;
* atualização da target network;
* salvamento dos pesos.

**`replay_buffer.py`**

Armazena experiências passadas para permitir o treinamento através de mini-batches.

**`main.py`**

Executa o ambiente, controla os episódios e conecta os agentes às redes neurais.

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/ai-tag.git
cd ai-tag
```

Instale as dependências:

```bash
pip install pygame torch
```

Execute:

```bash
python src/main.py
```

---

## 💾 Modelos treinados

Ao encerrar a execução, os pesos das redes são salvos:

```text
dqn_red.pth
dqn_blue.pth
```

Esses arquivos representam os conhecimentos adquiridos pelos respectivos agentes durante o treinamento.

---

## 🎯 Objetivo acadêmico

O projeto foi desenvolvido como um ambiente experimental para estudar conceitos de **Inteligência Artificial e Aprendizado por Reforço**, especialmente:

* Deep Q-Learning;
* redes neurais;
* exploração vs. explotação;
* aprendizado baseado em recompensas;
* experiência de replay;
* target networks;
* aprendizado multiagente;
* comportamento emergente.

A ideia é evoluir gradualmente de um ambiente simples para um cenário de **Multi-Agent Reinforcement Learning (MARL)**.

---

## 👨‍💻 Autor

**Caio Muniz**

Estudante de Engenharia da Computação — Universidade Federal do Ceará (UFC).

Este projeto faz parte dos estudos e experimentos pessoais com **Inteligência Artificial, Machine Learning e Reinforcement Learning**.
