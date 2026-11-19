# Python Tutorial

Code for the tutorials on my YouTube channel, [Manusia Setengah Chi Kuadrat](https://www.youtube.com/c/ManusiaSetengahChiKuadrat). It covers machine learning, deep learning, NLP, computer vision and model deployment in Python.

> Some videos don't have code here because the files were lost when I changed laptops.

## How to run

- **Google Colab (easiest):** click **Open** next to any notebook. Most notebooks install their own dependencies in the first cells.
- **Locally:** install [Jupyter](https://jupyter.org/install), then install the packages imported at the top of the notebook (for example `pip install scikit-learn pandas`).

Some notebooks need a data file you provide yourself. Where that's the case, the first cell says which file and where to put it.

## Contents

### Regression

| Notebook | Topic | Colab |
|---|---|---|
| [ElasticNet Regression](Regression/ElasticNet_Regression.ipynb) | Elastic Net regression | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Regression/ElasticNet_Regression.ipynb) |
| [Lasso Regression](Regression/Lasso_Regression.ipynb) | Lasso regression | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Regression/Lasso_Regression.ipynb) |
| [Multinomial Logistic Regression](Regression/Multinomial_Logistic_Regression.ipynb) | Multinomial logistic regression | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Regression/Multinomial_Logistic_Regression.ipynb) |
| [Ridge Regression](Regression/Ridge_Regression.ipynb) | Ridge regression | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Regression/Ridge_Regression.ipynb) |
| [Zero Inflated Poisson](Regression/Zero_Inflated_Poisson.ipynb) | Zero-inflated Poisson regression | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Regression/Zero_Inflated_Poisson.ipynb) |

### Classification

| Notebook | Topic | Colab |
|---|---|---|
| [CatBoost](Classification/CatBoost.ipynb) | Gradient boosting with CatBoost | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Classification/CatBoost.ipynb) |
| [KNN](Classification/KNN.ipynb) | K-Nearest Neighbors | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Classification/KNN.ipynb) |

### Clustering

| Notebook | Topic | Colab |
|---|---|---|
| [K Modes](Clustering/K_Modes.ipynb) | K-Modes for categorical data | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Clustering/K_Modes.ipynb) |
| [K Prototypes](Clustering/K_Prototypes.ipynb) | K-Prototypes for mixed data | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Clustering/K_Prototypes.ipynb) |

### Forecasting

| Notebook | Topic | Colab |
|---|---|---|
| [Exponential Smoothing](Forecasting/Exponential_Smoothing.ipynb) | Exponential smoothing (Holt-Winters) | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Forecasting/Exponential_Smoothing.ipynb) |
| [Sarimax](Forecasting/Sarimax.ipynb) | SARIMAX | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Forecasting/Sarimax.ipynb) |

### ML Support

| Notebook | Topic | Colab |
|---|---|---|
| [Distance Metrics](ML_Support/Distance_Metrics.ipynb) | Distance metrics | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/ML_Support/Distance_Metrics.ipynb) |
| [Handling Categorical Data](ML_Support/Handling_Categorical_Data.ipynb) | Encoding categorical data | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/ML_Support/Handling_Categorical_Data.ipynb) |

### AutoML

| Notebook | Topic | Colab |
|---|---|---|
| [Auto Sklearn](AutoML/Auto_Sklearn.ipynb) | AutoML with auto-sklearn | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/AutoML/Auto_Sklearn.ipynb) |
| [H2O](AutoML/H2O.ipynb) | H2O AutoML for classification | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/AutoML/H2O.ipynb) |
| [H2O AutoML Regression](AutoML/H2O_AutoML_Regression.ipynb) | H2O AutoML for regression | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/AutoML/H2O_AutoML_Regression.ipynb) |

### Market Basket Analysis

| Notebook | Topic | Colab |
|---|---|---|
| [Arules](MBA/Arules.ipynb) | Market basket analysis (association rules) | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/MBA/Arules.ipynb) |

### NLP

