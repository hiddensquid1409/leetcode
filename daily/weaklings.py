"""https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
1996. The Number of Weak Characters in the Game

You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters."""

from typing import List


## Solution 1 - Brute Force
## Time Complexity: O(n^2)
## Space Complexity: O(1)
# ! This solution is too slow for the test cases and probably would not work because it can count the same character more than once


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        if not properties:
            return 0
        weak_chars = 0
        for i in range(len(properties)):
            attack_i, defense_i = properties[i]
            for j in range(1, len(properties)):
                attack_j, defense_j = properties[j]
                if attack_j > attack_i and defense_j > defense_i:
                    weak_chars += 1
        return weak_chars


## Solution 2 - Sort by Attack and Defense
## Time Complexity: O(nlogn)
## Space Complexity: O(1)


class Solution2:
    def numberofWeakCharacter(self, properties: List[List[int]]) -> int:
        if not properties:
            return 0
        properties.sort(key=lambda x: (-x[0], x[1]))
        max_defense = 0
        weak_chars = 0
        for attack, defense in properties:
            if defense < max_defense:
                weak_chars += 1
            max_defense = max(max_defense, defense)
        return weak_chars


if __name__ == "__main__":
    test1 = [[5, 5], [6, 3], [3, 6]]
    test2 = [[2, 2], [3, 3]]
    test3 = [[1, 5], [10, 4], [4, 3]]
