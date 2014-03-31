# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        tmp = dummy
        k = len(lists)
        qu = []
        i = 0
        while i < k:
            if lists[i] is not None:
                qu.append([lists[i].val,i])
            i += 1
        qu.sort(key=lambda x:x[0])
        while len(qu) > 0:
            cur = qu.pop(0)
            list_index = cur[1]
            tmp.next = lists[list_index]
            tmp = lists[list_index]
            lists[list_index] = lists[list_index].next
            if lists[list_index] is not None:
                qu.append([lists[list_index].val, list_index])
                qu.sort(key=lambda x:x[0])
        return dummy.next
