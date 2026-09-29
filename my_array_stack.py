"""
Author: AU75ZB
Date: 9/10/2026

Purpose: Implements MyArrayStack, a LIFO (last-in, first-out) stack
built by inheriting from MyArrayList (Lab 2). The TOP of the stack is
mapped to the END (last valid index) of the backing list, so push, pop,
and get_top reuse the O(1) end operations append / delete_at(count - 1)
/ get(count - 1) -- no indexing or capacity-doubling logic is
reimplemented, and self._array is never touched directly. push goes
through the inherited append(), so MyArrayList's capacity-doubling
still fires correctly when the stack grows past its starting capacity.

Input: No console input. The test driver (test_my_stack.py) constructs
MyArrayStack objects (optionally with a starting capacity) and passes
integer values to push; the other methods take no arguments, except
copy_list, which takes another MyArrayStack (or MyArrayList) instance.

Output: Printed test results comparing expected vs. actual behavior for
every stack operation -- construction, push/get_top, pop (including pop
on an empty stack), deep copy with self-copy safety and object
independence, __str__, and capacity doubling through push -- verified
line-by-line against Lab_4_expected_output.txt.
"""

from my_array_list import MyArrayList


class MyArrayStack(MyArrayList):

    # -----------------------------------------------------------------
    # Required comment -- MyStack (linked) vs. MyArrayStack (array)
    # complexity, and why pop uses the END of the backing list.
    #
    # MyStack maps the TOP to the FRONT of a linked list: push is
    # add_first and pop is delete_at(0). Both are O(1), because a
    # linked list only has to rewire one or two node references at the
    # front -- nothing else moves.
    #
    # MyArrayStack maps the TOP to the END of the backing array: push
    # is append and pop is delete_at(get_count() - 1). Both are O(1)
    # (push is O(1) amortized, since append only occasionally doubles
    # capacity and copies). Removing the LAST element just drops the
    # count -- no element moves.
    #
    # If MyArrayStack used the FRONT instead -- pop as delete_at(0) --
    # every pop would be O(n): delete_at(0) shifts all remaining
    # elements down one slot to close the gap, so a stack of n items
    # costs n-1 shifts per pop. push at the front (insert_at(0)) would
    # be O(n) for the same reason. The END is the cheap end for an
    # array; the FRONT is the cheap end for a linked list -- same ADT,
    # opposite mapping.
    # -----------------------------------------------------------------

    def __init__(self, capacity=4):
        '''
        Precondition: capacity, if given, is a positive integer.
        Postcondition: Creates an empty MyArrayStack with the given
        starting capacity (default 4). Reuse MyArrayList's constructor --
        no additional state is needed.
        '''
        super().__init__(capacity=capacity)

    def is_empty_stack(self):
        '''
        Precondition: none.
        Postcondition: Returns True if the stack has no elements, False
        otherwise. Reuse the correct inherited method -- do not write
        new emptiness logic.
        '''
        return self.is_empty()

    def push(self, item):
        '''
        Precondition: item is the value to add.
        Postcondition: item becomes the new TOP of the stack. TOP =
        END (last valid index) of the backing list. Must go through
        MyArrayList's own append() -- do NOT touch self._array
        directly.
        '''
        self.append(item)

    def pop(self):
        '''
        Precondition: none.
        Postcondition: If the stack is not empty, the TOP element is
        removed (does not return a value). If the stack is empty, it is
        left unchanged. TOP = END of the backing list -- use
        delete_at(get_count() - 1), NOT index 0.
        '''
        self.delete_at(self.get_count() - 1)

    def get_top(self):
        '''
        Precondition: the stack is not empty.
        Postcondition: Returns the TOP element without modifying the
        stack. Reuse the correct inherited accessor at the END of the
        backing list.
        '''
        return self.get(self.get_count() - 1)

    def get_count(self):
        '''
        Precondition: none.
        Postcondition: Returns the number of elements currently in the
        stack. Reuse inherited count logic.
        '''
        return super().get_count()

    def __str__(self):
        '''
        Precondition: none.
        Postcondition: Returns "EMPTY STACK" if the stack has no
        elements. Otherwise returns each value from TOP to BOTTOM, one
        value per line. Do NOT access self._array directly -- build
        this using only get_count() and get() (both inherited public
        methods from MyArrayList).
        '''
        if self.get_count() == 0:
            return "EMPTY STACK"

        result = ""
        for i in range(self.get_count() - 1, -1, -1):
            if result == "":
                result = str(self.get(i))
            else:
                result = result + "\n" + str(self.get(i))
        return result
