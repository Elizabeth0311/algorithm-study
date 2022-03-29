# 분모와 분자를 따로 보고 규칙성이 있나 찾아봄 
# 분자는 1,1이 나오면 올라갔다가 다시 내려옴
# 분모는 처음에 1이 나온후 1까지 내려갔간 뒤부터 1,1이 나온후 올라갔다 다시 1까지 내려온후 1부터 시작함

# 주어진 사각형 안에 있는 위치에 분수의 규칙을 찾아봄 -> 안됨 


# 검색
# 지그재그로 되어있는 순서를 활용해서 대각선으로 줄을 나눔 
# 홀수번째 줄은 분자가 1,3,5.. 로 시작하며 숫자가 줄어들고 분모는 1부터 시작해서 늘어난다. 
# 짝수번째 줄은 분모가 2,4,..로 시작하며 숫자가 줄어들고 분자는 1부터 시작해서 늘어난다.
# 위 규칙에 맞게 입력값이 몇 번째 줄에서 어디에 위치해있는지 찾으면 된다.

X = int(input())

L = 1
while X > L :   # 몇 번째 줄인지 찾기
  X -= L        # 입력값이 어느 라인에 있는지 찾기 
  L += 1        # 라인 늘려가기 

if L % 2 == 0 :  # 라인이 짝수번째 일 때
  a = X          # X의 값이 분자가 됨 
  b = L - X +1
else :            # 라인이 홀수번째 일 때는
  a = L - X + 1
  b = X           # X의 값이 분모가 됨
print(f'{a}/{b}')
