with open("input.txt", "r+") as file:
    file.seek(0)
    text = file.readlines()

#storing goodies and price values

goodies_list=[]
price_list=[]
m=int(input('Number of employees: '))
for i in text:
    temp=str(i).split(":")
    goodies_list.append(temp[0])
    price_list.append(int(str(temp[1]).strip().split('\n')[0]))

print(goodies_list)

#sorting the lists

for i in range(len(price_list)):
    for j in range(i+1,len(price_list)):
        if price_list[j]<price_list[i]:
            temp=price_list[j]
            price_list[j]=price_list[i]
            price_list[i]=temp
            goodies_list[i],goodies_list[j] = goodies_list[j],goodies_list[i]

            

ans = price_list[m-1] - price_list[0]
index = 0

t = len(price_list)

for i in range(1,t-m-1):
    temp = price_list[i+m-1] - price_list[i]
    if temp < ans:
        ans = temp
        index = i
        
f = open("output.txt", "w")
f.write("Number of Employees:  "+str(m)+"\n")
f.write("\nSelected goodies:\n")
for j in range(index,index+m):
    f.write(str(goodies_list[j])+' : '+str(price_list[j])+'\n')
f.write("\nThe difference between the chosen goodie with highest price and the lowest price is "+str(ans)+"\n")
f.write("\n")
f.close()

print("\nOutput.txt\n")
f = open("output.txt", "r")
print(f.read())

print("\nDifference=",ans)        
