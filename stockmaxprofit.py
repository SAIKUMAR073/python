#Question:Maximize profit from stock
#Say you have an array, A, for which the ith element is the price of a given stock on day i.
#If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
#design an algorithm to find the maximum profit.Return the maximum possible profit.
#Note: Short sell is not allowed, i.e. you must buy a stock before selling it.

#Input Format:
#First line specifies the number of days
#Second line contains a comma-separated list of prices (integers)
#Output Format:
#Return an integer, representing the maximum possible profit
#sample input
#5 -->size
#1,4,5,2,4  --> comma separated input
#sample output
#4 -->maxprofit
#Explanation
#buy the stock on day0 and sell it on day2.



def maxprofit(n,y):
    max_profit = 0     #variable to store maximize profit
    list1 = list(y)    #converting comma separated input to list for process
    list2 = []         #to store amount we got if we by stock on ith day and sell it on i+1,i+2 ...th days
    for i in range(0,n):
        for j in range(i,n-1):
            list2.append(int(list1[j+1]) - int(list1[i]))
        max_profit = max(list2)
    if(max_profit >= 0):
        print(max_profit)
    else:
        print("no profit")
    

n = int(input("size"))  #size i.e no.of days
y = input().split(",")  #Comma separated input
maxprofit(n,y)          #function call
