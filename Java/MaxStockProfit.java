// Problem
/*
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
*/

// Notes & Working Outs
/*
Constraints:
Prices length 1 <= prices.length < 10^5
Prices 0 <= prices[i] <= 10^4
Max Profit 0 <= Max Profit <= 10^4

Input/Output:
Input Array - List of Integers
Output Int - Max Profit -> Sell - Buy = Profit

Explanation:
We can't sell before buying. There's no need to check before buying the price.

1,1,1,1
4,2,3,1
These produce 0 profit because the stock never increases.
That means the price we buy will always be larger (or the same as) how much we can sell it.
We can only get zero or negative profit.

Rules:
- Find the highest positive difference between the two numbers.
- In the array order, The buying price (int) should be before the selling price (int).

Default Max Profit is 0. Where nothing is brought or sold.

For each price, we check if it's the cheapest we can buy.
If it is, it becomes our buying price then we continue.
Else, it could be our selling price.
It's our selling price if the profit (selling price - buying price) is more profitable than our current max profit.
If it is, that becomes our new max profit.
After the loop, return the max profit.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
*/
        
class Solution {
    public static void main(String[] args) {
        testSolution();
    }

    // Solution
    private static int maxProfit(int[] prices) {
        int maxProfit = 0;
        int smallestBuying = 10_000; // Smallest you can buy
        
        for (int i=0; i<prices.length; i++) {
            // Set new smallestBuying if price[i] is smaller
            if (prices[i] < smallestBuying) {
                smallestBuying = prices[i];
                // We don't need to compare the prices before smallestBuying because we can't sell before we buy
                continue;
            }
            
            int currentProfit = prices[i] - smallestBuying; // Current profit (Price we sell - Price we brought)

            // Set new maximum profit if currentProfit is bigger
            if (maxProfit < currentProfit)
                maxProfit = currentProfit;
            }
        
        // Return maxProfit
        return maxProfit;
    }

    // Test
    private static void testSolution() {
        // Setup Test Cases'
        int[][] testPrices = {
            {15,24,20,11,22},
            {9,1,9},
            {1,2,3,4,5,6},
            {6,5,4,3,1},
            {6},
            {3,3,3,3},
            {7,1,5,3,6,4}
        };

        int[] testAnswers = {11,8,5,0,0,0,5};

        // Display Results
        for (int i=0;i<testPrices.length;i++) {
            int solutionOutput = maxProfit(testPrices[i]);

            System.out.print(String.format("\nTest Case %d - ", i+1));
            System.out.println(String.format((solutionOutput==testAnswers[i])?"Passed":"Failed"));
            System.out.println(String.format("---\nExpected Result: %d", testAnswers[i]));
            System.out.println(String.format("Solution's Result: %d\n", solutionOutput));
        }
    }
}