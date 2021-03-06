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
open('filename','r', encoding='utf8')로 해도 한글txt화일이 정상적으로 열리는데,  
import codec  # pip install codec
f=codec.open('filename','r','utf8')


## 3.2 정규식표현으로 문자열 다루기
파이썬 howto문서 docs.python.org/3.7/howto/regex.html  
점프투파이썬 7장 참고 https://wikidocs.net/4308  

python, c, c++, java, 아래아 한글 등 여러 프로그램에서 공통적으로 사용할 수 있음.  

### 메타문자  
__. ^ $ * + ? { } [ ] \ | ( ) __  

문자클래스 [ ]  
[]사이의 문자들과 매치  
- (하이픈) "~부터 ~까지"의 범위를 의미
ex1) [abc] "a, b, c 중 한개의 문자와 매치"  
ex2) [a-z] "a부터 z까지의 문자와 매치". ex1은 [a-c]로 표시할 수 있겠죠?  
ex3) [0-9] "0부터 9까지의 숫자와 매치"  

^ (not) 
ex4) [^0-9] "숫자가 아닌, 즉 문자만 매치"


자주 사용하는 문자 클래스  
|정규표현식 | 설명|  
|----------|-----|
|\d | 숫자와 매치, [0-9]와 동일 |  
|\D | 숫자가 아닌것과 매치, [^0-9]와 동일 |  
|\w | 문자 숫자와 매치. [a-zA-z0-9]와 동일 |  
|\W | \w와 반대  |  
|\s | whitespace문자와 매치. [\t\n\r\f\v]와 동일|  
|\S | \s와 반대  |

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
