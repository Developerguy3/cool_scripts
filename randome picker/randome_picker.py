from random import randint
print( "how many option do you want to enter:-" )
size = int(input())
print("enter the your choices:-")
lists = []

for item in range(size):
    x = input(f"enter the {item+1} value:-")
    lists.append(x)

genrater = randint(0,size)
for i in range(size):
    if genrater == i:
        ans = lists[i]

print(ans)

faltu = input()
