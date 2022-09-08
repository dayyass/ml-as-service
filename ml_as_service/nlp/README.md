# BERT as Service
Transformers model tuned on CoNLL-2003 dataset.

Inference:
```
python inference.py \
--path_to_model "models/bert-base-NER" \
--sentence "My name is Wolfgang and I live in Berlin"
```

### Service
Launch the Flask service:
```
python api.py
```

Launch the Flask + Gunicorn service:
```
gunicorn --config gunicorn.conf.py api:app
```

Launch the Flask + Gunicorn + Docker service:
```
docker build -t nlp_as_service .
docker run -p 5000:5000 nlp_as_service
```

Endpoints:
- `health`:
```
curl http://localhost:5000/health
# {"status": "UP"}
```
- `info`:
```
curl http://localhost:5000/info
# {"info": "transformers"}
```
- `predict`:
```
curl -X POST http://localhost:5000/predict \
-H 'Content-Type: application/json' \
-d '{"sentence": "My name is Wolfgang and I live in Berlin"}'
# {
#     "result": "\"[
#         {'entity': 'B-PER', 'score': 0.9990139, 'index': 4, 'word': 'Wolfgang', 'start': 11, 'end': 19},
#         {'entity': 'B-LOC', 'score': 0.999645, 'index': 9, 'word': 'Berlin', 'start': 34, # 'end': 40}
#     ]\""
# }
```
