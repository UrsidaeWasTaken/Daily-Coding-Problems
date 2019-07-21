/*
Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x.

Return -1 ([-1, -1]) if the target is not found.
*/

const getIndicesRange = (arr, target) => {
    const range = [arr.indexOf(target), -1]

    for (let i = range[0]; i < arr.length; i++) {
        if (arr[i] === target) {
            range[1] = i
        }
    }

    return range
}

// Custom Tests
const test_inputs = [[[1,3,3,5,7,8,9,9,9,15], 9], [[100,150,150,153], 150], [[1,2,3,4,5,6,10], 9], [[13,12,8,8,2,2,2,2], 13]]
const test_answers= [[6, 8], [1, 2], [-1, -1], [0, 0]]

// Results
for (i in test_inputs) {
    solution_output = getIndicesRange(test_inputs[i][0], test_inputs[i][1])
    console.log('\nOuput: ' + solution_output)
    console.log(solution_output.toString() == test_answers[i].toString())
}