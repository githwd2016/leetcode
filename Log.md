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

## Array Partition I(561)
#### Time: 2017.6.29
#### Description:
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
#### Solution:
先排序，将相邻两个数分为一组，每组较小数都在左边，求和即可

假设对于每一对i，bi >= ai。 定义Sm = min（a1，b1）+ min（a2，b2）+ … + min（an，bn）。最大的Sm是这个问题的答案。由于bi >= ai，Sm = a1 + a2 + … + an。 定义Sa = a1 + b1 + a2 + b2 + … + an + bn。对于给定的输入，Sa是常数。 定义di = | ai - bi |。由于bi >= ai，di = bi-ai, bi = ai+di。 定义Sd = d1 + d2 + … + dn。 所以Sa = a1 + (a1 + d1) + a2 + (a2 + d2) + … + an + (an + di) = 2Sm + Sd , 所以Sm =（Sa-Sd）/ 2。为得到最大Sm，给定Sa为常数，需要使Sd尽可能小。 所以这个问题就是在数组中找到使di（ai和bi之间的距离）的和尽可能小的对。显然，相邻元素的这些距离之和是最小的。

