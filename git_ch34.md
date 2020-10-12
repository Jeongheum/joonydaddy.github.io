## 브랜치 확인 / 만들기
git branch # branch확인하거나, 만드는 명령
git branch apple # b라는 브랜치 만들기

git log
# (HEAD -> master, apple) # 2개의 브랜치가 있고, 현재 작업중인 브랜치는 master브랜치다

git commit -am "branch명 message" # branch명에만 commit

## 브랜치 이동 
git checkout apple # apple branch로 체크아웃
git log --oneline
git log --oneline --branches #전체 브랜치별 로그 출력
git log --oneline --branches --graph 

git log master..apple # master-apple간 차이점 보여줌
git log apple..master # apple-master간 차이점 보여줌

# 브랜치 병합
git merge o2
