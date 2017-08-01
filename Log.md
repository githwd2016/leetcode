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

## 566. Reshape the Matrix
#### Time: 2017.7.5
#### Description:
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Note:
1. The height and width of the given matrix is in range [1, 100].
2. The given r and c are all positive.
#### Solution:
1. convert nums to 1-dimension list
2. convert list to r*c matrix

## 575. Distribute Candies
#### Time: 2017.7.13
#### Description:
Given an integer array with even length, where different numbers in this array represent different kinds of candies.
Each number means one candy of the corresponding kind.
You need to distribute these candies equally in number to brother and sister.
Return the maximum number of kinds of candies the sister could gain.

Note:
1. The length of the given array is in range [2, 10,000], and will be even.
2. The number in given array is in range [-100,000, 100,000].
#### Solution:
we only need to find the number of unique candies, and select the samller of it and the
half of the total number.

## 344. Reverse String
#### Time: 2017.8.1
#### Description:
Write a function that takes a string as input and returns the string reversed.
#### Solution:
just use python slice operation.

## 412. Fizz Buzz
#### Time: 2017.8.1
#### Description:
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
#### Solution:
use loop and judgment or list generator.

## 463. Island Perimeter
#### Time: 2017.8.1
#### Description:
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
#### Solution:
Since there are no lakes, every pair of neighbour cells with different values is part of the perimeter (more precisely, the edge between them is). So just count the differing pairs, both horizontally and vertically.