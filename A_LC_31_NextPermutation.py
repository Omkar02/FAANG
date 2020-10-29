# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def nextPermutation(nums):
    i = len(nums) - 2
    while i > 0 and nums[i + 1] <= nums[i]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while j > 0 and nums[j] <= nums[i]:
            j -= 1
        swap(nums, i, j)

    reverse(nums, i + 1)


def swap(a, s, o):
    a[s], a[o] = a[o], a[s]


def reverse(nums, start):
    i = start
    j = len(nums) - 1
    while i < j:
        swap(nums, i, j)
        i += 1
        j -= 1


nums = [1, 2, 3]

nextPermutation(nums)
print(nums)


# public class Solution {
#     public void nextPermutation(int[] nums) {
#         int i = nums.length - 2;
#         while (i >= 0 && nums[i + 1] <= nums[i]) {
#             i--;
#         }
#         if (i >= 0) {
#             int j = nums.length - 1;
#             while (j >= 0 && nums[j] <= nums[i]) {
#                 j--;
#             }
#             swap(nums, i, j);
#         }
#         reverse(nums, i + 1);
#     }

#     private void reverse(int[] nums, int start) {
#         int i = start, j = nums.length - 1;
#         while (i < j) {
#             swap(nums, i, j);
#             i++;
#             j--;
#         }
#     }

#     private void swap(int[] nums, int i, int j) {
#         int temp = nums[i];
#         nums[i] = nums[j];
#         nums[j] = temp;
#     }
# }
