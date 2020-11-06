"""
Week 7 guided
"""
"""
*** Demo 1 ***
--------------
Your task is create your own HashTable without using a built-in library.
Your HashTable needs to have the following functions:
- put(key, value) : Inserts a (key, value) pair into the HashTable. If the
value already exists in the HashTable, update the value.
- get(key): Returns the value to which the specified key is mapped, or -1 if
this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key if this map contains the
mapping for the key.
Example:
```plaintext
hash_table = MyHashTable();
hash_table.put("a", 1);
hash_table.put("b", 2);
hash_table.get("a");            // returns 1
hash_table.get("c");            // returns -1 (not found)
hash_table.put("b", 1);         // update the existing value
hash_table.get("b");            // returns 1
hash_table.remove("b");         // remove the mapping for 2
hash_table.get("b");            // returns -1 (not found)
```
"""


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashTable:
    def __init__(self):
        # Your code here
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.item_count = 0

    def djb2(self, key):
        str_key = str(key).encode()
        hash_value = 5381

        for b in str_key:
            hash_value = ((hash_value << 5) + hash_value) + b
            hash_value &= 0xffffffff

        return hash_value

    def hash_function(self, key):
        return self.djb2(key) % self.size

    def put(self, key, value):
        # Your code here
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return

            index = (index + 1) % self.size

        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        # Your code here
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index + 1) % self.size

        return None

    def remove(self, key: int) -> None:
        # Your code here
        index = self.hash_function(key)
        if self.keys[index] is not None:
            self.keys[index] = None
            self.values[index] = None

#
# hash_table = MyHashTable()
# print(hash_table.put("a", 1))
# print(hash_table.put("b", 2))
# print(hash_table.get('b'))
# print(hash_table.get("a"))
# print(hash_table.get("c"))
# print(hash_table.put("b", 1))
# print(hash_table.get("b"))
# print(hash_table.remove("b"))
# print(hash_table.get("b"))

"""
*** Demo 2 *** 
--------------
You've uncovered a secret alien language. To your surprise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).
You need to write a function that, given a sequence of words written in this
secret language, and the order the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.
The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".
Example 1:
```plaintext
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
```
Example 2:
```plaintext
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
```
Example 3:
```plaintext
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
```
Notes:
- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""


def are_words_sorted(words, alpha_order):
    """
    Inputs:
    words: List[str]
    alpha_order: str
    Output:
    bool
    """
    # Your code here
    # map the letters of the string to a dictionary
    hashed_letters = {}
    count = 0
    for letter in alpha_order:
        hashed_letters[letter] = count
        count += 1
    # iterate the array
    for word in range(len(words) - 1):

        # check if the first word is longer than the 2nd word if so return False
        if len(words[word]) > len(words[word + 1]):
            return False
        # iterate the first word
        for letter in range(len(words[word])):
            # create variables for the letters to check
            first_letter = words[word][letter]
            second_letter = words[word + 1][letter]
            print('first', first_letter, 'second', second_letter)
            if hashed_letters[first_letter] < hashed_letters[second_letter]:
                return True
            # if first word1[i] comes after 2nd word2[i] return False
            if hashed_letters[first_letter] > hashed_letters[second_letter]:
                return False

    return True

# print(are_words_sorted(["were","where","yellow"], "habcdefgijklmnopqrstuvwxyz"))


