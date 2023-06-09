# Token_Healling_project
Token healing is a technique used to correct errors in text by identifying and replacing incorrect or mistyped tokens(word) with their intended correct forms.

This is a python program. which is used to correct errors in text by identifying and replacing misspelled or mistyped tokens with their intended correct forms. 

This Python script aims to enhance the readability and coherence of text. The algorithm of token healing technique consists of three main steps:
1. Spelling and grammer correction
2. Addition of missing word
3. Removal of duplicate/extra words

# Installation
Make sure you have Python 3.x installed in your system.

To run this Python script, you need to install the following dependencies:
  1. gingerit: A python library for spelling and grammer correction.
  2. torch: the PyTorch library for deep learning.
  3. transformers: the transformers library for natural language processing.
  4. spacy: A Python library for natural language processing.

You can install the required dependencies using the following commond:
  pip install gingerit
  pip install torch
  pip install spacy
  pip install transformers
  python -m spacy download en_core_web_sm
  
# Usage
You have an active internet connection for using this script.
To use the token healing script, follow these steps:
  1. Run the "token_healing.py" file in your IDE
  2. The program will prompt the user to enter the text (type or copy & paste the text you want to enter)
  3. Then the program will process the input and give an output of modified text(corrected text, if needed).

# Working 
  1. torch: This is the main library used for deep learing and tensor computation.
  2. spacy: A popular library used for natural language processing(NLP) task.
  3. re: The regular expression module for pattern matching and string manipulation.
  4. GingerIt from gingerit library: A parser for spelling and grammer correction.
  BertTokenizer and BertForMaskedLM from the transformsers library. componants for utilizing BERT(Bidirectional Encoder representations from Transformers) model for masked language modeling.

# Initialization
  1. parser: An instance of GingerIt is created, which will be used for spelling and grammer correction.
  2. BERT Model Setup: model_name: Specifies the name of the pre-trained BERT model to be used (bet-base-uncased).tokenizer: Initializes a BERT tokenizer from the specifies pre-trained mo del. model: Loads a pre-trained BERT model for masked language modeling and sets it to evaluation mode.
  4. Spacy Model Setup: THe Englidh language model(en_core_web_sm) is loaded into the nlp object.
  
# Function Definitions
  1. correct_spelling_and_grammer: This function takes a text as input and uses the parser object to parse and correct the spelling and grammar of the text. The corrected result is returned.
  2. add_missing_words: This function takes a text as input and process itwiththe help of BERT. it identifies missing words(tokens) in the input text byreplacing them with the "[ MISSING ]" placeholder. The BERT model predicts the missing word, which is then substitute back in the text. The function returns the text with missing words added.
  3. remove_dupli_words: This function takes a text as input and utilizes a regular expression pattern to identify duplicate or extra words, including those with punctuation. It removes the duplicates and returns the deduplicated text.

# User Input
The code prompts the user to enter the text.

# Output 
The Modified text, after going through the text processing pipeline, is printed as "Corrected text".

# Sample Output
  ### Sample input 1 :
  I I I aam veY thirsty thirsty.can you plese give guve [MISSING] a glass of [MISSING]? the [MISSING] fox ased the rabbit. I dont have water, the [MISSING] replied.
  ### Sample output 1 : 
  I am very thirsty. Can you please give me a glass of water? The white fox asked the rabbit. I don't have water, the rabbit replied.
  
  ### Sample input 2 : 
  I will go to the office yesterday!
  ### Sample output 2 : 
  I went to the office yesterday! 
