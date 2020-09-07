# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Matrix', Difficult='Medium')


# public class Solution {
#     public int maximalSquare(char[][] matrix) {
#         int rows = matrix.length, cols = rows > 0 ? matrix[0].length : 0;
#         int[] dp = new int[cols + 1];
#         int maxsqlen = 0, prev = 0;
#         for (int i = 1; i <= rows; i++) {
#             for (int j = 1; j <= cols; j++) {
#                 int temp = dp[j];
#                 if (matrix[i - 1][j - 1] == '1') {
#                     dp[j] = Math.min(Math.min(dp[j - 1], prev), dp[j]) + 1;
#                     maxsqlen = Math.max(maxsqlen, dp[j]);
#                 } else {
#                     dp[j] = 0;
#                 }
#                 prev = temp;
#             }
#         }
#         return maxsqlen * maxsqlen;
#     }
# }


def maximalSquare(matrix):
    if not matrix:
        return 0

    maxRows = len(matrix)
    maxCols = len(matrix[0])
    maxLength = 0
    dp = [[0 for _ in range(maxCols + 1)] for _ in range(maxRows + 1)]
    for row in range(1, maxRows + 1):
        for col in range(1, maxCols + 1):
            if matrix[row - 1][col - 1] == 1:
                dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1]) + 1
                maxLength = max(maxLength, dp[row][col])
    return maxLength**2


matrix = [[1, 0, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 0, 0, 1, 0]]

print(maximalSquare(matrix))
