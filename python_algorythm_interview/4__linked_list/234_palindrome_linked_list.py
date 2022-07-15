# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        value_list=[]
        while(not head==None):
            value_list.append(head.val)
            head=head.next
        return value_list==value_list[::-1]