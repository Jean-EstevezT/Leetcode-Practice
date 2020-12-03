
//Title     : 1313. Decompress Run-Length Encoded List
//Category  : Array
//URL       : https://leetcode.com/problems/decompress-run-length-encoded-list/
//submission: https://leetcode.com/submissions/detail/426592402/


//--------------------------------------------------

/* @param {number[]} nums
 * @return {number[]}
 */

// Solution:
let decompressRLElist = function (nums) {
  let result = [];
  for (let i = 0; i < nums.length; i += 2) {
    for (let n = 0; n < nums[i]; n++) {
      result.push(nums[i + 1]);
    }
  }
  return result;
};

