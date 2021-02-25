/*
Title     : 917. Reverse Only Letters
Category  : String
URL       : https://leetcode.com/problems/reverse-only-letters/
submission: https://leetcode.com/submissions/detail/452190168/
*/


// --------------------------------------------------
/**
 * @param {string} S
 * @return {string}
 */
let reverseOnlyLetters = function (S) {
  let ar = S.split('')
  let re = /[a-z]/i;

  for (let i = S.length - 1, j = 0; i > 0; i--, j++) {
    if (S[i].match(re)) {
      if (ar[j].match(re)) {
        ar[j] = S[i]
      }
    }
  }

  return ar.join('')
};

console.log(reverseOnlyLetters("ab-cd"))
console.log(reverseOnlyLetters("a-bC-dEf-ghIj"))
console.log(reverseOnlyLetters("Test1ng-Leet=code-Q!"))

