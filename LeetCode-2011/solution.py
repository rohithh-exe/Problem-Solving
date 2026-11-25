class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for operator in operations:
            if operator == "++X" or operator == "X++":
                x = x + 1
            else:
                x = x - 1
        print(x)

Solution.finalValueAfterOperations(1,operations = ["--X", "X++", "X++"])

            