from pyexpat import model
import torch
from transformers import  AutoTokenizer,BertConfig, BertForSequenceClassification

class Predictor :
    def __init__(self,path):
        config = BertConfig.from_pretrained("bert-base-uncased", from_tf=False, num_labels = 2, output_hidden_states=False)
        self.tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertForSequenceClassification.from_pretrained(path,config = config)
        self.model.eval()
    
    def encode(self,headline):
        encode_sent = self.tokenizer.encode_plus(headline,
                                            max_length = 223,
                                            return_token_type_ids=False,
                                            pad_to_max_length=True,
                                            return_attention_mask=True,
                                            return_tensors='pt' )
        sent_id = encode_sent['input_ids']
        sent_mask = encode_sent['attention_mask']
        return sent_id, sent_mask
    
    def predict(self,headline):
        input_ids, attention_mask = self.encode(headline)
        logits = self.model(input_ids,attention_mask).logits
        prediction = torch.argmax(logits, dim=1)
        if prediction == torch.tensor(0):
            return 0 
        else:
            return 1

if __name__ == "__main__" :
    predictor = Predictor("D:\\interview\\weights\\model30000")
    predictor.predict("Morning Market Movers")



    

