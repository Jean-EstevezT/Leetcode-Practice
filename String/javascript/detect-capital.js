/*
Title     : 520. Detect Capital
Category  : String
URL       : https://leetcode.com/problems/detect-capital/
submission: https://leetcode.com/submissions/detail/468350151/
*/

// --------------------------------------------------
/**
 * @param {string} word
 * @return {boolean}
 */
let detectCapitalUse = function (word) {
	if (word === word.toUpperCase()) {
		return true;
	} else if (word === word.toLowerCase()) {
		return true;
	}
	if (word[0] === word[0].toUpperCase()) {
		for (let i = 1; i < word.length; i++) {
			if (word[i] == word[i].toUpperCase()) {
				return false;
			}
		}
		return true;
	}
	return false;
};
