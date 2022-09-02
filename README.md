## ML as Service
Transform ML models to Service with:
- Flask
- Gunicorn
- Docker

## Examples
### [ML](ml_as_service/ml)
Scikit-learn model trained on 20newsgroups dataset dumped as .joblib file.

Inference:
```
python ml_as_service/ml/inference.py \
--path_to_model "ml_as_service/ml/models/model.joblib" \
--path_to_email "ml_as_service/ml/email.txt"
```
