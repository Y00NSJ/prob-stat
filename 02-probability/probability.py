### 고전적 확률
## 시나리오: 뽑기 상자에서 특정 색의 공이 나올 확률
red = 2
blue = 3
green = 5

# 빨간색 공이 나올 경우의 수
red_outcomes = red

# 상자 안에서 가능한 모든 경우의 수
total_outcomes = red + blue + green

# 빨간색 공이 나올 확률
probability = red_outcomes / total_outcomes

print("빨간색 공이 나올 확률: ", probability)


### 통계적 확률
## 시나리오: 주사위를 1,000회 던져 4가 나오는 확률
import numpy as np
import matplotlib.pyplot as plt


# 시뮬레이션 횟수
n_throws_short = 1000
# 각 시점별 시뮬레이션 결과를 담은 배열
throws_short = np.random.randint(1, 7, n_throws_short)
# 4가 나온 횟수를 기록할 배열
fours_count_short = np.zeros(n_throws_short)

# 각 던지기마다 4가 나온 횟수를 업데이트
for i in range(n_throws_short):
    fours_count_short[i] = fours_count_short[i - 1] + (throws_short[i] == 4)

# 각 시점에서의 확률
probabilities_short = fours_count_short / np.arange(1, n_throws_short + 1)      # element-wise operation

# 결과 시각화
plt.figure(figsize=(10, 6))
plt.plot(probabilities_short, label = 'Simulated Probability')
plt.axhline(y=1/6, color='r', linestyle='-', label = 'Theoretical Probability = 1/6')
plt.xlabel('Number of Throws')
plt.ylabel('Probability of Throwing a 4')
plt.title('Probability of throwing a 4 Converging to 1/6 (1,000 Throws)')
plt.legend()
plt.grid(True)

plt.show()