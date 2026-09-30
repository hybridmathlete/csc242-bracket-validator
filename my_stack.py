"""
Author: AU75ZB
Date: 9/10/2026 (Lab 4); docstrings revised 9/29/2026 for the CSC 242 Group 2 project

Purpose: Implements MyStack, a LIFO (last-in, first-out) stack built by
inheriting from MyLinkedList (Lab 3). The TOP of the stack is mapped to
the FRONT of the linked list, so push, pop, and get_top reuse the O(1)
front operations add_first / delete_at(0) / get_first -- no node or
pointer logic is reimplemented. Also provides is_empty_stack, get_count
(delegating to the inherited count), deep-copy support through the
inherited copy_list, and a __str__ that prints TOP to BOTTOM using only
the stack interface plus a temporary MyStack to restore order.

Group project use: included as part of the shared base classes. The
bracket checker uses MyArrayStack, but MyStack offers the same
interface (push, pop, get_top, is_empty_stack), so either stack could
be used. For the group project, method docstrings were revised to
describe behavior, and a required comment on why deep copy matters was
added.

Input: No console input. The test driver (test_my_stack.py) constructs
MyStack objects and passes integer values to push; the other methods
take no arguments, except copy_list, which takes another MyStack (or
MyLinkedList) instance.

Output: Printed test results comparing expected vs. actual behavior for
every stack operation -- construction, push/get_top, pop (including pop
on an empty stack), deep copy with self-copy safety and object
independence, and __str__ -- verified line-by-line against
Lab_4_expected_output.txt.
"""

from my_linked_list import MyLinkedList


class MyStack(MyLinkedList):
    '''
    MyStack is a LIFO stack built by inheriting from MyLinkedList instead
    of managing its own nodes. Inheriting keeps every node and pointer
    operation in one place: the stack never touches _first, _last, or
    _count directly, so it cannot corrupt the list's invariants, and any
    fix or optimization made to MyLinkedList is picked up automatically.
    Each stack method is a thin rename over an inherited operation --
    push, pop, and get_top all map to the O(1) FRONT of the list
    (add_first / delete_at(0) / get_first).
    '''

    # -----------------------------------------------------------------
    # Required comment -- LIFO (stack) vs. FIFO (queue)
    #
    # A stack is LIFO: the last item pushed is the first one popped.
    # Every operation happens at ONE end, the TOP. This class maps TOP
    # to the FRONT of the inherited linked list, because a linked list
    # adds and removes at the front in O(1) -- so push, pop, and get_top
    # all act on index 0 (add_first / delete_at(0) / get_first).
    #
    # A queue is FIFO: the first item enqueued is the first one
    # dequeued, so a queue works at BOTH ends -- new items join the
    # back, old items leave from the front. If this were MyQueue instead
    # of MyStack, the front/back mapping would change to:
    #     enqueue -> add_last     (join at the BACK)
    #     dequeue -> delete_at(0)  (leave from the FRONT)
    #     peek    -> get_first     (look at the FRONT)
    # A linked list stays O(1) at both ends (delete_at(0) at the front,
    # and add_last is O(1) thanks to the _last pointer), so a linked
    # queue is efficient. An array-backed queue would not be -- removing
    # from the front shifts every element -- which is why MyArrayQueue
    # would need circular indexing.
    # -----------------------------------------------------------------

    # -----------------------------------------------------------------
    # Required comment -- Why deep copy matters (object independence)
    #
    # When a stack is copied, copy_list (inherited from MyLinkedList)
    # creates new nodes for the copy, so the original and the copy each
    # have their own nodes. This keeps the two stacks independent.
    #
    # If the two stacks shared nodes instead, a change to one could
    # quietly affect the other. For example, pushing or popping on one
    # stack might add or remove values the other stack can see, and its
    # count might no longer match the values it actually holds. Methods
    # like get_count, get_top, and __str__ would then return results
    # that don't match what was pushed, and nothing would signal that
    # anything went wrong. Giving each copy its own nodes avoids this.
    # -----------------------------------------------------------------

    def __init__(self):
        '''
        Precondition: none.
        Postcondition: Creates an empty MyStack by reusing MyLinkedList's
        constructor -- no additional state is needed.
        '''
        super().__init__()

    def is_empty_stack(self):
        '''
        Precondition: none.
        Postcondition: Returns True if the stack has no elements, False
        otherwise. Delegates to the inherited is_empty(), so emptiness
        is defined in one place.
        '''
        return self.is_empty()

    def push(self, item):
        '''
        Precondition: item is the value to add.
        Postcondition: item becomes the new TOP of the stack. TOP is the
        FRONT of the linked list, so push uses add_first, which is O(1).
        '''
        self.add_first(item)

    def pop(self):
        '''
        Precondition: none.
        Postcondition: If the stack is not empty, the TOP element is
        removed (does not return a value). If the stack is empty, it is
        left unchanged. TOP = FRONT of the linked list.
        '''
        self.delete_at(0)

    def get_top(self):
        '''
        Precondition: the stack is not empty.
        Postcondition: Returns the TOP element without modifying the
        stack, by reading the FRONT of the list with the inherited
        get_first().
        '''
        return self.get_first()

    def get_count(self):
        '''
        Precondition: none.
        Postcondition: Returns the number of elements currently in the
        stack by delegating to the inherited MyLinkedList count.
        '''
        return super().get_count()

    def __str__(self):
        '''
        Precondition: none.
        Postcondition: Returns "EMPTY STACK" if the stack has no
        elements. Otherwise returns each value from TOP to BOTTOM, one
        value per line. Built using only the stack interface (push, pop,
        get_top, is_empty_stack): values are moved into a temporary
        MyStack while being read, then pushed back, so the stack is left
        exactly as it was.
        '''
        if self.is_empty_stack():
            return "EMPTY STACK"

        temp = MyStack()
        result = ""

        # Drain self into temp, recording each value as it comes off the
        # top. Taking the top first gives TOP-to-BOTTOM order.
        while not self.is_empty_stack():
            value = self.get_top()
            if result == "":
                result = str(value)
            else:
                result = result + "\n" + str(value)
            temp.push(value)
            self.pop()

        # Pour temp back into self so the stack is left exactly as it was.
        while not temp.is_empty_stack():
            self.push(temp.get_top())
            temp.pop()

        return result

    # Creative Final Feature
    def peek_below(self, n):
        '''
        Precondition: n is an integer.
        Postcondition: Returns the value n positions below the TOP of
        the stack without modifying it -- n = 0 returns the TOP itself,
        n = 1 the element just beneath it, and so on. Returns None if n
        is out of range (negative, or n >= get_count()). Because the TOP
        of the stack is the FRONT of the linked list, "n below the top"
        is simply index n, so this reuses the inherited get_at.
        '''
        if n < 0 or n >= self.get_count():
            return None
        return self.get_at(n)
