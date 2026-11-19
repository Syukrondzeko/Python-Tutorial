# Deployment

Examples of serving Python code as web apps.

| Folder | What it shows |
|---|---|
| `model/` | Trains a linear regression on `healthcare_dataset.csv` and saves it as pickle files |
| `FastAPI/Linear_Regression_FastAPI/` | REST API that serves the model |
| `Streamlit/Linear_Regression_Streamlit/` | Web form that serves the model |
| `Flask/Blog_Flask/` | Simple blog: `my_blog_1.py` (quick start) and `my_blog_2.py` (templates + Bootstrap) |

## Run the regression apps

```bash
# 1. Train the model (creates model/*.pkl)
pip install pandas scikit-learn
python model/regression.py

# 2a. FastAPI -> open http://127.0.0.1:8000/docs
cd FastAPI/Linear_Regression_FastAPI
pip install -r requirements.txt
uvicorn app:app --reload

# 2b. Streamlit
cd Streamlit/Linear_Regression_Streamlit
pip install -r requirements.txt
streamlit run app.py
```

## Run the Flask blog

```bash
cd Flask/Blog_Flask
pip install -r requirements.txt
python my_blog_2.py
```
