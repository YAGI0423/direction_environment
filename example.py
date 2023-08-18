import random
from directionEnvironment import Env

env = Env(world_size=5, agent_loc='center')

is_done = False
while not is_done:
    goal_loc, agent_loc = env.get_state()

    act = random.randint(0, 1)
    is_done, reward = env.action(act)

    print(f'Goal Location: {goal_loc},\tAgent Location: {agent_loc}')
    print(f'is done: {is_done},\treward: {reward}')
    print('-' * 50, end='\n\n\n')