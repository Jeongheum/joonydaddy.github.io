git clone url git_home  
git clone url git_office  

git fetch  # FETCH_HEAD로 가져옴. 
git status # Your branch is behind 'origin/master' by 1 commit, and can be fast-forwarded. (use "git pull" to update your local branch)   

git merge FETCH_HEAD  # 지역저장소에 반영하지 않는 최신 커밋을 병합

git merge origin/master
git merge origin/brand_name

# 공동작업자 추가
