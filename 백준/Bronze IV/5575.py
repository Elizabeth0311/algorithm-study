
## 코드찾아봄

for _ in range(3):
  h1,m1,s1,h2,m2,s2 = map(int,input().split()).   
 
  t1 = h1*3600 + m1*60 + s1 
  t2 = h2*3600 + m2*60 + s2 

  t = t2-t1
  
  h = t//60//60 % 24
  m = t//60 % 60 
  s = t%60

  print(h,m,s)
  
  
  ## a,b,c 입력을 각각 리스트로 만들었음...입력부터 틀림 
  ## 초 단위까지 있어서 초 단위로 모두 바꾼다음에 빼고 다시 시,분,초로 나누어 출력
  ## 굳이 이렇게 까지..? 
  
  ## 시간문제 넘오싫다 
