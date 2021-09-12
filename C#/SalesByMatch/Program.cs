/*
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, given 7 socks of values [ 1, 2, 1, 2, 3, 1]
*/

using System;
using System.Collections.Generic;
using System.Linq;

namespace SalesByMatch
{
    class Program
    {
        static void Main(string[] args)
        {
            TestSolution();
        }

        static int SalesByMatch(int numberOfSocks, IEnumerable<int> socksColor)
        {
            // Check there's more than 2 socks, otherwise it'll always be 0
            if (numberOfSocks < 2)
            {
                return 0;
            }

            IEnumerable<int> colors = socksColor.Distinct();
            int totalPairs = 0;

            foreach (int color in colors)
            {
                totalPairs += socksColor.Count(x => x == color) / 2;
            }

            return totalPairs;
        }

        static void TestSolution()
        {
            int[] numberOfSocks = new[] { 7, 10, 1, 8, 2, 3, 0 };
            var socksColors = new List<int[]>
            {
                new int[] { 1, 2, 1, 2, 1, 3, 1 },
                new int[] { 10, 20, 20, 10, 10, 30, 50, 10, 20 },
                new int[] { 2 },
                new int[] { 3, 1, 33, 2, 11, 34, 42, 45 },
                new int[] { 5, 5 },
                new int[] { 1, 1, 1 },
                new int[] {}
            };

            int[] expectedResult = new[] { 3, 3, 0, 0, 1, 1, 0 };

            for (int i = 0; i < numberOfSocks.Length; i++)
            {
                int actualResult = SalesByMatch(numberOfSocks[i], socksColors[i]);

                Console.WriteLine($"Expected Result: {expectedResult[i]}");
                Console.WriteLine($"Actual Result: {actualResult}");
                Console.WriteLine($"{expectedResult[i] == actualResult}\n\n");
            }

            Console.ReadLine();
        }
    }
}
