
##################################################################################################
## Get user input for annual_salary, percent_saved, total_cost_of_home, semi_annual_raise below ##
##################################################################################################


annual_salary = float(input("Enter the annual salary: "))
percent_saved = float(input("Enter the percent of salary to be saved (decimal): "))
total_cost_of_home = float(input("Enter the total cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual salary raise (decimal)"))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################


percent_down_payment = 0.25 * total_cost_of_home    # the percentage of the total cost needed for a down payment
amount_saved = 0                                    # amount that you have saved at months = 0
months = 1                                          # initial month THIS IS DIFFERENT FROM PART A bacause the month start at Jan for the calculation
r = 0.05                                            # annual rate of return


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################


while (amount_saved <= percent_down_payment):       # while loop to execute commands as long as a certain condition is met
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
    amount_saved += ((percent_saved * (annual_salary / 12)) + ((amount_saved)* r)/ 12)
print(months, "months required to save for the down payment")






