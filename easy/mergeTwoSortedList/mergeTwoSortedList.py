class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = [1, 2, 4]
list2 = [1, 3, 4]

newList = ListNode()
tail = newList

while list1 and list2:
    if list1 <= list2:
        tail.next = list1
        tail = tail.next
        list1 = list1.next
    else:
        tail.next = list2
        tail = tail.next
        list2 = list2.next

if list1:
    tail.next = list1
else:
    tail.next = list2
