낭랑한 목소리, 귀에 쏙쏙들어오는 쉬운 생활코딩 강의를 진행하는 이고잉님  
git강의 중 엄선된 내용을 정리한 책  

## git사용용도  
1. 버전관리. no more xxx_v1, xxx_v2... stage, commit  
2. 백업하기. github라는 온라인(원격)저장소 이용  
3. 협업하기. 원격저장소에 두고 팀원A, B가 공동작업. push, pull  
1<2<3 순으로 배우자  

## git은  
버전관리 툴. 자동차에 비유.  
리누스 토발스가 리눅스를 만드는데, 지옥과도 같던 버전관리를 위해서 만들었음. 책 제목이 왜 "지옥에서 온~"이라 했는지 이해가 됐음.  

## git client PGM은  
자동차 회사/브랜드처럼 여러개가 있음. github desktop, tortoise, sourcetree, etc, etc
https://git-scm.com/download/gui/windows에 window용 client 프로그램이 수십개가 있음.

# 1장.   
## git 설치 git-scm.com  
<설치시 설정>  
기본편집기는 vim으로 설정.  
  - 예전에 설치한거라 설치했나 긴가민가 했는데, git bash에서는 기본적으로 vim이 실행됨.  
  - 대학 1학년때 배웠던 vi editor사용법과 같다. a, i로 편집모드. esc로 ex모드. :wq, :q 저장하고 종료하거나, 그냥 종료하거나.  
사용방법은 get from the command line and also from 3rd party software선택  

## 리눅스 기본 명령어  
리눅스에서 시초된 툴이라, git bash, git cmd등 cli가 제공된다. 따라서 기본 명령어를 익혀야 한다.  

pwd (present working directory)  
cd (change directory)  
cd ~ (change to home/user directory)  
cd ..  
mkdir (make directory)  
rm -r (remove)  
ls (list)  
ls -al (list all, long) 숨김화일, 디렉터리 포함해서, 상세 정보를 보여줌.  
dir도 사용가능함. DOS시절 명령어  

## git 최초 설정 명령어  

| git  | 사용법을 보여줌 |  
|------|----------------|  
| git config --global user.name "your_name" | 최초 1회 설정. 협업환경에서 사용자 이름 확인용. |  
| git config --global user.email "your_email_addr@your_email.com" | 최초 1회 설정. 협업환경에서 사용자 메일 확인용. 이거 바꾸려면, cd ~가서, vim .gitconfig하고 user.email의 값을 바꾸고 :wq!하면 된다. git config --help로 한참 찾았음.|
| git config --global core.editor "notepad++" | |  
| git config --list | 설정값을 리스트해줌 |  

## 자주 사용하는 git명령어
| git  | 사용법을 보여줌 |  
|------|----------------|  
| git status | on branch master, x commits, changes to be committed |  
| git init | .git/ 폴더 생성.  |  
| git add | 스테이지에 올리기 |  
| git commit -m "note message" | 간단한 메시지 노트와 함께 커밋 |  
| git commit -am | 한번이라도 commit한적 있는 파일에 대해서 한꺼번에 처리 |  
| git log | 작성자, 수정날짜, 메시지, 커밋 해시(커밋구분id) 등 표시  |  
| git log --stat | |  
| git diff | 수정내용을 비교 확인 |  
| git checkout | 수정내용을 버릴때 사용 |  
| git reset HEAD | |  
| git reset HEAD^ | |  
| git remote add |  |  

# 2장 git 버전관리  
큰 흐름  
1. git init : .git/을 만들어서 관리시작함. 먼저 git으로 관리할 (프로젝트) 폴더를 만들고, 이동해서 git init실행.   
              일반 폴더에서 명령하면 not a git repository라고 뜸  
2. new file or modify file : editor. working tree/directory  
--- 3, 4는 .git/ 에서 이뤄진다.
3. stage : git add. 버전으로 관리하고 싶은 화일을 stage에 등록. staging (untracked -> tracked).   
4. version생성 : git commit. 버전으로 반영. 여기까지 로컬 저장소  
5. push or pull : git remote add??? 원격저장소. 이거하기전에 remote설정해야겠지?   

.gitinore에 git을 무시할 화일, 확장자 등 지정가능
.png, .jpg, .pdf등 추가해두자
