import json

def hasList(Dict):
    values = list(Dict.values())
    for val in values:
        if type(val) == list:
            return True
    return False

class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

    def all_words(self, prefix):
        for letter, child in self.children.items():
            if letter == '/':
                yield prefix, child
            try:
                yield from child.all_words(prefix + letter)
            except:
                pass

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def _insert(self, index, word):
        indeces = '/'
        curr = self.root
        self.size = self.size + 1
        for letter in word:
            node = curr.children.get(letter)
            if not node:
                node = TrieNode()
                curr.children[letter] = node
            curr = node
        if not hasList(curr.children):
            curr.children[indeces] = [index]
            
        else:
            curr.children[indeces].append(index)
        curr.end = True

    def compress(self, string):
        for index, word in enumerate(string.split()):
            self._insert(index, word)

    def _decompress(self):
        prefix = ''
        cur = self.root
        for c in prefix:
            cur = cur.children.get(c)
            if cur is None:
                return
        yield from cur.all_words(prefix)

    def decompress(self):
        result = [None] * self.size #Initialising empty list of the output's size.
        combinations = list(self._decompress())
        for combination in combinations:
            word = combination[0]
            locations = combination[1]
            for location in locations:
                result[location] = word
        return ' '.join(result)
            
if __name__ == "__main__":
    trie = Trie()
    trie.compress('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    res = trie.decompress()
    print(res)
    

