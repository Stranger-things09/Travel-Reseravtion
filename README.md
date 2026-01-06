# Velvet Valet: Hotel Reservation System 🏨

### 📌 Project Overview
**Velvet Valet** is a Python-based command-line interface (CLI) tool designed to simulate a travel agency booking system. Developed as part of the **IS-340 Business Application Programming** curriculum, this program automates the calculation of travel costs, including multi-tier hotel options, vehicle rentals, tax computations, and loyalty program discounts.

### 💼 Business Logic & Problem Solved
Manual calculation of travel itineraries often leads to errors in tax application and discount eligibility. This program ensures operational accuracy by:
* **Automating Cost Calculation:** Instantly computes subtotals for variable lengths of stay.
* **Dynamic Logic:** Applies conditional logic to determine if a customer qualifies for a 10% "Travel Club" discount.
* **Financial Accuracy:** Automatically calculates a 9.5% tax rate and formats all outputs to standard currency format (`$X,XXX.XX`).

### 🛠️ Technical Implementation
Built using **Python 3**, this project demonstrates proficiency in core programming concepts essential for business logic:
* **Control Flow:** Utilizes `while` loops to allow continuous operation and `if-elif-else` structures for menu navigation.
* **Input Validation:** Includes error handling to catch invalid menu inputs (e.g., selecting a hotel that doesn't exist).
* **Mathematical Operations:** Performs compound calculations (Rate × Nights + Car + Tax - Discount).
* **String Formatting:** Uses f-strings to ensure professional, readable financial output.
* **Libraries:** Integrates the `datetime` module to timestamp reservations.

### 💻 How to Run
1.  Ensure you have Python installed.
2.  Clone this repository.
3.  Run the script in your terminal:
    ```bash
    python hotel_reservation.py
    ```

### 📄 Sample Output
*Below is an example of the program calculating a stay at the Ritz Carlton with a car rental and a member discount.*

```text
Welcome to Velvet Valet - your personal travel reservation assistant.
Here we specialize in providing the concierge comfort and curbside keys

2025-09-29 14:30:00.123456

H - Hyatt:            $630 per night
S - St Regent:       $1760 per night
R - Ritz Carlton:    $2599 per night
Q - Quit

Please choose any one: r
How many nights will you be staying? 3
Do you want to rent out a car? Y/N: y
For how many days will you be needing the car? 3

         Subtotal         
Rental Car      =  $285.00
Hotel Total     =  $7,797.00
Subtotal        =  $8,082.00

Are you a travel club member? Y/N: y

             Summary                 
Rental Car          =  $285.00
Hotel Total         =  $7,797.00
Discount amount     =  $884.98
Tax(9.5%)           =  $767.79
Total               =  $7,964.81

Do you want to make another reservation?(Y/N): n

Thank you & Goodbye
