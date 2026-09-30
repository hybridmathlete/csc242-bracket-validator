"""
Author: AU75ZB
Date: 9/1/2026 (Lab 3); updated 9/21/2026 for Lab 6; reused 9/29/2026 for the CSC 242 Group 2 project

Purpose: Implements MyLinkedList, a singly linked list built from
individually linked node objects (_Node). Supports insertion and
deletion at arbitrary indices via reference rewiring rather than array
shifting, deep copying (including a safe self-copy case), sequential
search, and operator overloading for __eq__/__ne__/__str__.
Lab 6 addition: get_at(index), which traverses to the given index and
returns the stored object itself (not a copy), so the caller can read
it or change it in place. MyHashTable uses this to walk each bucket
chain and increment a FreqPair's count directly.

Group project use: SessionHistory (session_history.py) logs every
check as an entry in a MyLinkedList, adding each one with add_last and
reading them back in order with get_count() and get_at(). MyStack also
inherits from this class. No changes to this class were needed.

Input: An optional Python list (or other iterable) of items passed to
from_array; items, indices, and values passed to the various methods
(add_first, add_last, insert_at, get_at, delete_item, delete_at,
search, index_of, etc.); and, for copy_list/__eq__/__ne__, another
MyLinkedList instance.

Output: Printed test results comparing expected vs. actual behavior
for every method -- constructors, add/insert, delete, search, deep
copy, and the operator overloads -- verified line-by-line against
Lab_3_expected_output.txt. In Lab 6, used as the bucket chain for
MyHashTable and as the result list returned by find_top_k.
"""


