# Capstonme project - Variables and Control structures
import math
#Write a program to calculate the interest for a home loan or investment depending on user inputs

#print financial options to user and ask user to choose one
print("Investment \t - to calculate the amount of interest you'll earn on your investment.")
print("Bond \t \t - to calculate the amount you'll have to pay on a home loan.")

finance_option = input("Enter either 'Investment' or 'Bond' from the menu above to proceed : ")
print("\n") #new line to make output more readible

#determin which formula to run depending on user's choice.

if(finance_option == "Investment") or (finance_option == "investment") or (finance_option == "INVESTMENT") :
    
    #ask user to input necessary integers for formula 
    invest_amount = int(input("What is the amount you would like to invest? \n (Only enter a numerical value) : "))
    invest_interest = int(input("Please enter an interest rate percentage for your investment, \n (Only enter a numerical value) : ")) / 100 
    #divided input to get percetage for interest formula
    invest_time = int(input("Over how many years would you like your investment to grow? \n (Only enter a numerical value) : "))
    
    print("\n") #new line to make output more readible
    
    #ask user to choose between simple and compound interest to calculate correct formula
    invest_option = input("Would you like to make a Simple or Compound investment? : ")

    print("\n") #new line to make output more readible

    #determin necessary formula depending on user choice and print answer
    if(invest_option == "Simple") or (invest_option == "simple") or (invest_option == "SIMPLE") :
        return_answer = invest_amount * (1 + invest_interest * invest_time)
        print(return_answer)
    
    elif(invest_option == "Compound") or (invest_option == "compound") or (invest_option == "COMPOUND") :
        return_answer = invest_amount * math.pow((1 + invest_interest), invest_time)
        print(f"Investment return : \t {return_answer}")

elif(finance_option == "Bond") or (finance_option == "bond") or (finance_option == "BOND") :
    
    #ask user to input necessary integers for formula
    bond_amount = int(input("What is the value of the house you want to buy? \n (Only enter a numerical value) : "))
    bond_interest = int(input("Please enter the interest rate percentage for you home loan, \n (Only enter a numerical value) : "))
    bond_interest = (bond_interest / 100) / 12 #divided by 100 to get float percentage then divided by 12 to get monthly float percentage - necessary for bond formula
    bond_months = int(input("Over how many months you would like repay your home loan? \n (Only enter a numerical value) "))

    print("\n") #new line to make output more readible

    #calculate bond repayment
    repayment = (bond_interest * bond_amount)/(1 - (1 + bond_interest)**(-bond_months))
    print(f"Monthly repayment : \t {repayment}")

else:
    print("Your input was invalid.")
