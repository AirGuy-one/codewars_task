class Dictionary:
    def __init__(self, words):
        self.words = words

    def find_most_similar(self, term):
        def edit_distance(word1, word2):
            m, n = len(word1), len(word2)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(m + 1):
                dp[i][0] = i
            for j in range(n + 1):
                dp[0][j] = j
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
            return dp[m][n]

        min_distance = float('inf')
        most_similar_word = None
        for word in self.words:
            distance = edit_distance(term, word)
            if distance < min_distance:
                min_distance = distance
                most_similar_word = word
        return most_similar_word


fruits = Dictionary(['cherry', 'pineapple', 'melon', 'strawberry', 'raspberry'])
print(fruits.find_most_similar('strawbery'))
print(fruits.find_most_similar('berry'))

things = Dictionary(['stars', 'mars', 'wars', 'codec', 'codewars'])
print(things.find_most_similar('coddwars'))

languages = Dictionary(['javascript', 'java', 'ruby', 'php', 'python', 'coffeescript'])
print(languages.find_most_similar('heaven'))
print(languages.find_most_similar('javascript'))
