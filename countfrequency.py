def count_frequencies(input):

    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
   
    # split the string object into a list of strings containing individual words
    word_list = []
    elements = input.split('\n')
    for element in elements:
        if element != '':
            for word in element.split(' '):
                word_list.append(word.lower())

    print(word_list)
    
    # process the text; remove unwanted punctuations
    result = {}
    for word in word_list:
        temp = ''
        for char in word:
            if char.isalpha():
                temp += char
        # check against the uninteresting_words list; drop the word if it's in the list
        if temp not in uninteresting_words:
            # add the word into a dictionary and return the dictionary
            if temp in result.keys():
                result[temp] += 1
            else:
                result[temp] = 1

    return result
    
    
    
    

text = '''
For this project, you'll create a "word cloud" from a text by writing a script. This script needs to process the text, remove punctuation, ignore case and words that do not contain all alphabets, count the frequencies, and ignore uninteresting or irrelevant words. A dictionary is the output of the calculate_frequencies function. The wordcloud module will then generate the image from your dictionary.

For the input text of your script, you will need to provide a file that contains text only. For the text itself, you can copy and paste the contents of a website you like. Or you can use a site like Project Gutenberg to find books that are available online. You could see what word clouds you can get from famous books, like a Shakespeare play or a novel by Jane Austen. Save this as a .txt file somewhere on your computer.

Now you will need to upload your input file here so that your script will be able to process it. To do the upload, you will need an uploader widget. Run the following cell to perform all the installs and imports for your word cloud script and uploader widget. It may take a minute for all of this to run and there will be a lot of output messages. But, be patient. Once you get the following final line of output, the code is done executing. 

Then you can continue on with the rest of the instructions for this notebook.
'''

print(count_frequencies(text))