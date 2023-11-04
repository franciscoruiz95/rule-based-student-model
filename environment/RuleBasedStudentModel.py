import gym
from gym import spaces
import numpy as np
from environment.rules_based_on_numbers import RBOnNumbers as Rules

# Crear el modelo de estudiante basado en reglas
class RuleBasedStudentModel(gym.Env):
    def __init__(self):
        super().__init__()
        self.action = 0
        self.reward = 0.0
        self.state = 0
        #Reglas difinidas para calcular la recompensa
        self.P = Rules()

        # Acciones: 5 categorías {0 : Aritmética, 1 : Proporciones, 2 : Geometría, 3 : Porcentajes, 4 : Tiempo-Velocidad}
        self.action_space = spaces.Discrete(5)

        # Observaciones: 6 emociones {0 : Felicidad, 1 : Triste, 2 : Miedo, 3 : Asco, 4 : Ira, 5 : Sorpresa}
        self.observation_space = spaces.Discrete(6)

    def step(self, action):
        response, probability = self.P[self.state][action]
        if response == 1:
            # Respuesta correcta
            self.reward = np.random.choice([0, 1], p=[1 - probability, probability])
        else:
            # Respuesta incorrecta
            self.reward = np.random.choice([0, 1], p=[probability, 1 - probability])

        self.state = np.random.randint(6) # Emoción/estado aleatoria
        self.action = action
        # self.render()
        return self.state, self.reward , False, False, {}  # Devolver observación, recompensa

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.action = 0
        self.reward = 0.0
        self.state = np.random.randint(6)  # Emoción/estado aleatoria

        return self.state, {}  # Estado inicial aleatorio

    def render(self):
        print(f"State: {self.state}, Action: {self.action}, Reward: {self.reward}")