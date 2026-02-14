class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"

        source_count = Counter(text)
        target_count = Counter(target)
        print(source_count)
        print(target_count)

        return min(source_count[c] // target_count[c] for c in target_count)