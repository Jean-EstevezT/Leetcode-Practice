//Title     : 287. Find the Duplicate Number
//Category  : Array
//URL       : https://leetcode.com/problems/find-the-duplicate-number/
//submission: https://leetcode.com/submissions/detail/452562834/


//--------------------------------------------------

/**
 * @param {number[]} nums
 * @return {number}
 */
let findDuplicate = function (nums) {
  let temp = new Set();
  for (let num of nums) {
    if (temp.has(num)) {
      return num;
    }
    temp.add(num);
  }
};


