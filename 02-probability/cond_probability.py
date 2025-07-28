def conditional_probability(prob_a_and_b, prob_b):
    """
    조건부 확률 계산
    :param prob_a_and_b: 사건 A와 B가 동시에 일어날 확률
    :param prob_b: 사건 B가 일어날 확률
    :return: 조건부 확률 (A | B)
    """
    return prob_a_and_b / prob_b

# 주어진 확률 값
prob_a = 0.6    # 빵
prob_b = 0.4    # 우유
prob_a_and_b = 0.3

# 조건부 확률 계산
prob_a_given_b = conditional_probability(prob_a_and_b, prob_b)

print("우유를 산 경우에 빵을 살 확률: ", prob_a_given_b)