l=[4,7,2,9,7,2,5]
new={}
for i in l:
    if i not in new:
        new[i]=1
    else:
        new[i]+=1

print(new)


s = "python is a programming language"
vowels='aeiouAEIOU'
count_v=0
count_c=0
for i in s:
    if i in vowels:
        count_v+=1
    elif i.isalpha():
        count_c+=1
print('count of vowels',count_v)
print('count of consonants',count_c)

#Define a function that takes a list as an argument and returns the largest odd number in the list.
l= [12, 7, 18, 25, 10, 13]
def large_odd(l):
    largest=0
    for i in l:
        if i%2!=0:
            if i>largest:
                largest=i
    return largest
l= [12, 7, 18, 25, 10, 13]
a=large_odd(l)
print(a)

#Write a program to find the sum of all digits present in a string.
s="abc123de45"
sum=0
for i in s:
    if i.isdigit():
        sum=sum+int(i)
print(sum)




for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print()


for i in range(1,5):
    for j in range(1,i+1):
        print('*',end="")
    print()



s=0
n=int(input('enter number'))
n1=str(n)
for i in n1:
    s+=int(i)**len(n1)
if s==n:
      print('armstrong')
else:
        print("not armstrong")



k=3*2
for i in range(1,5):
     #Code for spacing
     for p in range(1,k+1):
         print(end=' ')


     #for printing stars
     for j in range(1,i+1):
          print('*',end='   ')
     k=k-2
     print()


k=1
for i in range(3,0,-1):
     #Code for spacing
     for p in range(1,k+1):
         print(end='  ')


     #for printing stars
     for j in range(1,i+1):
          print('*',end='   ')
     k=k+1
     print()