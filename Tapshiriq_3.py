print("Kalkulyator\n")
a=int(input("a regemini daxil edin"))
b=int(input("b regemini daxil edin"))
funksiya=int(input("Funksiyani sechin: 1-Toplama\n 2-Chixma\n 3-Vurma\n 4-Bolme\n 5-EBOB tapma\n 6-EKOB tapma\n 7-Toplamin faktoriali"))

if funksiya == 1:
    print("1-ci funksiya sechildi")
    c=a+b
    print("Neticeniz",c)
elif funksiya == 2:
    print("2-ci funksiya sechildi")
    c=a-b
    print("Neticeniz",c)  
elif funksiya == 3:
    print("3-cu funksiya sechildi")
    c=a*b
    print("Neticeniz",c)  
elif funksiya == 4:
    print("4-cu funksiya sechildi")
    c=a/b
    print("Neticeniz",c)      
elif funksiya == 5:
    print("5-ci funksiya sechildi")    
    while max(a, b) % min (a, b) != 0:
        if a>b:
            
              a = a%b
        elif a<b:
            
              b = b%a
              print (min(a,b))
elif funksiya == 6:
    print("6-ci funksiya sechildi")    
    for i in range(max(a,b), 1 + (a * b)):
        if i % a == i % b == 0:
            EKOB = i
            print("EKOB=",EKOB)
elif funksiya == 7:
    print("7-ci funksiya sechildi") 
    def factorial(n):
	    result = 1
	    for i in range(1,n+1):
		      result = result*i    
        return result
        n = a + b
        result = factorial(n)
        print(n,'! = ',result,sep="")
    

