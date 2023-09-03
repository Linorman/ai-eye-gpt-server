# ai-eye-gpt-server
## 1. Introduction
#### This project is a server for AI Eye GPT. It is based on GPT-2 and provide a http api to interact with the model.
## 2. Installation
#### 2.1. Install Python 3.9
#### 2.2. Install pipenv
#### 2.3. Install dependencies
```bash
pipenv install
```
## 3. Run the server
```bash
pipenv run python app.py
```
## 4. API
#### 4.1. /api/v1/predict
##### 4.1.1. Request
```json
{
    "text": "string",
    "length": "int"
}
```
##### 4.1.2. Response
```json
{
    "text": "string"
}
```