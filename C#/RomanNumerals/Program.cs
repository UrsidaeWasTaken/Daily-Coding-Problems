/*
Given a Roman numeral(String) between 1 and 3999, find the corresponding integer value.

For example, given 'IX' the output should be 9.

I     1
IV    4
V     5
IX    9 
X     10
XL    40
L     50
XC    90
C     100
CD    400
D     500
CM    900
M     1000
*/

using System;

namespace RomanNumerals
{
    class Program
    {
        static void Main(string[] args)
        {
            TestSolution();
        }

        // Solution
        static int Solution(string numerals)
        {
            int total = 0;
            numerals = '.' + numerals;

            for(var i = 1; i < numerals.Length; i++)
            {
                switch (numerals[i])
                {
                    case 'M':
                        total += numerals[i-1] == 'C' ? 800 : 1000;
                        break;
                    case 'D':
                        total += numerals[i-1] == 'C' ? 300 : 500;
                        break;
                    case 'C':
                        total += numerals[i-1] == 'X' ? 80 : 100;
                        break;
                    case 'L':
                        total += numerals[i-1] == 'X' ? 30 : 50;
                        break;
                    case 'X':
                        total += numerals[i-1] == 'I' ? 8 : 10;
                        break;
                    case 'V':
                        total += numerals[i-1] == 'I' ? 3 : 5;
                        break;
                    case 'I':
                        total += 1;
                        break;
                }
            }

            return total;
        }

        // Test Solution
        static void TestSolution()
        {
            string[] testInputs = { "MCMIV", "MMMCMXCVIII", "XXVII", "I", "IX", "CMXCIX" };
            int[] testAnswers = { 1904, 3998, 27, 1, 9, 999 };

            for(var i = 0; i < testInputs.Length; i++)
            {
                int SolutionOutput = Solution(testInputs[i]);

                Console.WriteLine($"Output: { SolutionOutput }");
                Console.WriteLine(SolutionOutput == testAnswers[i]);
            }
        }
    }
}
