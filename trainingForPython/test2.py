import numpy as np

# 5행 4열의 행렬 생성
arr = np.random.normal(size=(5, 4))

# 첫 번째 행과 세 번째 행 더하기
new_row = np.sum(arr[[0, 2], :], axis=0)

# 다섯 번째 행과 곱하기
new_row = np.multiply(new_row, arr[4, :])

# 결과 출력
print(new_row)