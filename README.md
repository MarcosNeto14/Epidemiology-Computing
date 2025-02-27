Simulação do Modelo SIR em Grade
Este projeto implementa uma simulação do modelo epidemiológico SIR (Suscetível-Infectado-Recuperado) em uma grade 2D usando Python. A simulação mostra visualmente como uma doença se espalha através de uma população.

Descrição
O modelo SIR divide a população em três grupos:

Suscetível (S): Indivíduos que podem ser infectados.

Infectado (I): Indivíduos que têm a doença e podem transmiti-la.

Recuperado (R): Indivíduos que se recuperaram e estão imunes.

Parâmetros da Simulação
tamanho_grade: Tamanho da grade (50x50).

taxa_infeccao: Probabilidade de um indivíduo suscetível ser infectado por um vizinho infectado (0.3).

taxa_recuperacao: Probabilidade de um indivíduo infectado se recuperar (0.1).

passos: Número de passos da simulação (100).

Visualização
A simulação usa um mapa de cores 'viridis':

Azul escuro: Suscetível (0).

Verde/Amarelo: Infectado (1).

Amarelo claro: Recuperado (2).

Requisitos
Python 3.7+

NumPy

Matplotlib

Instalação
Clone este repositório:

bash
Copy
git clone https://github.com/MarcosNeto14/Epidemiology-Computing
Instale as dependências:

bash
Copy
pip install numpy matplotlib
Uso
Execute o script principal para iniciar a simulação:

bash
Copy
python main.py
Como Funciona
A simulação começa com uma grade de 50x50 células, onde a maioria está suscetível (azul).

Algumas células são inicialmente infectadas (verde/amarelo).

A cada passo:

Células suscetíveis podem ser infectadas por vizinhos infectados.

Células infectadas podem se recuperar.

A simulação continua por 100 passos, mostrando a evolução da epidemia.

Resultados
A simulação produz uma animação que mostra a propagação da doença ao longo do tempo. A grade é atualizada a cada passo, permitindo visualizar como a infecção se espalha e como os indivíduos se recuperam.
