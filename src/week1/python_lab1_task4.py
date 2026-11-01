
"""
Task 4 – Text-based Arithmetic Analyzer
---------------------------------------
Create a text-based analyzer made of small helper functions.

Rules used by all functions:
- Words are pieces of text separated by whitespace (use .split()).
- A NUMBER is a word that is a whole integer, optionally with a leading
  minus sign, e.g. "7", "42", "-3".
  Punctuation at the end of a word is ignored, so "5," "10." "8!" count
  as 5, 10 and 8. Use word.rstrip(".,!?;:") to remove it.
  Decimals ("3.5") and mixed words ("abc123") are NOT numbers.
- You do not need the `re` module; .split(), .rstrip() and .isdigit()
  are enough.

Helper functions:
- count_characters(text) -> int    : characters that are not whitespace
- count_words(text)      -> int    : number of words
- extract_numbers(text)  -> list   : list of ints, in the order they appear
- analyze_text(text)     -> dict   : combines the helpers (see below)

analyze_text() returns a dict with exactly these keys:
    "characters" : int
    "words"      : int
    "numbers"    : list
    "sum"        : int
    "average"    : float

In the main block: read a line of text, call analyze_text(), and print a
summary. Round the average to 2 decimals when printing.

Example run:
    Enter text: I have 3 apples and 5 pears
    Characters (no spaces): 21
    Words: 7
    Numbers: [3, 5]
    Sum: 8
    Average: 4.00

Examples (these are also used to check your work):
>>> count_characters("a b  c")
3
>>> count_words("I have 3 apples and 5 pears")
7
>>> extract_numbers("Scores: 10, -4 and 7! but not 3.5 or abc123")
[10, -4, 7]
>>> result = analyze_text("I have 3 apples and 5 pears")
>>> result["characters"], result["words"], result["numbers"]
(21, 7, [3, 5])
>>> result["sum"], result["average"]
(8, 4.0)
>>> analyze_text("no numbers here")["average"]
0.0
"""


def count_characters(text: str) -> int:
    """Count characters that are not whitespace."""
    sayac = 0

    for harf in text:
        if not harf.isspace():
            sayac += 1

    return sayac


def count_words(text: str) -> int:
    """Count number of whitespace-separated words."""
    return len(text.split())


def extract_numbers(text: str) -> list[int]:
    """Return a list of the integers found in text, in order."""
    sayilar = []

    for kelime in text.split():
        temiz_kelime = kelime.rstrip(".,!?;:")

        if temiz_kelime.isdigit():
            sayilar.append(int(temiz_kelime))
        elif temiz_kelime.startswith("-") and temiz_kelime[1:].isdigit():
            sayilar.append(int(temiz_kelime))

    return sayilar


def analyze_text(text: str) -> dict:
    """Return a dict with characters, words, numbers, sum and average."""
    karakter = count_characters(text)
    kelime = count_words(text)
    sayilar = extract_numbers(text)

    toplam = sum(sayilar)

    if len(sayilar) > 0:
        ortalama = toplam / len(sayilar)
    else:
        ortalama = 0.0

    return {
        "characters": karakter,
        "words": kelime,
        "numbers": sayilar,
        "sum": toplam,
        "average": ortalama
    }


if __name__ == "__main__":
    metin = input("Enter text: ")
    sonuc = analyze_text(metin)

    print(f"Characters (no spaces): {sonuc['characters']}")
    print(f"Words: {sonuc['words']}")
    print(f"Numbers: {sonuc['numbers']}")
    print(f"Sum: {sonuc['sum']}")
    print(f"Average: {sonuc['average']:.2f}")
