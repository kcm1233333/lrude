#LRUCacheAlgorithm
a=['A','B','C','A','D','Z','D','E']
db=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
us=[]
for i in range(0, len(db)):
  #print(a.count(a[i]))
  result=str(db[i])+":"+str(a.count(db[i]))
  if(a.count(db[i])>=1):
    if(a.count(db[i])>1):
       us.append(db[i])
#print("Hello!",us)
b=us
#print(b)
panjang=4

if(len(a)>panjang):
   tepatas=len(a)-panjang
else:
   tepatas=0
if(len(a)>panjang):
   tepbawa=len(a)
else:
   tepbawa=1   
while (tepatas<tepbawa):
 print(a[tepatas])
 tepatas+=1
init=0
#bawa=1
tung=0

bl=[]
cl=[]
al=[]
nela={}
while(init<len(b)):
 tempat=b[init]
 for i in range(0, len(a)):
   if (a[i]==tempat):
     tung+=1
     bl.append(i)
   if (a[i]!=tempat and a.count(a[i])==tung):
     cl.append(a[i])
     al.append(i)
 nela[init]=max(bl)  
 init+=1    
nl=[]
print(nela)
dear=[]
aw=len(nela)
for i in range(0, aw):
  dear.append(nela[i])
print(dear)  
#if (len(bl)>2):
# for i in range(0, len(bl)):
#  if(bl[i]!=max(bl) and bl[i]!=min(bl)):
#    nl.append(bl[i])
#print(sorted(nl+al))
#ml=sorted(nl+al)
#print(ml)
#halteng=[]
#for i in range(0,len(ml)):
#   halteng.append(a[ml[i]])
#print("Hi!",halteng) 
dela={}
deer=[]
for i in range(0, len(a)):  
  if(a.count(a[i])>1):
     print(i)
  else:
    deer.append(i)
    
print(deer)
duo=sorted(deer+dear)
print(duo)
hear=[]
for ji in range(0, len(duo)):
  hear.append(a[duo[ji]])
print(hear)  
