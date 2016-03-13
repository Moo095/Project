'''
Created on 2016/03/12

@author: Ryuya
'''

if __name__ == '__main__':
    print("hello, World!!")    #this is comment.
    
    a = 1
    print(a)  #int
    
    b = {'apple':100, "pine":500, 'grape':300}   #hash map
    print(b['apple'])
    
    c = 5
    if c == 1:
        print("c is 1.")
    elif c == 3:
        print("c is 3.")
    else:
        print("c is not 1 and 3.")
    
    print('begin while statement')
    n = 0
    while n < 10:
        print(n)
        n += 1
    else:
        print('END')