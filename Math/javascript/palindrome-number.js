// 9. Palindrome Number
// https://leetcode.com/problems/palindrome-number/

/**
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function(x) {
    let item = String(x);

    for (let i = 0; i < item.length; i++) {
        if (item[i] != item[item.length - i - 1]) {
            return false;
        } 
    }
    return true;
};
