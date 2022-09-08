# ML as Service
Scikit-learn model trained on 20newsgroups dataset dumped as .joblib file.

Inference:
```
python inference.py \
--path_to_model "models/model.joblib" \
--path_to_email "email.txt"
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
docker build -t ml_as_service .
docker run -p 5000:5000 ml_as_service
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
# {"info": "sklearn"}
```
- `predict`:
```
curl http://localhost:5000/predict -F "email=@email.txt"
# {"result": "rec"}
```
