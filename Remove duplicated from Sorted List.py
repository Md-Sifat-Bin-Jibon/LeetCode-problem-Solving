# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        seen = set()
        current = head
        seen.add(current.val)

        while current.next:
            if current.next.val in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.val)
                current = current.next
        return head