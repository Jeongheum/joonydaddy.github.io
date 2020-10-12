## 브랜치 확인 / 만들기
git branch # branch확인하거나, 만드는 명령
git branch apple # b라는 브랜치 만들기

git log
# (HEAD -> master, apple) # 2개의 브랜치가 있고, 현재 작업중인 브랜치는 master브랜치다

git commit -am "message" # branch명에만 commit

## 브랜치 이동 
git checkout apple # apple branch로 체크아웃
git log --oneline
git log --oneline --branches #전체 브랜치별 로그 출력
git log --oneline --branches --graph 

git log master..apple # master-apple간 차이점 보여줌
git log apple..master # apple-master간 차이점 보여줌

# 브랜치 병합
git merge o2  
git merge o2 --no-edit

# 동일한 화일 병합


# 같은 문서, 같은 위치 수정했을때 병합
$ git merge o2
Auto-merging work.txt
CONFLICT (content): Merge conflict in work.txt
Automatic merge failed; fix conflicts and then commit the result

vim work.txt에서 <<< HEAD, =====, o2>>>>>> 부분을 원하는대로 수정해주고 git commit -am 'merge o2'해줘야 함

# 병합이 끝난 브랜치 삭제하기
git branch -d o2

# 브랜치 관리하기
git stash
git stash pop
git stash apply
git stash drop
