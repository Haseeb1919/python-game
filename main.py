
import random

#global variable
MAX_LINES = 3
MIN_BET = 50

#global variable for game board
ROWS = 3
COLS = 3

symbol_count = {

    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8,

}

symbol_value = {

    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2,

}



#fuction to check wining
def check_win(columns, lines, bet,values):
    winnings = 0
    winnings_lines = []

    # Check if all the symbols in the line are the same
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    
    return winnings, winnings_lines





#function to spin the machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


#function to print the machine spin
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()



#collecting user deposit information
def deposit():
    while True:
        
            deposit_amount = input("How much would you like to deposit? ")
            if deposit_amount.isdigit():
                deposit_amount = int(deposit_amount)
                if deposit_amount > 0 :
                    break
                else:
                    print("Please enter the amount greater then 0")
            else:
                print("Please enter a number")
      
    #setting global variable of MAX_BET equal to deposit amount
    global MAX_BET
    MAX_BET = deposit_amount
    return deposit_amount

   


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


#collecting bet information
def get_bet(deposit_amount):
    while True:
        amount = input(f"How much would you like to bet mimimum range = {MIN_BET}, maximum range = {MAX_BET}? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                if amount <= deposit_amount:
                    break
                else:
                    print("Your bet cannot exceed your deposit amount.")
            else:
                print(f"Please enter the amount between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a number")
    return amount




def game(amount):  # Add 'amount' as an argument
    lines = number_of_line()
    bet = get_bet(deposit_amount=amount)
    total_bet = bet * lines

    # Check if the total bet exceeds the deposit amount
    while total_bet > amount:
        print("Your total bet amount exceeds your deposit amount. Please place your bets again your deposit amount is " + str(amount) + ".")
        lines = number_of_line()
        bet = get_bet(amount)
        total_bet = bet * lines

    # Print the bet information
    print("You have deposited " + str(amount) + " and you are betting on " + str(lines) + " lines with " + str(bet) + " each and total bet is equal to "+str(total_bet)+  ".")
    
    #spining machine and printing the result
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    # Check if the user won print the winnings and the winning lines
    winnings, winnings_lines = check_win(slots, lines, bet,symbol_value)
    print("You won: " + str(winnings) + "!")
    print("You won on lines: " + str(winnings_lines) + "!")

    return winnings_lines - total_bet


#main function
def main():
    amount = deposit()
    while True:
        print("You have " + str(amount) + " in your account.")
        spin = input("Would you like to spin? (Y/N) ")
        if spin.lower() == "y":
            # Pass 'amount' to 'game()' function
            amount += game(amount)
        elif spin.lower() == "n":
            print("You have " + str(amount) + " in your account.")
            break
    
    print("Thank you for playing!")

if __name__ == "__main__":
    main()





























# def game(amount):

#     lines = number_of_line()
#     bet = get_bet(deposit_amount=amount)
#     total_bet = bet * lines

#     # Check if the total bet exceeds the deposit amount
#     while total_bet > amount:
#         print("Your total bet amount exceeds your deposit amount. Please place your bets again your deposit amount is " + str(amount) + ".")
#         lines = number_of_line()
#         bet = get_bet(amount)
#         total_bet = bet * lines

#     # Print the bet information
#     print("You have deposited " + str(amount) + " and you are betting on " + str(lines) + " lines with " + str(bet) + " each and total bet is equal to "+str(total_bet)+  ".")
    
#     #spining machine and printing the result
#     slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
#     print_slot_machine(slots)

#     # Check if the user won print the winnings and the winning lines
#     winnings, winnings_lines = check_win(slots, lines, bet,symbol_value)
#     print("You won: " + str(winnings) + "!")
#     print("You won on lines: " + str(winnings_lines) + "!")

#     return winnings_lines - total_bet






# #main function
# def main():
#     amount = deposit()
#     while True:
#         print("You have " + str(amount) + " in your account.")
#         spin = input("Would you like to spin? (Y/N) ")
#         if spin.lower() == "y":
#             amount += game()
#         elif spin.lower() == "n":
#             print("You have " + str(amount) + " in your account.")
#             break
    
#     print("Thank you for playing!")
    
# main()