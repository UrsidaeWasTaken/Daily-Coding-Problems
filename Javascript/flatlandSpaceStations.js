/*
Flatland is a country with a number of cities, some of which have space stations. Cities are numbered consecutively and each has a road of 1km length connecting it to the next city. It is not a circular route, so the first city doesn't connect with the last city.

Determine the maximum distance from any city to its nearest space station.

For example, given n = 3 cities where c = [1] are space stations, only City 1 has a space station. They occur consecutively along a route. City 0 is 1-0=1 unit away and city 2 is 2-1=1 unit away. City 1 is 1-1=0 units from its nearest space station as one is located there. The maximum distance is 1.

flatlandSpaceStations has the following parameter(s):

    int n: the number of cities
    int c[m]: the indices of cities with a space station

*/

function flatlandSpaceStations(n, c) {
    let sortedArr = new Int32Array(c).sort();
    
    // Distance between the last space station and the last city
    const distanceFromLastStation = Math.abs(sortedArr[sortedArr.length - 1] - n) - 1;
    // Distance between the first space station and the first city
    const distanceFromFirstStation = sortedArr[0]
    // Compare distanceFromLastStation to distanceFromFirstStation. Which is the furthest is our starting point.
    let maxDistance = Math.max(distanceFromFirstStation, distanceFromLastStation)
    
    // Compare the distances within the c list to see if any are bigger than our starting Max Distance
    for (let i = 0; i < sortedArr.length; i++) {
        let currDistance = Math.round((Math.abs(sortedArr[i+1] - sortedArr[i]) - 1) / 2);
        
        if (currDistance > maxDistance) {
            maxDistance = currDistance;
        }
    }
    
    return maxDistance;
}

// Custom Tests
const test_inputs = [[95, [68,81,46,54,30,11,19,23,22,12,38,91,48,75,26,86,29,83,62]],
                    [5, [0,4]],
                    [6, [0,1,2,4,3,5]]]
const test_answers= [11, 2, 0]

// Results
for (i in test_inputs) {
    solution_output = flatlandSpaceStations(test_inputs[i][0], test_inputs[i][1])
    console.log('\nOuput: ' + solution_output)
    console.log(solution_output== test_answers[i])
}