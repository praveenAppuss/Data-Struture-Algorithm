class TrieNode:
    """
    Represents a single node in the Trie.
    Each node contains:
    - children: dictionary mapping characters to TrieNode
    - end: boolean flag to indicate end of a word
    """
    def __init__(self):
        self.children = {}   # Stores child nodes (character -> TrieNode)
        self.end = False    # True if this node marks the end of a word


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node does not store any character

    def insert(self, word):
        current = self.root
        for char in word:
            # Create a new node if character not present
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end = True  # Mark the end of the word

    def search(self, word):
        """
        Checks whether a complete word exists in the Trie.
        :param word: string to search
        :return: True if word exists, False otherwise
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.end  # True only if end of word is reached

    def start_with(self, prefix):
        """
        Checks whether any word in the Trie starts with the given prefix.
        :param prefix: prefix string
        :return: True if prefix exists, False otherwise
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def print_all_words(self):
        """
        Prints all words stored in the Trie using DFS traversal.
        """
        def dfs(node, path):
            # If end of a word is reached, print it
            if node.end:
                print("".join(path))
            # Traverse all children
            for char, child in node.children.items():
                dfs(child, path + [char])
        dfs(self.root, [])

    def autocomplete(self, prefix):
        """
        Returns all words in the Trie that start with the given prefix.
        :param prefix: prefix string
        :return: list of matching words
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
        words = []
        def dfs(node, path):
            if node.end:
                words.append("".join(path))
            for char, child in node.children.items():
                dfs(child, path + [char])
        dfs(current, list(prefix))
        return words


# --------- Example Usage ---------
x = Trie()
x.insert("praveen")
x.insert("who is the prime minister")

print(x.search("praveen"))          # True
print(x.start_with("pr"))           # True
x.print_all_words()                 # Prints all stored words
print(x.autocomplete("who"))        # Autocomplete results
