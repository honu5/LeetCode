# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        values_to_remove = set(nums)
        dummy_node = ListNode(next=head)
        current = dummy_node
        while current.next:
            if current.next.val in values_to_remove:
                current.next = current.next.next
            else:
                current = current.next
      
        return dummy_node.next
        