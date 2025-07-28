import numpy as np
from scipy.stats import variation


# 예제 데이터
data = [1, 2, 2, 3, 4, 5, 5, 5, 6]

# range
data_range = np.max(data) - np.min(data)

# variance
variance = np.var(data, ddof=0)     # 모집단 매개변수
sample_variance = np.var(data, ddof=1)

# standard deviation
std_deviation = np.std(data, ddof=0)
sample_std_deviation = np.std(data, ddof=1)

# coefficient of variation
cv = variation(data)    # scipy
cv = std_deviation / np.mean(data) * 100    # numpy

print(f"""범위: {data_range}
모분산: {variance}
표본 분산: {sample_variance}
모표준편차: {std_deviation}
표본 표준편차: {sample_std_deviation}
변동계수: {cv}""")