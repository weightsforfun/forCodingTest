import numpy as np

# 정규분포를 따르는 랜덤한 수로 이루어진 5행 4열의 행렬 생성
arr = np.random.normal(size=(5, 4))

# -0.1 이하이거나 0.5이상인 부분을 100으로 변경
arr = np.where((arr <= -0.1) | (arr >= 0.5), 100, arr)

print(arr)