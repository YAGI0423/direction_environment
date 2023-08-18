### 이 저장소(Repository)는 「1차원 Grid World 환경 구현」에 대한 내용을 다루고 있습니다.

***
작성자: YAGI<br>

최종 수정일: 2023-08-14
+ 2023.08.14: Environment 구현

+ 2023.08.19: READ ME 작성

+ 2023.08.19: 프로젝트 종료
***

<br>

***
+ 프로젝트 기간: 2023-08-12 ~ 2023-08-19
***

## 프로젝트 요약
&nbsp;&nbsp;
파이토치(Pytorch)의 'Dataset' 형식으로 된 Diabetes 데이터셋을 제공합니다. 기존 파이토치 Dataset과 마찬가지로 DataLoader를 이용하여 순회 가능한 객체(Iterable)를 구현할 수 있습니다.
<br><br>

## Getting Start

### Get Environment
```python
from directionEnvironment import Env

env = Env(world_size=5, agent_loc='center')

    is_done = False
    while not is_done:
        goal_loc, agent_loc = env.get_state()

        act = random.randint(0, 1)
        is_done, reward = env.action(act)

        print(f'Goal Location: {goal_loc},\tAgent Location: {agent_loc}')
        print(f'is done: {is_done},\treward: {reward}')
        print('=' * 50, end='\n\n\n')
```
***
<br><br>


## 개발 환경
**Language**

    + Python 3.9.12


<br><br>

## License
This project is licensed under the terms of the [MIT license](https://github.com/YAGI0423/direction_environment/blob/main/LICENSE).