import matplotlib.pyplot as plt


# 예제 데이터
data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20]

# 상자 그림 생성
plt.boxplot(data)

# 상자 그림에 제목 및 축 레이블 추가
plt.title("Boxplot of Data")
plt.ylabel("Values")

plt.show()