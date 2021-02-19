/*
Title     : 242. Valid Anagram
Category  : String
URL       : https://leetcode.com/problems/valid-anagram/
submission: https://leetcode.com/submissions/detail/457753474/
*/


// --------------------------------------------------
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
let isAnagram = function (s, t) {
  if (s.length !== t.length) {
    return false;
  }
  let ar1 = s.split('').sort();
  let ar2 = t.split('').sort();
  for (let i = 0; i < Math.max(ar1.length, ar2.length); i++) {
    if (ar1[i] !== ar2[i]) {
      return false;
    }
  }
  return true;
};



