
# 크기가 정해져있는 색종이 
# 도화지 위에 놓았을 때 색종이의 넓이를 구하는것 
# 겹치는 부분도 있음 -> 어떻게 해결할 것인가? . 
# 겹치는 부분을 알아내기 

# 색종이의 크기는 정해져있고 겹치는 부분을 빼면된다.
# 입력값에서 겹치는 부분을 어떻게 구분하고 계산할것인가? 

# 3,7
# 15,7
# 5,2 의 값이 주어졌을 때, 색종이의 오른쪽 위 꼭지점의 좌표는 (13,17)(25,17)(15,12) 
# (13,17)과 (15,12)색종이가 겹친다.
# 제일 길이가 긴 x축 15에서 입력값인 x 축인 3을 빼주고 
# 제일 길이가 긴 y축 17에서 입력값인 y 축인 7을 빼준다

n = int(input()) 

for _ in range(n): 
  x,y = map(int, input().split())
  
# 검색 
# 중복되는 경우, 중복되지 않은 경우,,등 경우의 수가 너무 많음 
# 색종이가 붙여진 영역을 구하면서, 중복되는 부분은 하나의 영역으로 계산 
# 좌측 하단의 좌표를 받아서 가로,세로의 길이가 10인 사각형을 1로 표현
# 1의 개수를 카운트

import sys
input = sys.stdin.readline 

board = [[0]*101 for _ in range(101)]


for _ in range(int(input())) :
  x,y = map(int, input().split())
  for i in range(10) :
    for j in range(10) :
          board[x+i][y+j] = 1      # 흰 도화지를 2차원 배열로 만들어서 검정 색종이를 1로 나타냄

S = 0
for i in board :
  S += sum(i)
print(S)
