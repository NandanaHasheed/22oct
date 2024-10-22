temp=float(input("Enter temperature"))
option=input("Is this celsius or farenheit")
if(option=='F'):
    C=5/9*(temp-32)
    print(temp," Farenheit is",C,"Celsius.")
elif(option=='C'):
    F= (9/5*temp)+32
    print(temp,"Celsius is",F,"Farenheit.")