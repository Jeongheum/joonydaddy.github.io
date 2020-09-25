# 3장 텍스트 화일 가공

## 3.1 파일입출력 연습  
import os # 반드시 필요  

os.getcwd()  
os.chdir()  
>경로 입력시 \\입력이 번거롭다면, r'경로명'  

os.listdir() #윈도우 dir명령과 같음.  

p.78, 80, 83 f.write()하면 입력한 개수출력은 idle에서 실행할때만 나온다.  
p.83 with 문으로 객체를 만들지 않고 파일 입출력하기 --> as f에서 f가 객체에 해당하므로, with문으로 파일 입출력하기가 더 적합할 듯하다.  

p.85 import codec # 필수일까?  


## 3.2 정규식표현으로 문자열 다루기
pytho, c, c++, java, 아래아 한글 등 여러 프로그램에서 공통적으로 사용할 수 있음.  

re.match(pattern, str) # 해당 문자열의 가장 처음부터  
re.search(pattern, str)  
re.findall(pattern, str)  
re.split(patter, str)  
re.sub(pattern, repl, str) # 이 순서는 함수 intelligence기능 도움을 받자  
