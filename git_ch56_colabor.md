# 5장 협업하기

git clone url git_home  

git clone url git_office  

git fetch  # FETCH_HEAD로 가져옴. 

git status # Your branch is behind 'origin/master' by 1 commit, and can be fast-forwarded. (use "git pull" to update your local branch)   

git merge FETCH_HEAD  # 지역저장소에 반영하지 않는 최신 커밋을 병합

git merge origin/master

git merge origin/brand_name

## 공동작업자 추가

공동 작업할 respository에 settings 메뉴 > collaboration > 에서 추가

# 6장 깃허브에서 개발자와 소통하기  
### 6.1 프로필 작성하기  

### 6.2 Readme화일 작성하기  

간단한 설명을 markdown형식으로 작성.

기본적인 markdown문법을 설명함. 이건 이전에 정리해 놓은 것으로 끝.

### <새로 배운 MD문법>  
# 줄바꾸기는 enter 2번

#### 순서없는 목록만들기
플러스기호 (+) 또는
마이너스기호(-) 또는
별표기호(*) 를 붙여서 나열하면 자동으로 글머리 기호가 붙음.
Tab을 눌러 항목을 들여 쓰면, 여러 단계를 가진 목록을 만들수 있음.

#### 글씨체 적용  
굵게: 별표2개 또는 언더바 2개로 앞뒤를 감싼다  
기울게: 별표1개 또는 언더바 1개로 앞뒤를 감싼다  
취소선: 물결기호 2개로 앞뒤를 감싼다  


#### 인용부호  
작다 > 기호 추가  
또 다른 인용문은 작다기호 2번 >>  

#### 소스코드 삽입

#### 작은따옴표  
물결기호 아래 grave기호  
한 줄짜리 소스코드는 `function add(x,y) {return x+y;}` 처럼 사용합니다.  

#### 링크  
<링크주소> 또는 [링크텍스트](링크주소) 또는 [링크텍스트](링크주소, "부가설명")

#### 이미지 추가  
맨앞에 느낌표(!)를 붙인후, 대체텍스트와 이미지 화일 경로를 지정
![아기고양이](./images/cat.jpg)

### 6.3 오픈소스 프로젝트에 기여하기  
readme 등 간단한 문서 한글 번역부터 시작할수도 있음.  
1. 오픈소스 저장소 복제하기  
fork를 눌러서 자신의 저장소로 복제해야 한다.  
2. 포크한 저장소를 지역 저장소로 클론하고, 수정하기  
3. 원저자에게 수정요청하기. new pull request, create pull request      
