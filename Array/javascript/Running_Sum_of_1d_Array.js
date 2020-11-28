// Link: https://leetcode.com/problems/running-sum-of-1d-array/
// #1480

//--------------------------------------------------

/* @param {number[]} nums
 * @return {number[]}
 */

// Solution 1:

let runningSum = function (nums) {
  let result = [];
  let sum = 0;
  for (let i of nums) {
    sum += i;
    result.push(sum)
  }
  return result;
}


// Solution 2:

//let runningSum = function (nums) {
//let result = [];
//for (let i = 1; i <= nums.length; i++) {
//result.push(nums.slice(0, i).reduce((a, b) => a + b))
//} 
//return result;
//}


// Solution 3:

//let runningSum = function (nums) {
//let result = [];
//for (let i = 1; i <= nums.length; i++) {
//let temp = 0;
//for (let el of nums.slice(0, i)) {
//temp += el;
//}
//result.push(temp);
//}
//return result;
//}


