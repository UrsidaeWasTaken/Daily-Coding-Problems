// Problem
/*
Larry has been given a permutation of a sequence of natural numbers incrementing from 1 as an array. He must
determine whether the array can be sorted using the following operation any number of times:
    Choose any 3 consecutive indices and rotate their elements in such a way that: ABC -> BCA -> CAB -> ABC

For example, if A = {1, 6, 5, 2, 4, 3}

A    rotate  
[1,6,5,2,4,3]  [6,5,2]
[1,5,2,6,4,3]  [5,2,6]
[1,2,6,5,4,3]  [5,4,3]
[1,2,6,3,5,4]  [6,3,5]
[1,2,3,5,6,4]  [5,6,4]
[1,2,3,4,5,6] 
 
Return "YES" if A can be fully sorted. Otherwise, return "NO".
In this case, A can be fully sorted using the rules stated above.

larrysArray has the following parameter(s):
    A: an array of integers
*/

// Solution
function larrysArray(A) {
    let inv = 0
    for (let i=0; i<A.length; i++) {
        for (let j=i+1; j<A.length; j++) {
            if (A[i] > A[j]) {
                inv++;
            }
        }
    }
    if (inv % 2 == 0) {
        return "YES";
    } else {
        return "NO";
    }
}

// Explaination
console.log("An inversion occurs when a value is preceded by a larger number. For this problem, as long as the total number of inversions is even, the array is sortable. This is because you want 0 inversion left by the end (0 is an even number).")

// Custom Tests
const test_inputs = [[3,1,2], [1,3,4,2], [1,2,3,5,4], [1,6,5,2,3,4], [3,1,2,4]]
const test_outputs = ["YES", "YES", "NO", "NO", "YES"]

// Results
for (i in test_inputs) {
    console.log(`\nInput: ${test_inputs[i]}`)
    solution_output = larrysArray(test_inputs[i])
    console.log(`Ouput: ${solution_output}`)
    console.log(solution_output.toString() == test_outputs[i].toString())
}