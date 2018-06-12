"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_path)

    return file.read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    words_lst = text_string.strip().split()
    chains = {}

    for i in range(len(words_lst) - 2):
        key = (words_lst[i], words_lst[i+1])
        chains[key] = chains.get(key, [])
        chains[key].append(words_lst[i+2])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    keys_lst = list(chains.keys())
    init_key = choice(keys_lst)
    words.extend(init_key)

    next_word = choice(chains[init_key])
    words.append(next_word)

    while True:
        next_key = (words[-2], words[-1])

        if next_key in chains:
            next_word = choice(chains[next_key])
            words.append(next_word)

        else:
            break

    return " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
