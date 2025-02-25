class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        words = re.findall(r'\w+',paragraph)  # Extracts words ignoring punctuation
        banned_word = set(banned)
        my_dict = {}
        for word in words:
            if word not in banned_word:
                my_dict[word] = 1+my_dict.get(word,0)
        print(my_dict)
        # Find the word with the maximum count
        return max(my_dict, key=my_dict.get)
