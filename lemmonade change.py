bills=[5,5,5,1,20]
five=0
ten=0
twenty=0
for dollar in bills:
    if(dollar==5):
        five+=1
    elif(dollar==10):
         if(five>0):
             ten+=1
             five-=1
         else:
             print("False")
    elif(dollar==20):
        if(five>0 and ten>0):
            five-=1
            ten-=1
        elif(five>=3):
            five-=3
        else:
            print("False")
    print("true")
