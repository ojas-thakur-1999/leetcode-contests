class Solution:
    def similarPairs(self, words):
        words_i_strings = []
        for i in range(len(words)):
            found_dict = {}
            for char in words[i]:
                found_dict[char] = True
            
            found_chars = found_dict.keys()
            found_chars = sorted(found_chars)
            found_string = ""
            for char in found_chars:
                found_string += char
            
            words_i_strings.append(found_string)
        
        found_pairs = []
        for i in range(len(words_i_strings)):
            for j in range(i+1, len(words_i_strings)):
                if words_i_strings[i] == words_i_strings[j]:
                    found_pairs.append([i,j])
        
        return len(found_pairs)

ans = Solution().similarPairs(["aabb","ab","ba"])
ans = Solution().similarPairs(["aba","aabb","abcd","bac","aabc"])
ans = Solution().similarPairs(["nba","cba","dba"])
print(ans)