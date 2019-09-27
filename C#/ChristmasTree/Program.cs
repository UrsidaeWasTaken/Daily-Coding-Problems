/*
 Given integer ("n") draw a christmas tree with n height, under the following conditions...
 - The tree is centered
 - Increases by 2 ("++") each layer
 - Always has an extra small trunk ("+") at the bottom
 For example:
 n = 3 will output...
   +  
  +++
 +++++
   +
 n = 4 will output...
    +
   +++
  +++++
 +++++++
    +
 */

using System;
using System.Linq;

namespace christmasTree
{
    class Program
    {
        static void Main(string[] args)
        {
            TestSolution();
        }

        // Solution
        static string[] Solution(int n)
        {
            string[] tree = new string[n + 1];
            int size = 1;

            for (int i = 0; i < tree.Length - 1; i++)
            {
                tree[i] = new String('+', size).PadLeft(i + n).PadRight(n * 2 - 1);
                size += 2;
            }

            tree[tree.Length - 1] = tree[0];

            return tree;
        }

        // Test Solution
        static void TestSolution()
        {
            // Setup Test Cases
            int[] testInputs = { 3, 5, 4 };
            string[][] testOutputs = 
            {
                new string[] { "  +  ", " +++ ", "+++++", "  +  " },
                new string[] { "    +    ","   +++   ", "  +++++  ", " +++++++ ", "+++++++++", "    +    " },
                new string[] { "   +   ", "  +++  ", " +++++ ", "+++++++", "   +   " }
            };

            // Test and Display Results
            for (int i = 0; i < testInputs.Length; i++)
            {
                string[] solutionOutput = Solution(testInputs[i]);
                foreach (string layer in solutionOutput)
                {
                    Console.WriteLine(layer);
                }
                Console.WriteLine(solutionOutput.SequenceEqual(testOutputs[i]));
            }
        }

    }
}