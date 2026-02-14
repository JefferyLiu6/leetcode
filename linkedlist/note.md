### Merge Two Sorted Lists

**Problem Description:**
You are given the `heads` of two sorted linked lists, `list1` and `list2`. Merge the two lists into a single **sorted** linked list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

**Example:**
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Approach using our `LinkedList` class:**
1.  Create a dummy node (or a sentinel node) to serve as the starting point of our merged list. This simplifies handling the head of the new list.
2.  Initialize a `current_merged` pointer to this dummy node.
3.  Iterate while both `list1` and `list2` have nodes (i.e., their `head` is not `None`):
    a.  Compare the data of the current nodes of `list1` and `list2`.
    b.  Append the node with the smaller data to `current_merged.next`.
    c.  Advance the pointer of the list from which the node was taken.
    d.  Advance `current_merged` to the newly appended node.
4.  After one of the lists is exhausted, append the remaining nodes from the other list to `current_merged.next`.
5.  The head of the merged list will be `dummy_head.next`.
6.  Return a new `LinkedList` object with this head.

**Time Complexity:** O(M + N), where M and N are the lengths of `list1` and `list2`, respectively, because we traverse each list once.
**Space Complexity:** O(1) if we are just re-pointing nodes (which is the standard approach), or O(M + N) if we create new nodes for the merged list (which our `LinkedList.append` would implicitly do if called on individual values, but here we will re-point existing nodes to be more efficient).