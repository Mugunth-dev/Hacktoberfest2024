#Reverse Words in a Sentence
def reverse_words(sentence):
    """ Split the input string by ' ' while 
    ignoring multiple consecutive spaces """
    words = [word for word in sentence.split(' ') if word]
    
    # Reverse the words
    words.reverse()
    
    # Join the reversed words back into a string
    return ' '.join(words)
