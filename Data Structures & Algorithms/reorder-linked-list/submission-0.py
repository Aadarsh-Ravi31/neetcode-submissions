# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        current = slow.next
        
        slow.next = None
        
        prev = None

        while current:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

       
        list2 = prev
        list1= head

        while list2 :
           next1 = list1.next
           next2 = list2.next

           list1.next = list2
           list2.next = next1

           list1 = next1
           list2 = next2



        


        
        