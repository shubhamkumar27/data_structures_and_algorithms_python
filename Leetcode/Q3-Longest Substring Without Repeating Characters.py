'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        maxm = 0
        l=0
        hashtable = [0]*256
        for i in range(len(s)):
            has = ord(s[i])
            if hashtable[has] != 1:
                l+=1
                hashtable[has] = 1
            else:
                l=0
                hashtable[has] = 0
            if l>maxm:
                maxm=l
        return maxm