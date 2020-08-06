class bank:
    def __init__(self,acno,acholdername,apin,abalance,atype):
        self.account_no = acno
        self.account_holdername=acholdername
        self.account_pin=apin
        self.account_balance=abalance
        self.account_type=atype
    def process(self,p2):
        bank=1
        while bank==1:
            print('********** Welcome To HDFC Bank *************')
            print('1. Deposit')
            print('2. Withdraw')
            print('3. Transfer')
            print('4. Balance')
            print('5. Exit')
            choice = int(input('please enter your choice'))
            if choice==1:
                print('** Welcome to Deposit section**')
                accno = input("Please enter Your ACCOUNT number")
                accpin = input("Please enter Your ACCOUNT pin")
                if accno==self.account_no:
                    if accpin==self.account_pin:
                        damount=int(input('please enter ur deposit amount'))
                        self.account_balance=damount + self.account_balance
                        print('Successfully deposited')
                    else:
                        print('Sorry !!! Incorrrect Pin')
                else:
                    print('Sorry !!! Incorrect Account Number')
                bank=int(input('Do u want to Continue Press 1 or exit press 0......................'))
            elif choice==2:
                print('** Welcome to WithDraw**')
                accno = input("Please enter Your ACCOUNT number")
                accpin = input("Please enter Your ACCOUNT pin")
                if accno==self.account_no:
                    if accpin==self.account_pin:
                        wamount=int(input('please enter ur widthdrawl amount'))
                        if wamount>self.account_balance:
                            print('InSufficient Balance in Your Account')
                        else:
                            print('Please wait .. Ypur Transaction is Processing.......')
                            self.account_balance=self.account_balance-wamount
                            print('Successfully Processed')
                    else:
                        print('Sorry !!! Incorrrect Pin')
                else:
                    print('Sorry !!! Incorrect Account Number')
                bank=int(input('Do u want to Continue Press 1 or exit press 0......................'))
            elif choice==3:
                print('** Welcome to Transfer**')
                accno = input("Please enter Your ACCOUNT number")
                accpin = input("Please enter Your ACCOUNT pin")
                if accno==self.account_no:
                    if accpin==self.account_pin:
                        taccno=input('please enter transfer account holder number')
                        if taccno==p2.account_no:
                            print('Account Verified Successfully')
                            amount=int(input('please enter transfer amount'))
                            if amount>self.account_balance:
                                print('Sorry !! Insufficient Balance to transfer')
                            else:
                                p2.account_balance=amount+p2.account_balance
                                self.account_balance=self.account_balance-tamount
                                print('Successfully Transferred')
                        else:
                            print('Sorry !!! Account Number is not verified or incorrect')
                    else:
                        print('Sorry !!! Incorrrect Pin')
                else:
                    print('Sorry !!! Incorrect Account Number')
                bank=int(input('Do u want to Continue Press 1 or exit press 0......................'))
            elif choice==4:
                print('** Welcome to Balance**')
                print('Your Current Account Balance is ............:         ' , self.account_balance)
                bank=int(input('Do u want to Continue Press 1 or exit press 0......................'))
            elif choice==5:
                print('**** Thanks for using HDFC Bank ****')
                break
    def display(self):
        print('Account Number ' , self.account_no)
        print('Account HolderName ' ,self.account_holdername)
        print('Account pin ' , self.account_pin)
        print('Account Balance ' ,self.account_balance)
        print('Account Type ',self.account_type)
person1 =bank('1234567890','kumar','1111',5000,'savings')
person2 =bank('0987654321','naveen','2222',7000,'savings')
person1.process(person2)
#person1.display()
#person2.display()
