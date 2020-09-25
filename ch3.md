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
파이썬 howto문서 docs.python.org/3.7/howto/regex.html  
점프투파이썬 7장 참고 https://wikidocs.net/4308  

python, c, c++, java, 아래아 한글 등 여러 프로그램에서 공통적으로 사용할 수 있음.  

|  method | 목적 |  
|---------|------|  
| obj=re.compile(정규식) | # 정규식을 pattern 객체로 만들어줌. 객체를 여러번 재사용하는 경우에 이 방법이 유리하다. 아니라면 re.findall(pattern, str)처럼 compile과 method를 한번에 수행한다. |  
| re.match(pattern, str) | # 문자열의 처음부터 정규식과 매치되는지 조사한 후, match객체를 돌려준다. group method해야 실제 검색결과 확인가능 |  
| re.search(pattern, str) | # 문자열 전체를 검색하여 정규식과 매치되는지 조사한 후, match객체를 돌려준다. group method해야 실제 검색결과 확인가능 |
| re.findall(pattern, str)  | # 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다 |  
| re.split(patter, str)  |  |
| re.sub(pattern, repl, str) | # 이 순서는 함수 intelligence기능 도움을 받자  |  


match객체의 method  
| method	| 목적 |  
|---------|------|
| group()	| 매치된 문자열을 돌려준다. |  
| start()	| 매치된 문자열의 시작 위치를 돌려준다. |  
| end()	| 매치된 문자열의 끝 위치를 돌려준다.  |  
| span()	| 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다. |  
