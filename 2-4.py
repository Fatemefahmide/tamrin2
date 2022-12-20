a = 0
sum = 0
count = 0

while True:
    b = input("please enter number: ")
    #if you dont want to enter numbers,type exit to exit and the sum of the numbers will be shown to you
    if b == exit :
        print(sum)
        break

    count = count+1
    a = int(b)
    sum = sum+a