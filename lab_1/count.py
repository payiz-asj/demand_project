import re
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

f = open("body.txt",'r',encoding= 'utf-8')
all_text = re.sub('\W+','\n',f.read())
#all_text = f.read()
f.close()

D = dict()
for i in all_text.split():
    D[i] = D.get(i,0) + 1

l = []
for a,b in D.items():
    l.append((b,a))
l.sort(reverse=True)

for count,word in l:
    print(word,count,sep='\t')

#作者：重生
#链接：https://www.zhihu.com/question/26564557/answer/141317574
#来源：知乎
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。