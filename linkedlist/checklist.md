## Basics Skills

1. Reverse 
2. Merge 
3. check cycle (s.next, f.next.next, check if s == f )

**Edge check**  
- If `head == null` OR `head.next == null` OR `head.next.next == null`  
→ return `null`

**Initialize pointers**  
- `s = head.next`  (slow pointer)  
- `f = head.next.next`  (fast pointer)

**Check cycle (Phase 1: find meeting point)**  
- While `s != f`:
  - If `f.next == null` OR `f.next.next == null`  
    → return `null` (no cycle)
  - Move pointers:
    - `s = s.next`
    - `f = f.next.next`

**Reset pointer (Phase 2: find cycle entry)**  
- `f = head`

**Find first loop node**  
- While `s != f`:
  - `s = s.next`
  - `f = f.next`

**Return result**  
- Return `s` (or `f`) → first node of the cycle

4. check if two linked list are the same
5. Check Intersection 

Init: pointer1 = head, pointer2 = head
Them: pointer1 = pointer1.next, pointer2 = pointer2.next until one of them stopped
pointer to short pointer's head, move until the longer pointer end




## Tricks

1. FastSlow pointers
    - find mid pointer
    if odd (only one mid-pointer):   
        init:
        then 
    if even (go to mid-1):

    - go the n-1 pointer   

    - check cycle
2. Hash Table (for enhancements)

