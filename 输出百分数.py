#utf-8
#用格式控制符输出
'''while 1:
    x=input('输入一个数字')
    print(x,end='%\n')
'''

'''
while 1:
    x=input('输入一个数字')
    a=int(x)
    b='%'
    print(a,b)'''

'''
while 1:
    x=input('输入一个数字')
    print(x,'%')'''

'''
while 1:
    x=input('输入一个数字') 
    print(f'{x}%')
    '''
    
while 1:
    x=input('输入一个数字')
    y=int(x)
    print('%(a)d %(b)s'%{'a':y,'b':'%'})
