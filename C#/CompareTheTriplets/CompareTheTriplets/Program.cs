// Problem - Easy
/*
Alice and Bob each create a coding challenge to assess developers' skills.

A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

Alice's rating is the triplet: (a[0], a[1], a[2]).
Bob's rating is the triplet: (b[0], b[1], b[2]).

Each index corresponds to the categories: problem clarity, originality, and difficulty. Retrospectively.


With this information, compare and award points for each category so that:
    If a[i] > b[i], then Alice is awarded 1 point.
    If a[i] < b[i], then Bob is awarded 1 point.
    If a[i] = b[i], then neither person receives a point.

Given Alice and Bob's rating, return the respective amount of points awarded to each.

The return array should be int[2] with Alice's score first and Bob's second. 
 */

// Explaintion
/*
It's important to remove all the extra story around this problem and break it down into a simple problem.
Compare the two arrays and see how many times one is bigger than the other.

We can do that by creating a For Loop. The index (category) we're comparing is the same for both lists so we only need one For Loop.

Next, we compare a[i] and b[i] to see which integer is greater (if any). We can do this with an If Statement.

If it's Alice, the result array should add 1 to Alice's score (index 0).
If it's Bob, the result array should add 1 to Bob's score (index 1).
Else, nothing has to be done.

Once the for loop is finished (which should always be after 3 loops), we return the result array.
 */

// Solution
static List<int> Solution(List<int> a, List<int> b)
{
    List<int> results = new List<int> { 0, 0 };

    for (int i = 0; i < a.Count; i++)
    {
        if (a[i] > b[i])
        {
            results[0]++;
        }
        else if (a[i] < b[i])
        {
            results[1]++;
        }
    }

    return results;
}

// Results
static void TestSolution()
{
    // Setup Test Cases
    var testAliceRatings = new List<List<int>>()
        {
            new List<int>{ 2, 1 , 4},
            new List<int>{ 20, 22, 30 },
            new List<int>{ 12, 22, 19 },
            new List<int>{ 31, 92, 1 },
            new List<int>{ 100, 100, 100 },
            new List<int>{ 3, 98, 50 },
            new List<int>{ 2 , 11, 30 },
        };

    var testBobRatings = new List<List<int>>()
        {
            new List<int>{ 1, 3 , 4},
            new List<int>{ 10, 11, 30 },
            new List<int>{ 11, 21, 18 },
            new List<int>{ 32, 100, 2 },
            new List<int>{ 100, 100, 100 },
            new List<int>{ 3, 99, 50 },
            new List<int>{ 2 , 11, 30 },
        };

    var expectedOutput = new List<List<int>>()
        {
            new List<int>{ 1, 1},
            new List<int>{ 2, 0 },
            new List<int>{ 3, 0 },
            new List<int>{ 0, 3 },
            new List<int>{ 0, 0 },
            new List<int>{ 0, 1 },
            new List<int>{ 0, 0 },
        };

    // Display Results
    for (int i = 0; i < testAliceRatings.Count; i++)
    {
        var solutionOutput = Solution(testAliceRatings[i], testBobRatings[i]);

        Console.WriteLine($"Test Case {i}\n---");

        Console.WriteLine("Expected Result: ");
        expectedOutput[i].ForEach(Console.WriteLine);

        Console.WriteLine("\nSolution's Result: ");
        solutionOutput.ForEach(Console.WriteLine);

        Console.WriteLine($"{(expectedOutput[i].SequenceEqual(solutionOutput) ? "Passed" : "Failed")}\n\n");
    }
}

TestSolution();