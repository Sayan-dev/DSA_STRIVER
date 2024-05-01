import sys
class Solution:

    def stockBuyAndSell(self, stocks: list[int]):
        # Write your code here
        min_item = sys.maxsize
        max_pro = 0

        for i in range(len(stocks)):
            min_item = min(min_item, stocks[i])
            max_pro = max(stocks[i] - min_item, max_pro)



        return max_pro