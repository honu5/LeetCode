class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Method to reverse the linked list (you can choose either approach)
    def reverseList(self, head):
        # Iterative approach
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Store the next node
            current.next = prev        # Reverse the link
            prev = current             # Move prev to current
            current = next_node        # Move to the next node
            
        return prev  # New head of the reversed list

    # Uncomment this section for the recursive approach
    # def reverseList(self, head):
    #     if not head or not head.next:
    #         return head
    #
    #     new_head = self.reverseList(head.next)  # Reverse the rest of the list
    #     head.next.next = head  # Make the next node point to the current node
    #     head.next = None       # Set the current node's next to None
    #
    #     return new_head  # Return the new head of the reversed list

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert linked list to a list for easy display
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result