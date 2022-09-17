"""https://leetcode.com/problems/median-of-two-sorted-arrays/
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        left, right = 0, len(A) - 1

        while True:
            i = (
                left + right
            ) // 2  # i is the index of the last element in the left partition of A
            j = (
                half - i - 2
            )  # j is the index of the last element in the left partition of B
            
            a_left = A[i] if i >= 0 else float("-inf")
            a_right = A[i + 1] if i + 1 < len(A) else float("inf")
            
            b_left = B[j] if j >= 0 else float("-inf")
            b_right = B[j + 1] if j + 1 < len(B) else float("inf")
            
            # We have partitioned A and B at the correct place
            if a_left <= b_right and b_left <= a_right:
                # odd length
                if total %2:
                    return min(a_right, b_right)
                # even length
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                right = i - 1
            else:
                left = i + 1
                
                
