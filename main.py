import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animacao
from matplotlib.widgets import Slider

# Parâmetros do modelo
tamanho_grade = 50 
taxa_infeccao = 0.3 
taxa_recuperacao = 0.1  
passos = 100  

# Inicialização da grade (0 = Suscetível, 1 = Infectado, 2 = Recuperado)
grade = np.zeros((tamanho_grade, tamanho_grade), dtype=int)
# Infectar algumas células aleatórias
grade[np.random.randint(0, tamanho_grade, 10), np.random.randint(0, tamanho_grade, 10)] = 1

def get_vizinhos(i, j):
    vizinhos = []
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x == i and y == j:
                continue
            if x < 0:
                x = tamanho_grade - 1
            elif x >= tamanho_grade:
                x = 0
            if y < 0:
                y = tamanho_grade - 1
            elif y >= tamanho_grade:
                y = 0
            vizinhos.append(grade[x, y])
    return vizinhos

def atualizar(frame):
    global grade
    nova_grade = grade.copy()
    

    suscetiveis = grade == 0
    for i in range(tamanho_grade):
        for j in range(tamanho_grade):
            if suscetiveis[i, j]:
                vizinhos = get_vizinhos(i, j)
                if np.any(np.array(vizinhos) == 1) and np.random.rand() < taxa_infeccao:
                    nova_grade[i, j] = 1
    

    recuperando = (grade == 1) & (np.random.rand(tamanho_grade, tamanho_grade) < taxa_recuperacao)
    nova_grade[recuperando] = 2
    
    grade = nova_grade
    matriz.set_array(grade)
    
   
    contagem_suscetivel = np.sum(grade == 0)
    contagem_infectado = np.sum(grade == 1)
    contagem_recuperado = np.sum(grade == 2)
    ax.set_title(f'Passo: {frame}\nSuscetíveis: {contagem_suscetivel}, Infectados: {contagem_infectado}, Recuperados: {contagem_recuperado}')
    
    return [matriz]


fig, ax = plt.subplots()
cmap = plt.cm.get_cmap('viridis', 3)  
matriz = ax.matshow(grade, cmap=cmap, vmin=0, vmax=2)
plt.colorbar(matriz, ticks=[0, 1, 2], label='Estado: 0 = Suscetível, 1 = Infectado, 2 = Recuperado')
plt.title('Simulação de Propagação de Doença')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')


ax.set_xlim(-0.5, tamanho_grade - 0.5)
ax.set_ylim(-0.5, tamanho_grade - 0.5)


ax_taxa_infeccao = plt.axes([0.2, 0.02, 0.65, 0.03])
slider_taxa_infeccao = Slider(ax_taxa_infeccao, 'Taxa Infecção', 0.0, 1.0, valinit=taxa_infeccao)

ax_taxa_recuperacao = plt.axes([0.2, 0.06, 0.65, 0.03])
slider_taxa_recuperacao = Slider(ax_taxa_recuperacao, 'Taxa Recuperação', 0.0, 1.0, valinit=taxa_recuperacao)

def update(val):
    global taxa_infeccao, taxa_recuperacao
    taxa_infeccao = slider_taxa_infeccao.val
    taxa_recuperacao = slider_taxa_recuperacao.val

slider_taxa_infeccao.on_changed(update)
slider_taxa_recuperacao.on_changed(update)


anim = animacao.FuncAnimation(fig, atualizar, frames=passos, interval=100, blit=True)
plt.show()