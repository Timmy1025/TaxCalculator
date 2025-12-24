# Program to calculate 2009 US Federal Income Tax
# Based on filing status and taxable income

def calculate_tax():
    # 1. [span_2](start_span)Get user input for filing status[span_2](end_span)
    print("Filing Statuses:")
    print("0 - Single")
    print("1 - Married Filing Jointly / Qualified Widow(er)")
    print("2 - Married Filing Separately")
    print("3 - Head of Household")
    
    try:
        status = int(input("Enter the filing status (0-3): "))
        income = float(input("Enter the taxable income: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    # 2. [span_3](start_span)Define tax brackets based on the 2009 table[span_3](end_span)
    # Brackets are organized by status index to match the user input
    brackets = [
        [8350, 33950, 82250, 171550, 372950], # 0: Single
        [16700, 67900, 137050, 208850, 372950], # 1: Married Joint
        [8350, 33950, 68525, 104425, 186475], # 2: Married Separate
        [11950, 45500, 117450, 190200, 372950]  # 3: Head of Household
    ]
    
    rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]
    
    # Select the specific brackets for the chosen status
    current_brackets = brackets[status]
    tax = 0
    remaining_income = income

    # 3. [span_4](start_span)Calculate tax using marginal rates[span_4](end_span)
    # This loop handles the progressive nature of the tax brackets
    if remaining_income > current_brackets[4]:
        tax += (remaining_income - current_brackets[4]) * rates[5]
        remaining_income = current_brackets[4]
        
    if remaining_income > current_brackets[3]:
        tax += (remaining_income - current_brackets[3]) * rates[4]
        remaining_income = current_brackets[3]
        
    if remaining_income > current_brackets[2]:
        tax += (remaining_income - current_brackets[2]) * rates[3]
        remaining_income = current_brackets[2]
        
    if remaining_income > current_brackets[1]:
        tax += (remaining_income - current_brackets[1]) * rates[2]
        remaining_income = current_brackets[1]
        
    if remaining_income > current_brackets[0]:
        tax += (remaining_income - current_brackets[0]) * rates[1]
        remaining_income = current_brackets[0]
        
    tax += remaining_income * rates[0]

    # 4. Display the result
    print(f"The total tax is: ${tax:,.2f}")

if __name__ == "__main__":
    calculate_tax()