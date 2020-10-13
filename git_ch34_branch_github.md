# 3장 브랜치  
## 브랜치 확인 / 만들기  
git branch # branch확인하거나,   
git branch apple # 브랜치 만들기. b라는 브랜치 생성  

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

# 
git reset Hash_ID  

# 브랜치 관리하기
git stash # 수정중인 화일 감출때 사용. 그렇지 않으면 계속 커밋하라고 하거나, 실수로 커밋할수가 있음. 이럴때 감춰뒀다가 다시 꺼내면 됨.  
git stash list # stash list up. stack구조로 저장됨. stash@{0}~stash@{n}  
git stash pop # 가장 최근 stash 목록으로 되돌리기
git stash apply # stash목록에 기록도 두고, 가장 최근 목록을 불러온다
git stash drop # 가장 최근 목록을 삭제한다.

# 4장 깃허브로 백업하기  
## 원격 저장소에 연결하기  
git remote add origin url  # 최초 1회 실행 remote repo (origin, url)을 연결해라  
git remote -v   # remote repo 연결확인  

git push -u origin master  # local repo (master)를 remote repo (origin)으로 push해라. 최초 1회 실행.  
git push # 이후에는 이렇게  

git pull = git pull origin master