| Notebook | Topic | Colab |
|---|---|---|
| [CAMeL Tools Guided Tour](NLP/CAMeL_Tools_Guided_Tour.ipynb) | Arabic NLP with CAMeL Tools | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/NLP/CAMeL_Tools_Guided_Tour.ipynb) |
| [Doc2vec](NLP/Doc2vec.ipynb) | Document embeddings with Doc2Vec | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/NLP/Doc2vec.ipynb) |
| [Google Trans New](NLP/Google_Trans_New.ipynb) | Translation with google_trans_new | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/NLP/Google_Trans_New.ipynb) |
| [NMT with Attention](NLP/NMT_with_Attention.ipynb) | Neural machine translation with attention | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/NLP/NMT_with_Attention.ipynb) |
| [Negative Sampling Skipgram](NLP/Negative_Sampling_Skipgram.ipynb) | Word2Vec skip-gram with negative sampling | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/NLP/Negative_Sampling_Skipgram.ipynb) |
| [PPO Training](NLP/PPO_Training.ipynb) | Tune GPT-2 with PPO (RLHF) | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/NLP/PPO_Training.ipynb) |
| [PyThaiNLP](NLP/PyThaiNLP.ipynb) | Thai NLP with PyThaiNLP | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/NLP/PyThaiNLP.ipynb) |
| [Sentiment Classification BERT](NLP/Sentiment_Classification_BERT.ipynb) | Sentiment classification with BERT | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/NLP/Sentiment_Classification_BERT.ipynb) |
| [Sentiment TF IDF](NLP/Sentiment_TF_IDF.ipynb) | Sentiment classification with TF-IDF | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/NLP/Sentiment_TF_IDF.ipynb) |
| [Word Embedding](NLP/Word_Embedding.ipynb) | Word embeddings | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/NLP/Word_Embedding.ipynb) |
| [seq2seq](NLP/seq2seq.ipynb) | Sequence-to-sequence model | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/NLP/seq2seq.ipynb) |

### Computer Vision

| Notebook | Topic | Colab |
|---|---|---|
| [Autoencoder](Computer_Vision/Autoencoder.ipynb) | Autoencoder | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Computer_Vision/Autoencoder.ipynb) |
| [CNN](Computer_Vision/CNN.ipynb) | Convolutional Neural Network | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Computer_Vision/CNN.ipynb) |
| [GAN](Computer_Vision/GAN.ipynb) | GAN and WGAN | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Computer_Vision/GAN.ipynb) |
| [Image Captioning with Attention](Computer_Vision/Image_Captioning_with_Attention.ipynb) | Image captioning with attention | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Computer_Vision/Image_Captioning_with_Attention.ipynb) |
| [OCR](Computer_Vision/OCR.ipynb) | Optical Character Recognition | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Computer_Vision/OCR.ipynb) |
| [Object Counting in Image](Computer_Vision/Object_Counting_in_Image.ipynb) | Counting objects in an image | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Computer_Vision/Object_Counting_in_Image.ipynb) |
| [Transfer Learning](Computer_Vision/Transfer_Learning.ipynb) | Transfer learning | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Computer_Vision/Transfer_Learning.ipynb) |

### Audio

| Notebook | Topic | Colab |
|---|---|---|
| [Tutorial Wav2vec2](Audio/Tutorial_Wav2vec2.ipynb) | Fine-tune Wav2Vec2 for speech recognition | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Audio/Tutorial_Wav2vec2.ipynb) |
| [whisper in transformers](Audio/whisper_in_transformers.ipynb) | Speech-to-text with Whisper (Hugging Face Transformers) | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Audio/whisper_in_transformers.ipynb) |

### Multimodal

| Notebook | Topic | Colab |
|---|---|---|
| [OpenAI CLIP](Multimodal/OpenAI_CLIP.ipynb) | Image-text matching with OpenAI CLIP | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Multimodal/OpenAI_CLIP.ipynb) |

### Graph

| Notebook | Topic | Colab |
|---|---|---|
| [NetworkX](Graph/NetworkX.ipynb) | Network analysis with NetworkX | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Graph/NetworkX.ipynb) |
| [Node2Vec](Graph/Node2Vec.ipynb) | Node embeddings with Node2Vec | [Open](https://colab.research.google.com/github/Syukrondzeko/Python-Tutorial/blob/master/Graph/Node2Vec.ipynb) |

### Deployment

Serving a model with [FastAPI](Deployment/FastAPI/Linear_Regression_FastAPI) and [Streamlit](Deployment/Streamlit/Linear_Regression_Streamlit), plus a simple [Flask blog](Deployment/Flask/Blog_Flask). See the [Deployment README](Deployment/README.md) for how to run them.

## License

[MIT](LICENSE). Notebooks adapted from other projects (CAMeL Tools Guided Tour, TRL PPO example, H2O AutoML demo) credit their original authors in the first cell and remain under their original licenses.
