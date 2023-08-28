
##################################################################################
## Get user input for annual_salary, percent_saved and total_cost_of_home below ##
##################################################################################


annual_salary = float(input("Enter the annual salary: "))
percent_saved = float(input("Enter the percent of salary to be saved (decimal): "))
total_cost_of_home = float(input("Enter the total cost of your dream home: "))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################



percent_down_payment = 0.25 * total_cost_of_home    # the percentage of the total cost needed for a down payment
amount_saved = 0                                    # amount that you have saved at months = 0
months = 0                                          # initial month
r = 0.05                                            # annual rate of return
total_savings = percent_saved * (annual_salary / 12) # your savings increase by a percentage of your monthly salary and the monthly return on your investment


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################


while (amount_saved <= percent_down_payment):       #while loop to execute commands as long as a certain condition is met
    months += 1
    amount_saved += total_savings + (amount_saved * r) / 12
print(months, "months required to save for the down payment")


