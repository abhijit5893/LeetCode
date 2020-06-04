# https://leetcode.com/problems/word-ladder/
# BFS - Solution
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        all_combined_dict = collections.defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                all_combined_dict[w[:i] + '_' + w[i + 1:]].append(w)

        queue = collections.deque([(beginWord, 1)])
        visited = set()
        while queue:
            word, steps = queue.popleft()
            if word not in visited:
                visited.add(word)
            if word == endWord:
                return steps
            for i in range(len(word)):
                s = word[:i] + "_" + word[i + 1:]
                neigh_words = all_combined_dict.get(s, [])
                for neigh in neigh_words:
                    if neigh not in visited:
                        queue.append((neigh, steps + 1))

        return 0