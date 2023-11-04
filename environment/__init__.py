from RuleBasedStudentModel import RuleBasedStudentModel as RBStudentModel

from gym.envs.registration import register

register(
    id="RBStudentModel-v1",
    entry_point='RuleBasedStudentModel:RBStudentModel'
)

(RBStudentModel,)