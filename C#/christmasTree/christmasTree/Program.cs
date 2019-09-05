/*
 Given an integer ("n") draw a christmas tree with n height, under the following conditions...
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

        // Testing
        static void Main(string[] args)
        {
            // Test Cases
            int[] test_inputs = { 3, 5, 4 };
            string[][] test_outputs =
            {
                new string[] { "  +  ", " +++ ", "+++++", "  +  " },
                new string[] { "    +    ","   +++   ", "  +++++  ", " +++++++ ", "+++++++++", "    +    " },
                new string[] { "   +   ", "  +++  ", " +++++ ", "+++++++", "   +   " }
            };

            // Results
            for( int i = 0; i < test_inputs.Length; i++ )
            {
                string[] solution_output = Solution(test_inputs[i]);
                foreach(string layer in solution_output)
                {
                    Console.WriteLine(layer);
                }
                Console.WriteLine(solution_output.SequenceEqual(test_outputs[i]));
            }
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

    }
}
