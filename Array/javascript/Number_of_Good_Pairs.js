
//Title     : 1512. Number of Good Pairs
//Category  : Array
//URL       : https://leetcode.com/problems/number-of-good-pairs/
//submission: https://leetcode.com/submissions/detail/425882021/


//--------------------------------------------------

/* @param {number[]} nums
 * @return {number[]}
 */

// Solution 1:
//let numIdenticalPairs = function (nums) {
//let result = 0;
//for (let i = 0; i < nums.length - 1; i++) {
//nums.slice(i + 1, nums.length).forEach((x) => nums[i] == x ? result += 1 : false);
//}
//return result;
//};

// Solution 2:
let numIdenticalPairs = function (nums) {
  let result = 0;
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] == nums[j]) {
        result += 1;
      }
    }
  }
  return result;
};

// Solution 3:
//let numIdenticalPairs = function (nums) {
  //let result = 0;
  //for (let i = 0; i < nums.length - 1; i++) {
    //result += nums.slice(i + 1, nums.length).filter(x => nums[i] === x).length;
  //}
  //return result;
//};





