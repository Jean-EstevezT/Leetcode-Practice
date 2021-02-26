/*
Title     : 917. Reverse Only Letters
Category  : String
URL       : https://leetcode.com/problems/reverse-only-letters/
submission: https://leetcode.com/submissions/detail/460744850/
*/


// --------------------------------------------------
/**
 * @param {string} S
 * @return {string}
 */
let reverseOnlyLetters = function (S) {
  let letters = S.match(/[a-z]/ig);
  let res = "";
  for (let i of S) {
    if (i.toLowerCase() != i.toUpperCase()) {
      res += letters.pop();
      continue;
    }
    res += i;
  }
  return res;
};


