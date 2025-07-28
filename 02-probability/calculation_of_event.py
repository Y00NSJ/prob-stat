### 시나리오: 주사위 던지기 실험
# 표본공간
S = set(range(1, 7))
# 사건 A: 주사위 눈금이 2 이하
A = {1, 2}
# 사건 B: 주사위 눈금이 홀수
B = {x for x in S if x % 2 != 0}

# union event
union_AB = A.union(B)

# product event
product_AB = A.intersection(B)

# complement events
complement_A = S.difference(A)
complement_B = S.difference(B)

print(f"""합집합: {union_AB}
교집합: {product_AB}
여집합_A: {complement_A}
여집합_B: {complement_B}""")