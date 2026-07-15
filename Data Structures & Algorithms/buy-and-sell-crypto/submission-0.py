class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 0
        min_price = 101
        answer = 0

        for price in prices:
            min_price = min(min_price, price)
            answer = max(price - min_price, answer)
        
        return answer

                
