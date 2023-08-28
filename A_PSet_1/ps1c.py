
##############################################
## Get user input for initial_deposit below ##
##############################################


initial_deposit = float(input("Enter the initial amount in your savings account: "))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################


total_cost_of_home = 800000                              # provided variable
down_payment = total_cost_of_home * 0.25                 # provided variable
months = 36                                              # provided variable

steps = 0                                   # how many 'guesses' are necessary to figure out 'r'
low = 0
high = 1
r = (high + low) / 2
amount_saved = initial_deposit * (1 + r / 12) ** months


##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

# one way: max amount saved in 36 months and compare to define r

while abs(amount_saved - down_payment)>=100:                    #bisectional search
    amount_saved = initial_deposit * (1 + r / 12) ** months     #formula that contains `r`
    if  amount_saved < down_payment - 100 and months<=36:       #e.g. down payment is $1000, the total amount is up to $900
        low = r                                                 #low boundary of bisectional search
        amount_saved = 0.
    elif amount_saved > down_payment + 100 and months<=36:      #e.g. down payment is $1000, the total amount is up to $1100
        high = r                                                #high boundary of bisectional search
        amount_saved = 0.
    if steps > 12 or months>36:                                 # 12 is the number obtained in the PART C Tests 1 and 2
        r = None                                                # Add None to the ratio
        break                                                   #stop the loop
    r = (low+high) / 2
    steps = steps +1

print("Best saving rate: ", r)
print("Number of steps: ", steps)
