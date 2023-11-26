class Solution:

    def stockBuyAndSell(self, stocks: list[int]):
        # Write your code here
        sorted_stocks = stocks.copy()
        sorted_stocks.sort()
        minim=sorted_stocks[0]

        min_index= 0
        
        max_pro = 0

        for i in range(1,len(stocks)):
            if stocks[i]==minim: 
                min_index = i
                break

        for i in range(min_index, len(stocks)):
            if stocks[i]-stocks[min_index] > max_pro:
                max_pro = stocks[i]-stocks[min_index]


        return max_pro