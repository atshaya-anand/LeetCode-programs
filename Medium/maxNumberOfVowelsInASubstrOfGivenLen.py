# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = { 'a', 'e', 'i', 'o', 'u' }
        
        substring = s[:k]
        
        vowel_count = sum( 1 for char in substring if char in vowels )
        
        # record for max vowel count in substring
        max_vowel_count = vowel_count
        
        
        # sliding window of size k
        for tail_index in range(k, len(s)):
            
            head_index = tail_index - k
            head_char, tail_char = s[head_index], s[tail_index]
            
            if head_char in vowels:
                vowel_count -= 1
                
            if tail_char in vowels:
                vowel_count += 1
                
            max_vowel_count = max( max_vowel_count, vowel_count)
            
        
        return max_vowel_count