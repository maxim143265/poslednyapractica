x=input().split()
c=[]
k=[]
f= False
for i in range (len(x)):
    if x[i]=='(':
        c.append(x[i])
        k.append(i)
    if x[i] == ')':
        if len(c)==0:
            print ('скобка на', i, 'позиции:')
            f=True
            break
        if len(c)>0:
            if c[-1]=='(':
                c.pop()
                k.pop()
if len(c)==0 and f==False:
    print('Правильно')
if len(c)>0 and f==False:
    print('Не закрылась на позиции', k[-1])




