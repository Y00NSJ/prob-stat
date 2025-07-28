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