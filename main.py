def get_sponged_word(word):
    chars = list(word)
    for i in range(len(chars)):
        try:
            if chars[i] == 'i' and chars[i+1] != 'i':
                chars[i+1] = chars[i+1].upper()
        except IndexError:
            pass
        if chars[i] == 'l' or (chars[i] != 'i' and is_odd(i)):
            chars[i] = chars[i].upper()
    return "".join(chars)


def is_odd(num):
    return (num % 2) == 1


user_text = input("Please enter text to be put into Spongebob Case:\n")
words = user_text.strip().split()
sponged_words = [get_sponged_word(word.lower()) for word in words]

print(" ".join(sponged_words))
