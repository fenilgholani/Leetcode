class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        r = 0
        rem = numBottles
        while numBottles >= numExchange:

            r = numBottles % numExchange
            rem += numBottles // numExchange
            # print(rem)
            numBottles = numBottles // numExchange + r

        return rem