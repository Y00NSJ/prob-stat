import random


### 주사위를 10,000번 던지는 실험을 통해 짝수 눈금이 나올 확률 계산
# 시뮬레이션을 위한 변수 초기화
trials = 10000          # 시행
even_rolls_count = 0   # 짝수 눈금이 나온 횟수

# 주사위 던지기 시뮬레이션
for _ in range(trials):
    roll = random.randint(1, 6)
    if roll % 2 == 0:
        even_rolls_count += 1

# 확률 계산
probability = even_rolls_count / trials
print(f"짝수 눈금이 나올 확률: {probability}")