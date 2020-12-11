
//Title     : 283. Move Zeroes
//Category  : Array
//URL       : https://leetcode.com/problems/move-zeroes/
//submission: https://leetcode.com/submissions/detail/429693300/


//--------------------------------------------------

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
let moveZeroes = function (nums) {
  let len = nums.length;
  let count = 0
  for (let i = 0; i < len; i++) {
    if (nums[i] != 0) {
      nums[count] = nums[i];
      count += 1;
    }
  }
  while (count < len) {
    nums[count] = 0
    count += 1
  }
  return nums;
};


