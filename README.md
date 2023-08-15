# LeetCode #86: Partition List (Daily Challenge 08/15/2023)
This repository contains a Python 3 solution to the LeetCode daily challenge #86 for 08/15/2023. https://leetcode.com/problems/partition-list/

This solution beats 95.58% of users in runtime (36 ms) and 16.48% of users in memory usage (16.48 MB).

## Running
The Python solution can be run with
```
python3 partition_list.py
```

There are no arguments; the test cases are hard-coded into the Python file. Example output:

```
Testing Report
------------------------------------------------------------
partition(head, 3): [1 -> 2 -> 2 -> 4 -> 3 -> 5 -> None]
          Expected: [1 -> 2 -> 2 -> 4 -> 3 -> 5 -> None]
Test case 1 passed!

partition(head, 2): [1 -> 2 -> None]
          Expected: [1 -> 2 -> None]
Test case 2 passed!

partition(head, 0): [None]
          Expected: [None]
Test case 3 passed!

partition(head, 0): [1 -> None]
          Expected: [1 -> None]
Test case 4 passed!

partition(head, 2): [1 -> None]
          Expected: [1 -> None]
Test case 5 passed!

Test cases passed: 100.0%
------------------------------------------------------------
```