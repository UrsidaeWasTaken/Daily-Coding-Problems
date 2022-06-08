// Problem
/*
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.

Return an array of each ratio in decimal form (with 6 places after the decimal), in this order:
    1. Proportion of positive values
    2. Proportion of negative values
    3. Proportion of zeros
    
    
Example:
[1,1,0,-1,-1] -> [0.400000, 0.400000, 0.200000]

2/5 is a positive value, 2/5 is a negative value, 1/5 is a zero value.
 */

TestSolution();

// Solution
static List<string> Solution(int[] arr)
{
    double positiveRatio = 0;
    double negativeRatio = 0;
    double zeroRatio = 0;

    double ratioCount = 1.0 / arr.Length;

    foreach (int number in arr)
    {
        switch (number)
        {
            case > 0:
                positiveRatio += ratioCount;
                break;
            case < 0:
                negativeRatio += ratioCount;
                break;
            default:
                zeroRatio += ratioCount;
                break;
        }
    }

    // Return Output
    return new List<string> {
        $"{positiveRatio.ToString("F6")}",
        $"{negativeRatio.ToString("F6")}" ,
        $"{zeroRatio.ToString("F6")}"
    };
}

// Test Solution
static void TestSolution()
{
    // Test Cases
    var testInputs = new List<int[]>
    {
        new int[] { -4, 3, -9, 0, 4, 1 },
        new int[] { 1, 2, 3, -1, -2, -3, 0, 0 },
        new int[] { 0, 3, 4, 0, -2, -3, 2 },
        new int[] { 0, 0, 0, 0 },
        new int[] { -1 },
        new int[] { 2, 2 },
        new int[] { },
    };

    var expectedOutput = new List<List<string>>
    {
        new List<string> { "0.500000", "0.333333", "0.166667" },
        new List<string> { "0.375000", "0.375000", "0.250000" },
        new List<string> { "0.428571", "0.285714", "0.285714" },
        new List<string> { "0.000000", "0.000000", "1.000000" },
        new List<string> { "0.000000", "1.000000", "0.000000" },
        new List<string> { "1.000000", "0.000000", "0.000000" },
        new List<string> { "0.000000", "0.000000", "0.000000" },
    };

    // Test and Display Results
    for (int i = 0; i < testInputs.Count; i++)
    {
        var actualOutput = Solution(testInputs[i]);

        Console.WriteLine("Expected Result: ");
        expectedOutput[i].ForEach(Console.WriteLine);

        Console.WriteLine("\nSolution's Result: ");
        actualOutput.ForEach(Console.WriteLine);

        Console.WriteLine($"{expectedOutput[i].SequenceEqual(actualOutput)}\n\n");
    }

}
