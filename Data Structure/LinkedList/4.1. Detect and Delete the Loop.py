class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detectAndDeleteLoop(head):
    loopExist = False
    # Edge cases:
    if head is None:
        return
    if head.next is None:
        return

    slow = head
    fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loopExist = True
            break

    # if loop exist-> remove
    if loopExist:
        slow = head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None
    else:
        return loopExist


def takeInput():
    inputList = [int(i) for i in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode
    return head


# __Printing LL function _______________________________________________________________________________________________
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    # print(None)
    return


# Program to detect loop and remove if exist
head = takeInput()
# creating Loop for testing:
head.next.next.next.next.next = head.next.next
ans = detectAndDeleteLoop(head)
if ans == False:
    print('No Loop exist')
else:
    print('LinkedList after removing Loop:')
    printLL(head)
