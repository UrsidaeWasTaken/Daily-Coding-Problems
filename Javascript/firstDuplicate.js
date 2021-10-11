// Problem
/*
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.
*/

// Solution
function firstDuplicate(a) {
    const unique = new Set();
    
    for (num of a) {
        if (unique.has(num)) {
            return num;
        }
        unique.add(num)
    }
    
    return -1
}

// Explaination
console.log("A set does not allow duplicate values. We can use this to return the first value we come across which is already added to this list in at most O(n)");

// Results
const testInputs = [[2, 1, 3, 5, 3, 2], [2, 2], [3, 3, 3], [1, 1, 2, 2, 1], [10, 6, 8, 4, 9, 1, 7, 2, 5, 3], [2, 4, 3, 5, 1], [2, 3, 3]]
const testOutputs = [3, 2, 3, 1, -1, -1, 3]

for (i in testInputs) {
    console.log(`\nInput: ${testInputs[i]}`)
    solutionOutput = firstDuplicate(testInputs[i])
    console.log(`Ouput: ${solutionOutput}`)
    console.log(solutionOutput == testOutputs[i])
}