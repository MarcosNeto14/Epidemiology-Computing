import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animacao

# Parâmetros do modelo
tamanho_grade = 50  # Tamanho da grade
taxa_infeccao = 0.3  # Taxa de infecção
taxa_recuperacao = 0.1  # Taxa de recuperação
passos = 100  # Número de passos da simulação

# Inicialização da grade (0 = Suscetível, 1 = Infectado, 2 = Recuperado)
grade = np.zeros((tamanho_grade, tamanho_grade), dtype=int)
# Infectar algumas células aleatórias
grade[np.random.randint(0, tamanho_grade, 10), np.random.randint(0, tamanho_grade, 10)] = 1

def atualizar(frame):
    global grade
    nova_grade = grade.copy()
    
    for i in range(tamanho_grade):
        for j in range(tamanho_grade):
            if grade[i, j] == 0:  # Suscetível
                vizinhos = [grade[x, y] for x in range(max(0, i-1), min(tamanho_grade, i+2))
                                          for y in range(max(0, j-1), min(tamanho_grade, j+2))
                                          if (x, y) != (i, j)]
                if np.any(np.array(vizinhos) == 1) and np.random.rand() < taxa_infeccao:
                    nova_grade[i, j] = 1  # Infecta
            elif grade[i, j] == 1:  # Infectado
                if np.random.rand() < taxa_recuperacao:
                    nova_grade[i, j] = 2  # Recuperado
    
    grade = nova_grade
    matriz.set_array(grade)
    return [matriz]

# Configuração do plot
fig, ax = plt.subplots()
matriz = ax.matshow(grade, cmap='viridis')
plt.colorbar(matriz)

# Configurar limites dos eixos
ax.set_xlim(-0.5, tamanho_grade - 0.5)
ax.set_ylim(-0.5, tamanho_grade - 0.5)

# Criar e exibir a animação
anim = animacao.FuncAnimation(fig, atualizar, frames=passos, interval=100, blit=True)
plt.show()