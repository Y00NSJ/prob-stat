"""
e.g. 철수의 직업 - 가수 or 직장인
- 철수에 대한 정보; 춤을 잘 추고 노래하길 좋아함       => 가수일 가능성 높음
- 직업적인 배경 분포; 남자 가수:남자 직장인 = 1:24    => 직장인일 확률 높음
"""
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl

# macOS의 기본 한글 폰트 설정
mpl.rcParams['font.family'] = 'AppleGothic'

## 사전확률 P(A): 가수일 확률 = 0.04
prior = [1/25. , 24/25.]

## 사후확률 P(A|X): 정보를 알고 있을 때 철수가 가수일 확률
# P(X|A): 철수가 가수일 때 정보가 그러할 확률
prob_x_given_a = 0.9
# P(X|A'): 철수가 직장인일 때 정보가 그러할 확률
prob_x_given_acomp = 0.2
# P(X) = p(A^B) + p(A'^B) . . . 각 확률들의 서로 배반사건이기 때문
#      = p(X|A)p(A) + p(X|A')p(A')
prob_x = prob_x_given_a * prior[0] +prob_x_given_acomp * prior[1]
posterior = prob_x_given_a * prior[0] / prob_x
post_array = [posterior, 1-posterior]

## 시각화
plt.bar([0, .7], prior, alpha=0.7, width=0.25, label='사전확률')
plt.bar([0+0.25, .7+0.25], post_array, alpha=0.7, width=0.25, label='사후확률')
plt.xticks([0.12, 0.82], ['가수', '직장인'])
plt.title('철수의 직업에 대한 사전/사후 확률')
plt.ylabel('확률')
plt.legend(loc='upper left')

plt.show()