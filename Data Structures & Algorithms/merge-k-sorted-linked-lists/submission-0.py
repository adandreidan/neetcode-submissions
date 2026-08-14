# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merg = []
            for i in range (0, len(lists), 2):
                l1 = lists[i]
                if (i + 1) < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None
                merg.append(self.merger(l1, l2))
            lists = merg
        return lists[0]

    def merger(self, l1, l2):
        dummy = ListNode(0, None)
        temp = dummy
        while (l1 and l2):
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return dummy.next
                

