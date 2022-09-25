#max of three numbers
def max(a,b,c):
    if (a >=b) and (a>=c):
        print('largest =',a)
    elif (b >= a) and (b >= c):
        print('largest =',b)
    else:
        print('largest =',c)
max(10,12,15)



#sum of all nums in list
def add(*n):
    print(sum(n))
add(10,12)
add(40,56,10)

#mul of all nums in list
def mul(*a):
    total=1
    for i in a:
        total=total*i
    print(total)
mul(10,10,2)

#to find alphabeticals
def alpha(*n):
    for i in n:
        if str(i).isalpha():
            print(i)
alpha('a','v','d','d',5)

#to reverse string
def stat(*n):
    for i in (n):
        i = str(i[::-1])
        print(i,end='')
stat('avgiu')

#calculate letters in upper n lowercase
def let(*n):
    lower_let=0
    upper_let=0
    for i in n:
        if i.isupper():
            upper_let=upper_let+1
        elif i.islower():
             lower_let=lower_let+1
        else:
            pass
        print('upper letters are',upper_let)
        print('lower letters are',lower_let)
let('vFrYUI')


#to print unique number
def unique(*n):
    for i in n:
      i=set(i)
    print(i)
unique([10,45,45,12,12,10])

#to print even numbers of list
def even(n):
    x = []
    for i in n:
        if i%2==0:
            x.append(i)
    return(x)
print(even([10,12,45,63,41]))

#passed string is palindrom or not
def pal(*n):
    for i in n:
        if str(i)==i[::-1]:
         return ('it is palindrome')
        else:
            return('it is not palindrome')
print(pal('nayan'))
print(pal('char'))
print(pal('none'))

#create n print the list where values are square of list
def square(*n):
        for i in n:
            i = i*i
            print(i)
square(10,12,11)

#if want to write range
def square(*n):
    for n in range(1,11):
        n = n *n
        print(n)
square()

'''

