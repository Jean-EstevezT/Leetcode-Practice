/*
Title     : 557. Reverse Words in a String III
Category  : String
URL       : https://leetcode.com/problems/reverse-words-in-a-string-iii/
submission: https://leetcode.com/submissions/detail/452190168/
*/


// --------------------------------------------------
/**
 * @param {string} s
 * @return {string}
 */
let reverseWords = function (s) {
  return s.split(' ').map(x => x.split('').reverse().join('')).join(' ');
};



