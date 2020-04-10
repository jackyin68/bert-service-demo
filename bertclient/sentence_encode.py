from bert_serving.client import BertClient

bc = BertClient()
sentences_encode = bc.encode(['First do it', 'then do it right', 'then do it better'])
print(len(sentences_encode))
for sentence in sentences_encode:
    print(len(sentence), sentence)
    print('*' * 100)

sentences_encode = bc.encode(['First do it ||| then do it right'])
print(len(sentences_encode))
for sentence in sentences_encode:
    print(len(sentence), sentence)
    print('*' * 100)
