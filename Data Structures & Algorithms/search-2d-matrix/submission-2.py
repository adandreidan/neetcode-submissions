class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while (l <= r):
            mid = (l + r) // 2
            if (matrix[mid][0] == target):
                return True
            elif (matrix[mid][0] > target):
                r = mid - 1
            elif (matrix[mid][-1] < target):
                l = mid + 1
            else:
                break
        if not (l <= r):
            return False
        row = mid

        left = 0

        right = len(matrix[row]) - 1

        while (left <= right):

            middle = (left + right) // 2

            if (matrix[row][middle] == target):

                return True

            elif (matrix[row][middle] < target):

                left = middle + 1

            else:

                right = middle - 1

        return False