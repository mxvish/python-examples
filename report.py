import gym, numpy as np
import matplotlib.pyplot as plt

def get_status(_observation):
    env_low = env.observation_space.low 
    env_high = env.observation_space.high
    env_dx = (env_high - env_low) / 40 
    position = int((_observation[0] - env_low[0])/env_dx[0])
    velocity = int((_observation[1] - env_low[1])/env_dx[1])
    return position, velocity

def update_q_table(_q_table, _action,  _observation, _next_observation, _reward, _episode):
    next_position, next_velocity = get_status(_next_observation)
    next_max_q_value = max(_q_table[next_position][next_velocity])

    position, velocity = get_status(_observation)
    q_value = _q_table[position][velocity][_action]

    _q_table[position][velocity][_action] = q_value + alpha * (_reward + gamma * next_max_q_value - q_value)
    return _q_table

def get_action(_env, _q_table, _observation, _episode):
    epsilon = 0.002
    if np.random.uniform(0, 1) > epsilon:
        position, velocity = get_status(observation)
        return np.argmax(_q_table[position][velocity])
    else:
        return np.random.choice([0, 1, 2])

if __name__ == '__main__':
    env = gym.make('MountainCar-v0')
    q_table = np.zeros((40, 40, 3))
    observation = env.reset()
    rewards = []
    alpha = 0.2 # 学習率
    gamma = 0.99 # 時間割引き率
    episodes = 10000

    for episode in range(episodes):
        total_reward = 0
        observation = env.reset()

        for _ in range(200):
            action = get_action(env, q_table, observation, episode)

            next_observation, reward, done, _ = env.step(action)

            q_table = update_q_table(q_table, action, observation, next_observation, reward, episode)
            total_reward += reward
            observation = next_observation

            if done:
                rewards.append(total_reward)
                break

""" 
    rate = []
    key = 0

    while key < episodes / 100:
        count = 0
        for x in range(100):
            if rewards[100 * key + x] >= -200:
                count += 1
        rate.append(count / 100)
        key += 1
    print(rate)
""" 

plt.plot(rewards)
plt.title("alpha = " + str(alpha) + ", gamma = " + str(gamma))
plt.ylabel('Episode reward')
plt.xlabel('Training episode')
plt.savefig("output3.png")
