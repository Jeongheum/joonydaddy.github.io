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
import re, os

# ex="""이동민 교수님은 다음과 같이 설명했습니다(이동민, 2019). 
# 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다(최재영, 2019). 
# 또 다른 견해도 있었습니다(Lion, 2018)"""

# res=re.findall(r'\([A-Za-z가-힣]+, \d+\)',ex)
# print(res)

# p=r'life'
# script='life'
# re.match(p, script) # match 찾기
# print(re.match(p, script).group()) # return matched object 

# print(re.match(r'life','life').group())

# def refinder(pattern, script):
#     if re.match(pattern, script):
#         print('Match!')
#     else:
#         print('No match!')

# script='life is so cool'
# refinder(p, script)

# script='Life is cool'
# refinder(p, script)

# refinder('is', script)

# p=re.compile('[a-z]+')  # 한번 만든 객체를 여러번 사용해야 할때 편하다.
# text='life is too short'

# print(re.search('is',script).group())
# print(re.search('Life',script).group())
# print(re.search('cool',script).group())

# m=p.match('python')
# print(m)

# result2=p.findall(text)
# print(result2)


# result=re.findall('[a-z]+',text) # 아니라면, 그냥 re.xx로 compile과 method를 한번에 수행 
# print(result)

# number ='My number is 5111223-1****** and yours is 521012-2******'
# print(re.findall('\d{6}',number))

# ex='저는 91년에 태어났습니다. 97년에는 imf가 있었습니다. 지금은 2020년입니다.'
# print(re.findall('\d.+년',ex)) # 숫자로 시작, 모든문자가 1회이상 반복하고, 년으로 끝나는 문자 매치

# print(re.findall(r'\d.+?년',ex)) # 숫자로 시작, 모든 문자가 1회이상 한고, 년으로 끝나는 문자
# print(re.findall(r'\d+.년',ex))

# # split
# sentence='I love a lovely dong, really. I am not telling a lie. What a pretty dog! I love this dog.'
# print(re.split(r'[.?!]',sentence))

# data='a:3;b:4;c:5'
# for i in re.split(r';',data):
#     print(re.split(r':',i))

# # sub
# print(re.sub(r'dog','cat',sentence))

# words='I am home now. \n\n\nI am with my cat.\n\n'
# print(words)
# print(re.sub(r'\n','',words))

# print(re.findall(r'\w+ly',sentence))

os.chdir(r'c:/Python/python/')
# f=open('friends101.txt','r')
# data=f.read()
# print(data[:10], type(data))
# f.close()

# line=re.findall(r'Monica:.+', data)
# print(line[:3], type(line))

# f=open('monica_write.txt','w')
# f.write(str(line)) # input - string, output - list
# f.close()

# f=open('monica_writlines.txt','w')
# f.writelines(line) # input - list, output - string
# f.close()

# f=open('monica_write.txt','r')
# dat=f.readlines()
# print(dat[:10],type(dat))
# f.close()

# words=['apple','cat','brave','drama','arise','blow','coat','above']
# for i in words:
#     m = re.match(r'a\D+',i)
#     if m:
#         print(m.group())

# a='제 이메일 주소는 greatking@naver.com입니다. 오늘 저는 travel@daum.net라는 주소로 메일을 보내려 합니다. 저는 apple@gmail.com, life@abc.co.kr라는 메일도 사용하고 있습니다.'
# b=re.findall(r'[a-z]+@[a-z.]+', a)
# print(b)

# exam='저는 92년에 태어났습니다. 88년에는 올림픽이 있었습니다. 지금은 2020년입니다.'
# print(re.findall('\d.+?년',exam))
# print(re.findall('\d+.년',exam))

d='I have a dong. I am not a girl. You are not alone. I am happy.'
print(re.split(r'[.]',d))

e="Chandler: All righ Joey, be nice. So does he have a hump? A hup and a hair-piece? Phoebe: Wait, does he eat chalk? Phoebe: Just, because, I don't want her to go through what I went through with Carl-oh!"
m=re.findall('\w+:',e)
print(m)
M=list(set(m))
print(M)
