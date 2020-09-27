# directory 
# import os
# print(os.getcwd())

# path='D:/Coding/do-it-life-coding/03textfile/' # /가 더 편함. \\
# os.chdir(path)
# print(os.getcwd())

# print(os.listdir())

# # file open, close 

# f=open('a.txt','w')
# f.write('i went to the school yesterday')
# f.close()

# f=open('a.txt','r')
# f.read()  # 읽고 커서가 다음 줄로 이동
# f.read()  # 커서가 맨 끝에 와있는 경우, 결과가 없다.
# f.seek(0) # 커서를 다시 맨 첫줄로 보내주는 역할
# diary = f.read()
# print(diary)
# print(diary[:10])
# f.close()

# with open('a.txt','a') as f:
#     f.write('i go to shool today')
    
# # f=open('a2.txt','r')
# # dat = f.read()  # cp949 error
# # f.close()

# f=open('a2.txt','r',encoding='utf8')
# data = f.read()
# print(data)
# f.close()

# import codec # pip install codec
# f=codec.open('a2.txt','r',encoding='utf8')
# dat2=f.read()
# f.close()
# with open('test.txt','w') as f:
# 	f.write('나는 오늘 학교에 갔습니다.')

#Regular expression
import re

ex="""이동민 교수님은 다음과 같이 설명했습니다(이동민, 2019). 
그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다(최재영, 2019). 
또 다른 견해도 있었습니다(Lion, 2018)"""

res=re.findall(r'\([A-Za-z가-힣]+, \d+\)',ex)
print(res)

p=r'life'
script='life'
re.match(p, script) # match 찾기
print(re.match(p, script).group()) # return matched object 

print(re.match(r'life','life').group())

def refinder(pattern, script):
    if re.match(pattern, script):
        print('Match!')
    else:
        print('No match!')

script='life is so cool'
refinder(p, script)

script='Life is cool'
refinder(p, script)

refinder('is', script)

p=re.compile('[a-z]+')  # 한번 만든 객체를 여러번 사용해야 할때 편하다.
text='life is too short'

print(re.search('is',script).group())
print(re.search('Life',script).group())
print(re.search('cool',script).group())

m=p.match('python')
print(m)

result2=p.findall(text)
print(result2)


result=re.findall('[a-z]+',text) # 아니라면, 그냥 re.xx로 compile과 method를 한번에 수행 
print(result)

