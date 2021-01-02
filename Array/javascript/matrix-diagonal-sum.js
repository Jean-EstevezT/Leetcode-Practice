//Title     : 1572. Matrix Diagonal Sum
//Category  : Array
//URL       : https://leetcode.com/problems/matrix-diagonal-sum/
//submission: https://leetcode.com/submissions/detail/437720515/
//

//--------------------------------------------------

/**
 * @param {number[][]} mat
 * @return {number}
 */
let diagonalSum = function (mat) {
  let diagonal = 0;
  for (let i = 0, j = mat.length - 1; i < mat.length; i++, j--) {
    diagonal += i != j ? mat[i][i] + mat[i][j] : mat[i][j]
  }
  return diagonal;
};


