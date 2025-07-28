import numpy as np
from statistics import mode, StatisticsError
from scipy import stats


# 예제 데이터
exam_scores = [82, 90, 76, 92, 88, 79, 95, 87, 90, 76, 92, 90, 85, 78, 85]

# mean
mean_score = np.mean(exam_scores)

# median
median_score = np.median(exam_scores)

# mode
try:
    mode_score = mode(exam_scores)
except StatisticsError:     # 최빈값이 여러 개일 경우
    mode_score = stats.mode(exam_scores)[0][0]      # 가장 먼저 등장한 값

print(f"평균: {mean_score}\n"
      f"중앙값: {median_score}\n"
      f"최진값: {mode_score}\n")