#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Ask user how much data they have used
    #Run rate calculation(s) depending on how many mbs of data they used
    #Based on rate, calculate total data cost

    #input amount of data
    Data=float(input("How many mbs of data did you use?"))

    #if under 200 or 200mb of data, flat rate of $20.00
    if Data < 200 or Data==200:
        RateOfCharge=20.00
        FlatDataCost=RateOfCharge
        print("Your total data cost is:",FlatDataCost)

    #if 200-500mb of data, rate is $0.105 per mb
    if Data > 200 or Data==500:
        RateOfCharge=0.105
        PerDataCost=Data*RateOfCharge
        print("Your total data cost is:",PerDataCost)

    #if over 500-1000mb of data, rate is $0.110 per mb
    if Data > 500 or Data==1000:
        RateOfCharge=0.110
        PerDataCost=Data*RateOfCharge
        print("Your total data cost is:",PerDataCost)

    #if over 1000mb of data, flat rate of $118
    if Data > 1000:
        RateOfCharge=118
        FlatDataCost=RateOfCharge
        print("Your total data cost is:",FlatDataCost)

    # YOUR CODE ENDS HERE

main()