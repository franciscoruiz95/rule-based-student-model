import sys
import time
import gym
from agent import QLearning
from environment import RBStudentModel

ENVIRONMENT = "RBStudentModel-v0"

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

