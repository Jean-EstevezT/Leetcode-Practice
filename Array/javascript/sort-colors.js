//Title     : 75. Sort Colors
//Category  : Array
//URL       : https://leetcode.com/problems/sort-colors
//submission: https://leetcode.com/submissions/detail/454640535/

//--------------------------------------------------

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
let sortColors = function (nums) {
  let len = nums.length;
  for (let i = 1; i < len; i++) {
    for (let j = 0; j < len - i; j++) {
      if (nums[j] > nums[j + 1]) {
        let temp = nums[j]
        nums[j] = nums[j + 1];
        nums[j + 1] = temp;
      }
    }
  }
  return nums;
};


