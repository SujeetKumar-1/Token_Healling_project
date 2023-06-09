import torch
import spacy
import string
import logging
import re
from gingerit.gingerit import GingerIt
from transformers import BertTokenizer, BertForMaskedLM

logging.getLogger("transformers").setLevel(logging.ERROR)

# Initializing GingerIt parser
parser = GingerIt()

# Load BERT tokenizer and model
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForMaskedLM.from_pretrained(model_name)
model.eval()
    
# Load spacy model
nlp = spacy.load("en_core_web_sm")


def correct_spelling_and_grammar(text):
    result = parser.parse(text)
    return result['result']

def add_missing_words(text):
    doc = nlp(text)
    missing_words = [token.text for token in doc if token.is_alpha and not token.is_stop]

    # Generate missing words using BERT
    for i, token in enumerate(doc):
        if token.text in missing_words:
            masked_text = text.replace("[MISSING]", "[MASK]", 1)
            encoded_input = tokenizer.encode_plus(masked_text, return_tensors="pt", padding=True, truncation=True, max_length=512)
            input_ids = encoded_input["input_ids"][0]
            attention_mask = encoded_input["attention_mask"][0]

            with torch.no_grad():
                logits = model(input_ids.unsqueeze(0), attention_mask=attention_mask.unsqueeze(0)).logits

            masked_index = torch.where(input_ids == tokenizer.mask_token_id)[0]

            if len(masked_index) > 0:
                predicted_token_index = torch.argmax(logits[0, masked_index]).item()
                predicted_token = tokenizer.decode([predicted_token_index])

                # Replace the missing word with the predicted token
                text = text.replace("[MISSING]", predicted_token, 1)

    return text

def remove_duplicate_words(text):
    # Use regular expression to find consecutive duplicate words with or without punctuation
    pattern = r'\b(\w+[^\w\s]?)(\W+\1\b)+'
    
    deduplicated_text = re.sub(pattern, r'\1', text)
    return deduplicated_text

text = input("Enter text : ")

#removing spelling errors and grammatical errors
corrected_spelling_grammar_text = correct_spelling_and_grammar(text)

#adding any missing words
final_text_with_missing_words  = add_missing_words(corrected_spelling_grammar_text)

#removing consecutive duplicates or extra words
deduplicated_final_text = remove_duplicate_words(final_text_with_missing_words)

print("Corrected text : ", deduplicated_final_text)
