"""
// Time Complexity : O(N)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
Algorithm Explanation
Given below
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Since we don't know the exact number of candies to be distributed and there are 2 conditions need to be considered in distribution, we can consider 1 candy as minimal base for all children
        - Left pass (from left)
            - Increment the candy count for each child for which left child is of less rating
        - Right pass (from right)
            - Increment the candy count for each child for which right child is of less rating
        """
        candies = [1] * len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1
        return sum(candies)