print("**** All Logic Program ****")
q=1
while q==1:
     print("\n*** 1. Odd number generation****")
     print("*** 2. Even number generation****")
     print("*** 3. Prime number generation****")
     print("*** 4. leap Year  generation****")
     print("*** 5. Factorial Program Check****")
     print("*** 6. Armstrong number generation****")
     print("*** 7. Pascal Triangle Star Pattern****")
     print("*** 8. Flody Triangle Star Pattern****")
     print("*** 9. Fibonacci Series Number Generation****")
     print("*** 0. Exit****")
     choice=int(input("Please choose your choice"))
     if choice==1:
          print("***** Odd Number Generation*******")
          n = int(input("Please enter nth term"))
          for i in range(1,n+1):
               if i%2==1:
                    print(i,end='      ')
          q=int(input("Do u want to choice Press 1 or Exit Press 0....\t"))
     elif choice==2:
          print("***** Even Number Generation*****")
          n = int(input("Please enter nth term"))
          for i in range(1,n+1):
               if i%2==0:
                    print(i,end='      ')
          q=int(input("Do u want to choice Press 1 or Exit Press 0....\t"))
     elif choice==3:
          print("***** Prime Number Generation*******")
          n = int(input("Please enter nth term"))
          for i in range(1,n+1):
               count=0
               for j in range(1,i+1):
                    if i%j==0:
                         count = count + 1
               if count==2:
                    print(i,end='      ')
          q=int(input("Do u want to choice Press 1 or Exit Press 0....\t"))
     elif choice==4:
          print("*****Leap Year Generation******")
          n = int(input("Please enter nth term of Year"))
          for i in range(2000,n+1):
               if i%4==0 and i%100!=0:
                    print(i,end='     ')
          q=int(input("Do u want to choice Press 1 or Exit Press 0....\t"))
     elif choice==5:
          print("***** Factorial Number Check******")
          n = int(input("Please enter Nth Term"))
          fact=1
          for i in range(1,n+1):
               fact = fact * i
          print('Factorial Number value is ',fact)
          q=int(input("Do u want to choice Press 1 or Exit Press 0....\t"))
     elif choice==6:
          print("***** Armstrong Number Generation ******")
          n = int(input("Please enter Nth Term"))
          for i in range(1,n+1):
               n1 = i
               summ=0
               while n1 != 0:
                    m = n1 % 10
                    summ = summ + ( m ** 3)
                    n1 = n1 // 10
               if i==summ:
                    print(i,end='      ')
          q=int(input("Do u want to choice Press 1 or Exit Press 0....\t"))
     elif choice==7:
          print("*** Pascal Triangle Star Pattern*****")
          m =0
          p = int(input("Please enter N th term"))
          while m<p:
               for r in range(0,50-3*m):
                    print(' ',end='')
               for x in range(0,m+1):
                    if x==0:
                         bin=1
                    else:
                         bin=bin*(m-x+1)//x
                    print('     *',end='')
               m = m +1
               print()
          q=int(input("Do u want to choice Press 1 or Exit Press 0....\t"))
     elif choice==8:
          print("********* Floyd triangle Star Pattern *******")
          n=int(input("Please enter Nth Term"))
          for i in range(1,n+1):
               for j in range(1,i+1):
                    print("* ",end='')
               print()
          q=int(input("Do u want to choice Press 1 or Exit Press 0....\t"))
     elif choice==9:
          print("**** Fibonacci Series ******")
          n = int(input("Please enter Nth Term"))
          a=0
          b=1
          for i in range(1,n+1):
               c=a+b
               print(c,end='     ')
               a=b
               b=c
          q=int(input("Do u want to choice Press 1 or Exit Press 0....\t"))
     elif choice==0:
          print("***** Bye Bye !!!!!!")
          break
          
                    
     
