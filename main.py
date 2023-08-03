#global variable
MAX_LINES = 3


#collecting user deposit information
def deposit():
    while True:
        
            amount = input("How much would you like to deposit? ")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0 :
                    break
                else:
                    print("Please enter the amount greater then 0")
            else:
                print("Please enter a number")
      

    return amount


#collecting line information to bet on 
def number_of_line():
    while True:
        
            lines = input("On which line you want to bet on (1-" +str(MAX_LINES)+ ")? ")
            if lines.isdigit():
                lines = int(lines)
                if  1 <= lines <= MAX_LINES:
                    break
                else:
                    print("Please enter the number from the range.")
            else:
                print("Please enter a number")
      

    return lines



def get_bet():
    while True:
        bet = input("How much would you like to bet? ")
        if bet.isdigit():
            bet = int(bet)
            if bet > 0:
                break
            else:
                print("Please enter the amount greater then 0")
        else:
            print("Please enter a number")
    return bet



#main function
def main():
    amount = deposit()
    lines = number_of_line()
    print("You have deposited " + str(amount) + " and you are betting on " + str(lines) + " lines.")



main()