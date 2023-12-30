# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode()
        # `node` is assigned the same value as `dummy`
        # This node pointer is used to traverse and build the merged list.
        node = dummy
        
        # iternate as long as both not empty
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            # move the node pointer to the last node in the merged list
            node = node.next

        # if any remaining elements in either list, it links the remaining elments to the merged list
        node.next = list1 or list2

        return dummy.next
