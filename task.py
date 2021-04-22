
import random


class bank():
    def __init__(self,name="kemal",surname="cetinakay",password=1234,balance=7900,thebankname="bnp",banksnames=["ing","bnp","ziraat"]):
        self.name=name
        self.surname=surname
        self.password=password
        self.balance=balance
        self.banksnames=banksnames
        self.thebankname=thebankname
    def money(self):
        while True:
            answer=input("if you want to withdrawal please press'-'for deposite press '+'")
            if (answer== '-'):
                if (self.balance<=5):
                    break
                else:
                    value=int(input("the value you want to withdrawal"))
                    self.balance-=value
            
            elif(answer=='+'):
                value=int(input("the value you want to deposite"))
                self.balance+=value
            
            else:
                break
    
    def changingbank(self):
        randomly = random.randint(0,len(self.banksnames)-1)
        self.thebankname=self.banksnames(randomly)
    

class customer(bank):
        def __init__(self,name,surname,credit,password,balance,thebankname="bnp",banksnames=["ing","bnp","ziraat"]):
            super().__init__(name="kemal",surname="cetinakay",password=1234,balance=7900,thebankname="",banksnames=["ing","bnp","ziraat"])
            self.credit=credit

        def discharge(self):
            answer2=input("if you want to pay your kredit press 'pay'; if you want some extra credit press'yes' ")
            while True:
                if (answer2=='pay'):
                    moneyvalue=int(input("write your payment"))
                    self.credit-=moneyvalue
                    return self.credit #?
                
                elif(answer2=='yes'):
                    if (self.kredit<=-2000):
                        break
                    else:
                        moneyvalue=int(input("write your payment"))
                        self.credit+=moneyvalue
                        return self.credit # ?
                
                else:
                    break
                    
        def moneytransfer(self):
            transferred=int(input("how much that you want to sent "))
            self.balance-=transferred
            
        def __str__(self):
            return "name:{}\nsurname:{}\npassword:{}\nbalance:{}\nthebankname:{}\ncredit:{} ".format(self.name,self.surname,self.password,self.balance,self.thebankname,self.credit)
        

            
customer1 =customer("kemal","cetinkaya",7800,13213,7000)                
print("""

1)deposit and  withdrawal

2) changing bank

3)credit transactions

4)money transfer

5) information

6) delete account

getting out press 'q'
""")

while True:
    process=input("enter your process")
    if(process=='q'):
        break
    elif(process=='1'):
        customer1.money()
        
    elif(process=='2'):
        customer1.changingbank()
    elif(process=='3'):
        customer1.discharge()
    elif(process=='4'):
        customer1.moneytransfer()
    elif(process=='5'):
        print(customer1)
    elif(process=='6'):
        del(customer1)
        print("your account is deleted")
    else:
        print("unused digit")

                    
                
        
            
            
        
