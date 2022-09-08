# ML as Service
Scikit-learn model trained on 20newsgroups dataset dumped as .joblib file.

Inference:
```
python inference.py \
--path_to_model "models/model.joblib" \
--path_to_email "email.txt"
```

### Service
Launch the service:
```
python api.py
```

# TODO:
```
gunicorn --config gunicorn.conf.py api:app
```

# TODO:
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
curl http://localhost:5000/predict -F "email=@ml_as_service/ml/email.txt"
# {"result": "rec"}
```
