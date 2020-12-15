
//Title     : 1464. Maximum Product of Two Elements in an Array
//Category  : Array
//URL       : https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
//submission: https://leetcode.com/submissions/detail/430728470/


//--------------------------------------------------

/**
 * @param {number[]} nums
 * @return {number}
 */
let maxProduct = function (nums) {
  nums.sort((x, y) => y - x);
  return (nums[0] - 1) * (nums[1] - 1);
};

