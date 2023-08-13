import random


class Env:
    '''
    world_size: Grid의 크기, 정수 이며 3보다 커야함
    agent_loc: 초기화 시 Agent의 시작 위치, ['random': 무작위, 'center': 중심]
    goal_loc: 초기화 시 목표점의 위치, ['random': 양 극단 중 무작위로 선택, 'left': 왼쪽 극단, 'right': 오른쪽 극단]
    '''
    def __init__(self, world_size: int,
                 agent_loc: str='random', goal_loc: str='random') -> None:
        self.init_vari = {
            'world_size': world_size,
            'agent_loc': agent_loc,
            'goal_loc': goal_loc,
        }

        if world_size >= 3:
            self.world_size = world_size
        else:
            raise Exception("\'world_size\' must be rather than 2")
        
        self.episod_size = self.world_size - 1
        
        self.agent_loc, self.goal_loc = self.init(**self.init_vari)

    def get_state(self) -> tuple[int, int]:
        if self.goal_loc is None or self.agent_loc is None:
            raise Exception("\'agent_loc\' or \'goal_loc\' is None. Please initialize Environment")
        return self.goal_loc, self.agent_loc

    def action(self, act: bool) -> tuple[bool, bool]:
        #act: [True: Left, False: Right]
        #return is_done[True: Done, False: During], reward[True: 상, False: 벌]
        nn_agent_loc = self.agent_loc + act * -2 + 1

        self.episod_size -= 1

        if self.episod_size == 0:
            self.agent_loc, self.goal_loc = None, None
            return True, False
        
        if nn_agent_loc == self.goal_loc:
            self.agent_loc, self.goal_loc = None, None
            return True, True
        
        if nn_agent_loc == 0 or nn_agent_loc == self.goal_loc:
            return False, False
        
        self.agent_loc = nn_agent_loc
        return False, False
        
    def init(self, world_size: int, agent_loc: str, goal_loc: str) -> tuple[int, int]:
        goal_loc_, agent_loc_ = None, None #return value 

        if goal_loc == 'random':
            goal_loc_ = random.choice((0, world_size - 1))
        elif goal_loc == 'left':
            goal_loc_ = 0
        elif goal_loc == 'right':
            goal_loc_ = world_size - 1
        else:
            raise Exception("\'goal_loc\' must be \'random\', \'left\', \'right\'")
        
        if agent_loc == 'random':
            idxs = list(range(world_size))
            idxs.remove(goal_loc_)

            agent_loc_ = random.choice(idxs)
        elif agent_loc == 'center':
            agent_loc_ = world_size // 2
        else:
            raise Exception("\'agent_loc\' must be \'random\', \'center\'")
        return agent_loc_, goal_loc_




if __name__ == '__main__':
    env = Env(world_size=5, agent_loc='center')

    is_done = False
    while not is_done:
        goal_loc, agent_loc = env.get_state()
        print(goal_loc, agent_loc)

        act = random.randint(0, 1)
        is_done, reward = env.action(act)
        print(f'is done: {is_done}, reward: {reward}')
