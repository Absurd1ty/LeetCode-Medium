"""
You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
For example, the word "apple" becomes "applema".
If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
Return the final sentence representing the conversion from sentence to Goat Latin.
"""
class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        words = sentence.split()
        goat_words= []
        for i, word in enumerate(words):
            if word[0].lower() in ['a', 'e', 'i', 'u', 'o']:
                goat_word = word +"ma"
            else:
                goat_word = word[1:] + word[0] + "ma"
            goat_word += "a" * (i+1)
            goat_words.append(goat_word)

        goat_latin_sentence = " ".join(goat_words)
        return goat_latin_sentence


test = Solution()
print(test.toGoatLatin("I speak Goat Latin"))

