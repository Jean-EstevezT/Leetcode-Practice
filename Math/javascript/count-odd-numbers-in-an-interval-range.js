//Title     : 1523. Count Odd Numbers in an Interval Range
//Category  : Math
//URL       : https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
//submission: https://leetcode.com/submissions/detail/449522277/


//--------------------------------------------------
//Solution:
/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
let countOdds = function (low, high) {
  let res = ~~((high - low) / 2);
  if (low % 2 != 0 || high % 2 != 0) {
    res += 1;
  }
  return res;
};
