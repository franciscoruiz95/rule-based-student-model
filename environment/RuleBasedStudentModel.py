import gym
from gym import spaces
import numpy as np
from rules_based_on_numbers import RBOnNumbers as Rules

# Crear el modelo de estudiante basado en reglas
class RuleBasedStudentModel(gym.Env):
    def __init__(self):
        super().__init__()
        #Reglas difinidas para calcular la recompensa
        self.P = Rules()

        # Acciones: 5 categorías {0 : Aritmética, 1 : Proporciones, 2 : Geometría, 3 : Porcentajes, 4 : Tiempo-Velocidad}
        self.action_space = spaces.Discrete(5)

        # Observaciones: 6 emociones {0 : Felicidad, 1 : Triste, 2 : Miedo, 3 : Asco, 4 : Ira, 5 : Sorpresa}
        self.observation_space = spaces.Discrete(6)

    def step(self, action, emotion):
        response, probability = self.P[emotion][action]
        if response == 1:
            # Respuesta correcta
            reward = np.random.choice([0, 1], p=[1 - probability, probability])
        else:
            # Respuesta incorrecta
            reward = np.random.choice([0, 1], p=[probability, 1 - probability])

        return reward, probability, False, {}  # Devolver recompensa y probabilidad

    def reset(self):
        action = np.random.randint(5)  # Acción aleatoria
        emotion = np.random.randint(6)  # Emoción aleatoria

        return action, emotion  # Estado inicial aleatorio