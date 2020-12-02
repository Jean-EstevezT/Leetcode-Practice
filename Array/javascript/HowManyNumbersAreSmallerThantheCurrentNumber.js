
//Title     : 1365. How Many Numbers Are Smaller Than the Current Number
//Category  : Array
//URL       : https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
//submission: https://leetcode.com/submissions/detail/426237874/


//--------------------------------------------------

/* @param {number[]} nums
 * @return {number[]}
 */

// Solution:
let smallerNumbersThanCurrent = function (nums) {
  function order(a, b) {
    return a - b;
  }
  const tp = Array.from(nums).sort(order);
  const result = nums.map(x => tp.indexOf(x));
  return result;
};

