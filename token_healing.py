import torch
import spacy
import re
from gingerit.gingerit import GingerIt
from transformers import BertTokenizer, BertForMaskedLM

# initializing gingerit parser
parser=GingerIt()

# Loading BERT Tokenizer and model
model_name="bert-base-uncased"
tokenizer=BertTokenizer.from_pretrained(model_name)
model=BertForMaskedLM.from_pretrained(model_name)
model.eval()

#here load spacy model
nlp=spacy.load("en_core_web_sm")

#definig function for correct spelling & grammer
def correct_spelling_and_grammer(text):
  result=parser.parse(text)
  return result['result']

#define function for add missing word in givens string
def add_missing_words(text):
  doc=nlp(text)
  missing_words=[token.text for token in doc if token.is_alpha and not token.is_stop]

  #Finding missing words using BERT
  for i, token in enumerate(doc):
    if token.text in missing_words:
      masked_text=text.replace("[missing]","[mask]", 1)
      encode_input=tokenizer.encode_plus(masked_text, return_tensors="pt", padding=True, truncation=True, max_length=512)
      input_ids=encode_input["input_ids"][0]
      attention_mask=encode_input["attention_mask"][0]

      with torch.no_grad():
        logits=model(input_ids.unsqueeze(0),attention_mask=attention_mask.unsqueeze(0)).logits 
      masked_index=torch.where(input_ids==tokenizer.mask_token_id)[0]

      if len(masked_index)>0:
        predicted_token_index=torch.argmax(logits[0, masked_index]).item()
        predicted_token=tokenizer.decode([predicted_token_index])

        #replace the missing word with the predicted token
        text=text.replace("[missing]", predicted_token, 1)
  return text

#define fucntion for remove duplicate or repeated or extra word from given string
def remove_dupli_words(text):
  #use regular pattern to find dulpicate words with or without punctuation
    pattern = r'\b(\w+[^\w\s]?)(\W+\1\b)+'
    
    new_text = re.sub(pattern, r'\1', text)
    return new_text

text=input("Enter text : ")

#call the finction for removing spelling errors and grammatical errors from givven string
corrected_spelling_grammer_text=correct_spelling_and_grammer(text)

#call the function for add missing words in given string if any exist
new_text_with_missing_words=add_missing_words(corrected_spelling_grammer_text)

#call the function for remove duplication or extra words from given string
final_new_text=remove_dupli_words(new_text_with_missing_words)

print("Corrected text : ",final_new_text )