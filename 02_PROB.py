index=1
n=5
while(index<6):
    if index%2==0:
        print(f"{index+1}",end="")
        print(f"{index}"*(n-1))
    
    else:
        print(f"{index}"*(n-1),end="")
        print(f"{index+1}")
    index+=1
