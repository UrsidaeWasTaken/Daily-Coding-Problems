/*
Given a string, find the length of the longest substring without repeating characters.

For example, given the string 'Javascript', the program should return 8 ('vascript')
*/

// Solution
const lengthOfLongestSubstring = string => {
    let max_len = 0

    if (string) {
        let visited = []

        for (char of string) {
            if (visited.includes(char)) {
                if (visited.length > max_len) {
                    max_len = visited.length
                }
                visited.push(char)
                visited = visited.splice(visited.indexOf(char)+1)
            } else {
                visited.push(char)
            }
        }

        if (visited.length > max_len) {
            max_len = visited.length
        }
    }

    return max_len
}

// Custom Tests
const test_cases = { 'Javascript':8, 'Eyes':3, 'Honey':5 , 'kmjkoskjlm':6, 'A':1, '':0, 'abcabcbb':3 }

// Results
for (test_case in test_cases) {
    solution_output = lengthOfLongestSubstring(test_case.toLowerCase())
    console.log('\nOuput: ' + solution_output)
    console.log(solution_output === test_cases[test_case])
}
