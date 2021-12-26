houses = int(input())
cost_of_paint = []
for i in range(houses):
    cost_of_paint.append(list(map(int, input().split())))
for i in range(1, len(cost_of_paint)):
    cost_of_paint[i][0] = min(cost_of_paint[i - 1][1], cost_of_paint[i - 1][2]) + cost_of_paint[i][0]
    cost_of_paint[i][1] = min(cost_of_paint[i - 1][0], cost_of_paint[i - 1][2]) + cost_of_paint[i][1]
    cost_of_paint[i][2] = min(cost_of_paint[i - 1][0], cost_of_paint[i - 1][1]) + cost_of_paint[i][2]
print(min(cost_of_paint[houses - 1][0], cost_of_paint[houses - 1][1], cost_of_paint[houses - 1][2]))