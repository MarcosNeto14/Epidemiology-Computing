# Simulação do Modelo SIR em Grade

Este projeto realiza uma simulação visual de como uma doença se espalha em uma população, utilizando um modelo simplificado baseado em uma grade 2D. A simulação é inspirada no modelo SIR (Suscetível-Infectado-Recuperado), que divide a população em três categorias principais, permitindo observar a dinâmica de contágio e recuperação.

## Sobre o modelo

O modelo SIR é amplamente utilizado em epidemiologia para entender como doenças infecciosas se propagam. Nesta simulação, a população é representada por uma grade, onde cada célula pode estar em um dos três estados:

- **Suscetível (S)**: Indivíduos que ainda não foram infectados e podem contrair a doença.
- **Infectado (I)**: Indivíduos que estão infectados e podem transmitir a doença para os suscetíveis.
- **Recuperado (R)**: Indivíduos que se recuperaram da doença e estão imunes.

## Parâmetros da Simulação

- `grid_size`: 50x50 células.
- `tau`: Probabilidade de um suscetível ser infectado por um vizinho infectado (0.3).
- `gamma`: Probabilidade de um infectado se recuperar (0.1).
- `steps`: 100 iterações da simulação.

## Visualização

A simulação utiliza um mapa de cores para representar os estados das células:

- Azul escuro: Suscetível (0)
- Verde/Amarelo: Infectado (1)
- Amarelo claro: Recuperado (2)

A animação mostra a evolução da doença ao longo do tempo, permitindo observar padrões de propagação e recuperação.

## Requisitos

- Python 3.7+
- NumPy
- Matplotlib

## Instalação

1. Clonar o repositório
2. Instalar as dependências:

```bash
pip install numpy matplotlib
```

## Uso

```bash
python main.py
```

## Funcionamento da Simulação

1. A grade é criada com a maioria das células no estado Suscetível.Algumas células são infectadas aleatoriamente no início.

2. A cada iteração:
   Células suscetíveis podem ser infectadas por vizinhos infectados, dependendo da taxa de infecção.

Células infectadas podem se recuperar, dependendo da taxa de recuperação.

A grade é atualizada e a animação é gerada.

3. A simulação produz uma animação que mostra a propagação da doença e a evolução dos estados das células ao longo do tempo.

## Resultados

A animação gerada permite visualizar:

A propagação inicial da doença.

O pico de infecções.

A recuperação gradual da população.
