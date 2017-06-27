## Merge Two Binary Trees(617)
#### Time: 2017.6.22
#### Description:
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
#### Solution:
Recursive program
1. if t1 and t2 are all none, return none else return t1 + t2
2. left = t1.left + t2.left
3. right = t1.right + t2.right
4. don't miss the situation that t1 or t2 is none

## Hamming Distance(461)
#### Time: 2017.6.27
#### Description:
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
#### Solution:
1. x xor y
2. count '1'
