import sys
import time
import gym
import numpy as np
from agent import QLearning
from environment import RBStudentModel
import matplotlib.pyplot as plt

ENVIRONMENT = "RBStudentModel-v0"

def graphic(values):
    # Matriz dada
    matrix = np.array(values)

    # Encontrar el máximo para cada fila y su índice correspondiente
    max_indices = np.argmax(matrix, axis=1)
    max_values = np.max(matrix, axis=1)

    # Crear una lista de acciones para el eje x
    acciones = ['Acción 1', 'Acción 2', 'Acción 3', 'Acción 4', 'Acción 5']

    # Crear una lista de emociones para el eje y
    emociones = ['Emoción 1', 'Emoción 2', 'Emoción 3', 'Emoción 4', 'Emoción 5', 'Emoción 6']

    # Asignar colores para cada emoción
    colores = ['cyan', 'grey', 'magenta', 'blue', 'red', 'yellow']

    # Crear un gráfico de líneas que muestre la acción correspondiente al valor máximo para cada emoción
    for i in range(len(emociones)):
        plt.plot(acciones, matrix[i], label=emociones[i], color=colores[i], marker='o')
        # plt.text(acciones[max_indices[i]], max_values[i] + 0.05, f"{max_values[i]:.2f}", ha='center')

    plt.xlabel('Acciones')
    plt.ylabel('Probabilidad')
    plt.title('Acciones con puntaje más alto por emoción')
    plt.legend()
    plt.show()

if __name__ == "__main__":

    env = gym.make(ENVIRONMENT)
    agent = QLearning(
        env.observation_space.n, env.action_space.n, alpha=0.1, gamma=0.9, epsilon=0.1
    )

    iterations = 100 if len(sys.argv) == 1 else int(sys.argv[1])

    observation, _ = env.reset()
    
    for _ in range(iterations):
        action = agent.get_action(observation, "random")
        new_observation, reward, terminated, _, _ = env.step(action)
        agent.update(observation, action, new_observation, reward, terminated)
        observation = new_observation
        agent.render('step')
        agent.render()

        print('*************************************************************')
    
    graphic(agent.q_table)