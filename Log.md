## 617. Merge Two Binary Trees
#### Time: 2017.6.22
#### Description:
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Note: The merging process must start from the root nodes of both trees.
#### Solution:
Recursive program
1. if t1 and t2 are all none, return none else return t1 + t2
2. left = t1.left + t2.left
3. right = t1.right + t2.right
4. don't miss the situation that t1 or t2 is none

## 461. Hamming Distance
#### Time: 2017.6.27
#### Description:
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
#### Solution:
1. x xor y
2. count '1'

## 561. Array Partition I
#### Time: 2017.6.29
#### Description:
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Note:
1. n is a positive integer, which is in the range of [1, 10000].
2. All the integers in the array will be in the range of [-10000, 10000].
#### Solution:
先排序，将相邻两个数分为一组，每组较小数都在左边，求和即可

假设对于每一对i，bi >= ai。 定义Sm = min（a1，b1）+ min（a2，b2）+ … + min（an，bn）。最大的Sm是这个问题的答案。由于bi >= ai，Sm = a1 + a2 + … + an。 定义Sa = a1 + b1 + a2 + b2 + … + an + bn。对于给定的输入，Sa是常数。 定义di = | ai - bi |。由于bi >= ai，di = bi-ai, bi = ai+di。 定义Sd = d1 + d2 + … + dn。 所以Sa = a1 + (a1 + d1) + a2 + (a2 + d2) + … + an + (an + di) = 2Sm + Sd , 所以Sm =（Sa-Sd）/ 2。为得到最大Sm，给定Sa为常数，需要使Sd尽可能小。 所以这个问题就是在数组中找到使di（ai和bi之间的距离）的和尽可能小的对。显然，相邻元素的这些距离之和是最小的。

## 476. Number Complement
#### Time: 2017.6.30
#### Description:
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
1. The given integer is guaranteed to fit within the range of a 32-bit signed integer.
2. You could assume no leading zero bit in the integer’s binary representation.
#### Solution:
1. find the minimum h that 2^h > num
2. return 2^h - 1 - num

## 500. Keyboard Row
#### Time: 2017.7.3
#### Description:
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Note:
1. You may use one character in the keyboard more than once.
2. You may assume the input string will only contain letters of alphabet.
#### Solution:
python re module or set operate

## 557. Reverse Words in a String III
#### Time: 2017.7.4
#### Description:
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Note:In the string, each word is separated by single space and there will not be any extra space in the string.
#### Solution:
use list generator or double reverse.