class _Node:
    '''
    Precondition: data is the value to store; next is either None or
    another _Node.
    Postcondition: Creates a single linked-list node holding data and a
    reference to the next node (or None if this is the last node).
    '''
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class MyLinkedList:

    def __init__(self):
        '''
        Precondition: none.
        Postcondition: Creates an empty MyLinkedList with no nodes, a
        count of 0, and first/last references set to None.
        '''
        self._first = None
        self._last = None
        self._count = 0

    @classmethod
    def from_array(cls, items):
        '''
        Precondition: items is a Python list (or other iterable) of
        values, in the order they should appear in the list.
        Postcondition: Returns a new MyLinkedList containing a node for
        each value in items, in the same order, built by repeated calls
        to add_last.
        '''
        newList = cls()
        for item in items:
            newList.add_last(item)
        return newList

    def copy_list(self, other):
        '''
        Precondition: other is a MyLinkedList (may be the same object as
        self).
        Postcondition: self becomes a deep copy of other's contents --
        every node in self is newly allocated, not shared with other.
        Correctly handles the self-copy case (copy_list(self)) without
        corrupting or losing data.
        '''
        if self is other:
            return

        newFirst = None
        newLast = None
        newCount = 0
        current = other._first
        while current is not None:
            newNode = _Node(current.data)
            if newFirst is None:
                newFirst = newNode
                newLast = newNode
            else:
                newLast.next = newNode
                newLast = newNode
            newCount += 1
            current = current.next

        self._first = newFirst
        self._last = newLast
        self._count = newCount

    def get_count(self):
        '''
        Precondition: none.
        Postcondition: Returns the number of nodes currently in the
        list.
        '''
        return self._count

    def is_empty(self):
        '''
        Precondition: none.
        Postcondition: Returns True if the list has no nodes, False
        otherwise.
        '''
        return self._count == 0

    def __str__(self):
        '''
        Precondition: none.
        Postcondition: Returns "EMPTY LIST" if the list has no nodes.
        Otherwise returns each node's value separated by " -> ", with no
        trailing arrow after the last element.
        '''
        if self._first is None:
            return "EMPTY LIST"

        result = str(self._first.data)
        current = self._first.next
        while current is not None:
            result = result + " -> " + str(current.data)
            current = current.next
        return result

    def get_first(self):
        '''
        Precondition: the list is not empty.
        Postcondition: Returns the value stored in the first node.
        '''
        return self._first.data

    def get_last(self):
        '''
        Precondition: the list is not empty.
        Postcondition: Returns the value stored in the last node.
        '''
        return self._last.data

    def get_at(self, index):
        '''
        Precondition: 0 <= index < self.get_count().
        Postcondition: Returns the object stored at that index (not a
        copy), found by traversing from the first node one node at a
        time until index is reached. Since Python objects are passed by
        reference, the caller can read the object or mutate its
        attributes in place (e.g. pair.count += 1), exactly like
        returning a reference in C++. Added in Lab 6.
        '''
        current = self._first
        for i in range(index):
            current = current.next
        return current.data

    def search(self, item):
        '''
        Precondition: item is the value to search for.
        Postcondition: Returns True if item is found in the list, False
        otherwise. Reuses index_of so the search logic stays in one
        place.
        '''
        return self.index_of(item) != -1

    def add_first(self, item):
        '''
        Precondition: item is the value to add.
        Postcondition: item is inserted as the new first node. If the
        list was empty, last is also updated to the new node. count
        increases by 1.
        '''
        newNode = _Node(item, self._first)
        #created Node above. newNode = _Node(item) is the data box and newNode.next is the pointer box. 
        self._first = newNode
        if self._last is None:
            self._last = newNode
        self._count += 1

    def add_last(self, item):
        '''
        Precondition: item is the value to add.
        Postcondition: item is inserted as the new last node. If the
        list was empty, first is also updated to the new node. count
        increases by 1.
        '''
        newNode = _Node(item)
        if self._last is None:
            self._first = newNode
            self._last = newNode
        else:
            self._last.next = newNode
            self._last = newNode
        self._count += 1

    def insert_at(self, index, item):
        '''
        Precondition: index is an integer; item is the value to insert.
        Postcondition: If 0 <= index <= count, item is inserted at
        index (rewiring the previous node's reference), and returns
        True. Otherwise, the list is left unchanged and returns False.
        '''
        if index < 0 or index > self._count:
            return False

        if index == 0:
            self.add_first(item)
            return True

        if index == self._count:
            self.add_last(item)
            return True

        previous = self._first
        for i in range(index - 1):
            previous = previous.next

        newNode = _Node(item, previous.next)
        previous.next = newNode
        self._count += 1
        return True

    def delete_item(self, item):
        '''
        Precondition: item is the value to remove.
        Postcondition: Removes only the FIRST occurrence of item. If
        item is not found, the list is left unchanged. first, last, and
        count are updated correctly. Reuses delete_at so the rewiring
        logic stays in one place.
        '''
        index = self.index_of(item)
        if index != -1:
            self.delete_at(index)

    def delete_at(self, index):
        '''
        Precondition: index is an integer.
        Postcondition: If 0 <= index < count, removes the node at index
        (rewiring the previous node's reference) and returns True.
        Otherwise, the list is left unchanged and returns False.
        '''
        if index < 0 or index >= self._count:
            return False

        if index == 0:
            self._first = self._first.next
            if self._first is None:
                self._last = None
            self._count -= 1
            return True

        previous = self._first
        for i in range(index - 1):
            previous = previous.next

        target = previous.next
        previous.next = target.next
        if target is self._last:
            self._last = previous
        self._count -= 1
        return True

    def index_of(self, item):
        '''
        Precondition: item is the value to search for.
        Postcondition: Returns the index of the first occurrence of
        item, using sequential traversal. Returns -1 if not found.
        '''
        current = self._first
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        return -1

    def __eq__(self, other):
        '''
        Precondition: other is any object.
        Postcondition: Returns True only if other is a MyLinkedList with
        the same length and the same values in the same order. Returns
        NotImplemented if other is not a MyLinkedList.
        '''
        if not isinstance(other, MyLinkedList):
            return NotImplemented

        if self._count != other._count:
            return False

        currentSelf = self._first
        currentOther = other._first
        while currentSelf is not None:
            if currentSelf.data != currentOther.data:
                return False
            currentSelf = currentSelf.next
            currentOther = currentOther.next
        return True

    def __ne__(self, other):
        '''
        Precondition: other is any object.
        Postcondition: Returns the logical opposite of __eq__.
        '''
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def clear(self):
        '''
        Precondition: none.
        Postcondition: Removes all nodes, resetting the list to an
        empty state (first and last become None, count becomes 0).
        '''
        self._first = None
        self._last = None
        self._count = 0
       