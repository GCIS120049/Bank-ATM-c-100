class atm :

    def __init__( self , card_number , pin_number ) :

        self.card_number = card_number
        self.pin_number = pin_number

    def balanceEnquiry( self ) :

        print("Your balance is: $1000")

    def cashWithdrawal( self , amount ) :
        
        new_amount = 1000 - amount
        print("Your remaining balance is " + str(new_amount))
        print("Money withdrawed: " + str(amount))

def main() :

    name = input("Hello ! What is your name ?")
    print("Hello " + name)

    card_number = input("Enter your card number: ")
    pin = input("Enter pin: ")

    new_user = atm( card_number , pin )

    print("What would you like to do today ?")
    print("Press 1 for balance enquiry")
    print("Press 2 for cash withdrawal")

    activity = int(input("Enter your choice: "))

    if activity == 1 :
        new_user.balanceEnquiry()
    else :
        amount = int(input("Enter amount you want to withdraw :"))
        new_user.cashWithdrawal(amount)

main()