#Reverse Words in a Sentence
def reverse_words(sentence):
    """Reverses the order of words in the sentence."""
    # Step 1: Split the sentence into words
    words = sentence.split()

    # Step 2: Reverse the list of words
    reversed_words = words[::-1]

    # Step 3: Join the reversed words into a sentence
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence
