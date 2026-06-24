#1
n=int(input("Enter a number between 1 and 100:"))
for i in range(1,n+1):
    if i%9==0:
        break
    if i%3==0:
        continue
    print(i)


#2
n=int(input("Enter a number:"))
while n>=1:
    if n==5:
        pass
    print(n)
    n=n-1


#3
word="python"
for ch in word:
    if ch=="h":
        continue
    print(ch)


#4
n=20
while n>=1:
    if n==17:
        n=n-1
        continue
    if n==13:
        break
    print(n)
    n=n-1
