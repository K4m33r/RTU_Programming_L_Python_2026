
"""
Lab 2.3 – Operator Frequency Counter
------------------------------------
Practice strings and dictionaries by counting characters.

Write a function `count_operators(expression)` that returns a dictionary
with how many times each operator character appears in the expression.

Rules:
- The dictionary ALWAYS has all six keys from OPERATORS, in that order,
  even when a count is 0. Hint: start with {op: 0 for op in OPERATORS}.
- Count character by character: the minus in "-5" counts as "-",
  and "**" counts as two "*".
- Every other character (digits, spaces, letters) is ignored.

In the main block: ask the user for an arithmetic expression, call
count_operators() and print the result.

Example run:
    Enter an arithmetic expression: 3 + 5 * (2 - 1) + 7 / 2
    Operator counts: {'+': 2, '-': 1, '*': 1, '/': 1, '(': 1, ')': 1}

Examples (these are also used to check your work):
>>> count_operators("3 + 5 * (2 - 1) + 7 / 2")
{'+': 2, '-': 1, '*': 1, '/': 1, '(': 1, ')': 1}
>>> count_operators("2 ** 3 - -4")
{'+': 0, '-': 2, '*': 2, '/': 0, '(': 0, ')': 0}
>>> count_operators("")
{'+': 0, '-': 0, '*': 0, '/': 0, '(': 0, ')': 0}
"""

OPERATORS = ['+', '-', '*', '/', '(', ')']


def count_operators(expression: str) -> dict[str, int]:
    """Return a dict with the count of each operator in expression."""
    sayac = {isaret: 0 for isaret in OPERATORS}

    for karakter in expression:
        if karakter in sayac:
            sayac[karakter] += 1

    return sayac


if __name__ == "__main__":
    ifade = input("Enter an arithmetic expression: ")
    sonuc = count_operators(ifade)
    print(f"Operator counts: {sonuc}")

