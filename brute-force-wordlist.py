import itertools
import string


def insert_special_characters(word):
    special_chars = string.punctuation
    variations = set()

    # Kelimenin başına ve sonuna özel karakterler ekleyelim
    for char in special_chars:
        variations.add(char + word)
        variations.add(word + char)

    # Kelimenin arasına özel karakterler ekleyelim
    for i in range(1, len(word)):
        for char in special_chars:
            variations.add(word[:i] + char + word[i:])

    return variations


def generate_combinations(words):
    combinations = set()  # Set kullanarak tekrarları önleriz
    for r in range(1, len(words) + 1):
        for combo in itertools.combinations(words, r):
            for perm in itertools.permutations(combo):
                word = ''.join(perm)
                # Kombinasyonlar ve permütasyonlar
                combinations.add(word)
                combinations.add(word[::-1])  # Tersten ekleme
                combinations.add(word.capitalize())
                combinations.add(word.capitalize()[::-1])  # Tersten capitalize ekleme
                if len(word) > 1:
                    combinations.add(word[:-1] + word[-1].upper())
                    combinations.add((word[:-1] + word[-1].upper())[::-1])  # Tersten son harfi büyük ekleme
                if len(word) > 1:
                    combinations.add(word[0].upper() + word[1:-1] + word[-1].upper())
                    combinations.add((word[0].upper() + word[1:-1] + word[-1].upper())[
                                     ::-1])  # Tersten hem ilk hem son harfi büyük ekleme
                combinations.add(word.upper())
                combinations.add(word.upper()[::-1])  # Tersten tamamen büyük harfli ekleme
                combinations.add(word.lower())
                combinations.add(word.lower()[::-1])  # Tersten tamamen küçük harfli ekleme

                # Özel karakterli kombinasyonlar
                special_variations = insert_special_characters(word)
                for var in special_variations:
                    combinations.add(var)
                    combinations.add(var[::-1])  # Tersten ekleme
                    combinations.add(var.capitalize())
                    combinations.add(var.capitalize()[::-1])  # Tersten capitalize ekleme
                    if len(var) > 1:
                        combinations.add(var[:-1] + var[-1].upper())
                        combinations.add((var[:-1] + var[-1].upper())[::-1])  # Tersten son harfi büyük ekleme
                    if len(var) > 1:
                        combinations.add(var[0].upper() + var[1:-1] + var[-1].upper())
                        combinations.add((var[0].upper() + var[1:-1] + var[-1].upper())[
                                         ::-1])  # Tersten hem ilk hem son harfi büyük ekleme
                    combinations.add(var.upper())
                    combinations.add(var.upper()[::-1])  # Tersten tamamen büyük harfli ekleme
                    combinations.add(var.lower())
                    combinations.add(var.lower()[::-1])  # Tersten tamamen küçük harfli ekleme

    return combinations


def generate_wordlist():
    # Kullanıcıdan kaç kelime isteyeceğini sor
    num_words = int(input("Kaç tane kelime gireceksiniz? "))

    # Kullanıcıdan kelimeleri al
    words = []
    for i in range(num_words):
        word = input(f"{i + 1}. kelimeyi girin: ")
        words.append(word)

    # Tüm olası kombinasyonları oluştur
    wordlist = generate_combinations(words)

    # Parola listesini txt dosyasına kaydet
    with open("wordlist.txt", "w") as file:
        for password in wordlist:
            file.write(password + "\n")

    print("Parola listesi 'wordlist.txt' dosyasına kaydedildi.")


# Programı çalıştır
generate_wordlist()
