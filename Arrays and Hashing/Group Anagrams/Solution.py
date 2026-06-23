def groupAnagrams(self, strs):
        grouped = {}
        for i in strs:
            sorted_word = ''.join(sorted(i))
            if sorted_word in grouped:
                grouped[sorted_word].append(i)
            else:
                grouped[sorted_word] = [i]
        return list(grouped.values())