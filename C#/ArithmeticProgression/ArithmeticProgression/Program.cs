/*
Given the first two integers of an arithmetic progression sequence, find its nth element.

For example, given the sequence [3, 2] and n = 4, the output should be 0.
 */

using System;
using System.Collections.Generic;

namespace ArithmeticProgression
{
    class Program
    {
        static void Main(string[] args)
        {
            TestSolution();
        }

        // Solution
        static int Solution(List<int> sequence, int n) => sequence[1] + (n - 2) * (sequence[1] - sequence[0]);

        // Test Solution
        static void TestSolution()
        {
            // Setup Test Cases
            List<List<int>> testInputSequences = new List<List<int>>()
            {
                new List<int>{ 3, 2 },
                new List<int>{ 2, 2 },
                new List<int>{ 12, -2 },
                new List<int>{ 3100, 9214 },
                new List<int>{ -34, -21 },
                new List<int>{ 0, 0 },
                new List<int>{ -2 , -2 },
            };

            List<int> testInputNth = new List<int>() { 4, 0, 10, 7, 1, 0, 2 };

            List<int> testOutput = new List<int>() { 0, 2, -114, 39784, -34, 0, -2 };

            // Test and Display Results
            for (int i = 0; i < testInputSequences.Count; i++)
            {
                int solutionOutput = Solution(testInputSequences[i], testInputNth[i]);

                Console.WriteLine($"Output: { solutionOutput }");
                Console.WriteLine(solutionOutput == testOutput[i]);
            }
        }
    }
}
