from environment.RuleBasedStudentModel import RuleBasedStudentModel as RBStudentModel

from gym.envs.registration import register

register(
    id="RBStudentModel-v0",
    entry_point='environment.RuleBasedStudentModel:RBStudentModel'
)

(RBStudentModel,)