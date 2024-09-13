class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        res = []
        max = candies[0]
        for candy in candies[1:]:
            if max < candy:
                max = candy

        for candy in candies:
            res.append(candy + extraCandies >= max)
        return res
