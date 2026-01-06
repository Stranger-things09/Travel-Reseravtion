#==========================================================================
# IS-340 Project 1
# A project on hotel reservation using math operators,
# if-elif-else statements, and while loops.
#
# Kriti Krishnan                                          September 29, 2025
#===========================================================================

Welcome=("Welcome to Velvet Valet - your personal travel reservation assistant.\n"
          "Here we specialize in providing the concierge comfort and curbside keys")
print(Welcome)

#The prices for various hotels, car rentals and taxes are given below.
Hyatt        = 630
St_Regent    = 1760 #All the prices given are per night
Ritz_Carlton = 2599
Discount = 0.10
Car_Rental = 95
Tax = 0.095
loopagain = True



while loopagain:

    # we need to input date and time
    from datetime import datetime

    now = datetime.now()
    print()
    print(f"{now}")

    #This displays the menu where the customers can choose the hotel.
    print()#gives a blank line before the string starts
    print("H - Hyatt:           $630 per night") 
    print("S - St Regent:      $1760 per night")
    print("R - Ritz Carlton:   $2599 per night")
    print("Q - Quit")
    print()

    #The code displayed below will be where the customer will enter their choice.
    choice = input("Please choose any one: ").lower()

    if choice == 'q':
        loopagain = False
        continue

    elif choice == 'h':
        nights = float(input("How many nights will you be staying? "))
        #we put float here because the input will be integers.
        Total_Hotel = Hyatt * nights

    elif choice == 's':
        nights = float(input("How many nights will you be staying? "))
        Total_Hotel = St_Regent * nights

    elif choice == 'r':
        nights = float(input("How many nights will you be staying? "))
        Total_Hotel = Ritz_Carlton * nights

    else:
        print("Opps! It is invalid. Please select any one H/S/R/Q")
        continue
        #Helps when the user puts a wrong input and this takes you to the front of the loop.

    #Now we need to add the car rental total
    need_car = input("Do you want to rent out a car? Y/N: ").lower()
    

    if need_car == 'y':
        days = float(input("For how many days will you be needing the car? "))
        Car_total = Car_Rental * days

    else:
        Car_total = 0 #This is purely for display purposes.

    Subtotal = Car_total + Total_Hotel
    Hotel_format = (f"${Total_Hotel:,.2f}")
    Car_formatted = (f"${Car_total:,.2f}")
    Formatted = (f"${Subtotal:,.2f}")
    print()
    print("         Subtotal         ")
    print("Rental Car     = ", Car_formatted)
    print("Hotel Total    = ", Hotel_format)
    print("Subtotal       = ", Formatted)
    print()

    #Now we need to compute discount for travel members
    print()
    travel_member = input("Are you a travel club member? Y/N: ").lower()
    Tax_subtotal = Subtotal * Tax
    Subtotal = Subtotal + Tax_subtotal

    if travel_member == 'y':
        travel_discount = (Subtotal * Discount)
        Subtotal = Subtotal - travel_discount
    
    else:
        travel_discount = 0
        #Now we need to show our customers how much the tax percent is and then apply it to the subtotal

    Subtotal = (f"${Subtotal:,.2f}")
    Car_total = (f"${Car_total:,.2f}")
    Total_Hotel = (f"${Total_Hotel:,.2f}")
    Tax_subtotal = (f"${Tax_subtotal:,.2f}")
    travel_discount = (f"${travel_discount:,.2f}")
    
    print()     
    print("             Summary                ")
    print("Rental Car         = ",Car_total)
    print("Hotel Total        = ",Total_Hotel)
    print("Discount amount    = ",travel_discount)
    print("Tax(9.5%)          = ",Tax_subtotal)
    print("Total              = ",Subtotal)
    print()

    #After one reservation is complete, we should as the user if they want to continue or quit
    Last = input("Do you want to make another reservation?(Y/N): ").lower()

    if Last == 'y':
        continue

    else:
        break
print()
print("Thank you & Goodbye")

    

    





               
