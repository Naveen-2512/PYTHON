
def are_anagrams(word1, word2):
    # Remove spaces and convert to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Compare sorted characters
    return sorted(word1) == sorted(word2)


def character_count(word):
    # Count each character using a dictionary
    count = {}

    for ch in word.lower():
        if ch != " ":
            count[ch] = count.get(ch, 0) + 1

    return count


def find_anagrams(words, target):
    # Find words that are anagrams of the target
    result = []

    for word in words:
        if are_anagrams(word, target):
            result.append(word)

    return result


def main():
    words = input("Enter words separated by spaces: ").split()
    target = input("Enter the target word: ")

    matches = find_anagrams(words, target)

    print("\nTarget word:", target)
    print("Anagram matches:", matches)
    print("Character count:", character_count(target))

    if len(matches) > 0:
        print("Anagrams found successfully.")
    else:
        print("No anagrams found.")


if __name__ == "__main__":
    main()
