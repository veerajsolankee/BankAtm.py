class Atm:
    def _init_(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 50,000")


    def withdrawl(self,amount):
        new_amount = 50,000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaing balance  is "+str(new_amount))


def main():
    Card_number = input("insert you card:- ")
    pin_card    = input("enter your pin number:- ")

    new_user = Atm(Card_number , pin_number)


    print("Choose your activity ")
    print("1.Balance Enquiry   2.withdrawl")

    if (withdrawl == 1):
        new_user.check_balance()
    else (withdrawl -> 2):
        print("enter a valid number")

 if__name__"__main__":
main()
