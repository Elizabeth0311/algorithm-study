 
 # 규칙찾기
# 1        방 1개 
# 2~7      방 2개
# 8~19     방 3개 
# 20~37    방 4개.. 

# 끝의 수가 6의 배수만큼 커진다. 


n = int(input())

cnt = 1               ## 1번방에서 시작하므로 방1개로 설정

while n > 1 :         ## n의 값이 1인 경우를 제외 
  n-= (6*cnt)         #  입력값에서 6의 배수만큼 빼준다
  cnt+= 1             # 방 하나 지나옴 
  
print(cnt)
      
