def check_magazine(magazine: list, note: list):
    magazine_words = {}
    for word in magazine:
        if word in magazine_words:
            magazine_words[word] += 1
        else:
            magazine_words[word] = 1

    for word in note:
        if word in magazine_words:
            magazine_words[word] -= 1
            if magazine_words[word] < 0:
                return False
        else:
            return False

    return True

def main():
    pass

if __name__ == "__main__":
    main()