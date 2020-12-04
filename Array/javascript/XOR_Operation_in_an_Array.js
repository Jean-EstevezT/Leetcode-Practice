
//Title     : 1486. XOR Operation in an Array
//Category  : Array
//URL       : https://leetcode.com/problems/xor-operation-in-an-array/
//submission: https://leetcode.com/submissions/detail/426955501/


//--------------------------------------------------

/**
 * @param {number} n
 * @param {number} start
 * @return {number}
 */
let xorOperation = function (n, start) {
  let xor_result = start;
  for (let i = 1; i < n; i++) {
    xor_result = xor_result ^ (start + 2 * i);
  }
  return xor_result;
};
