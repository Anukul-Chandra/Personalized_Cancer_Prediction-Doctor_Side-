
# 🩺 Personalized Cancer Prediction for Doctors

A machine learning-driven web application that provides personalized cancer risk predictions. Built with FastAPI and powered by multiple ML models, this tool helps healthcare professionals and researchers analyze genetic mutation data to generate detailed cancer risk assessments. 

🎯 **Feature**
- ✨ **Multiple ML Model Support** - Choose from various trained models for different cancer prediction scenarios
- 🚀 **FastAPI Backend** - High-performance, modern Python web framework for lightning-fast predictions
- 📊 **Detailed Prediction Results** - Get comprehensive risk assessments with probability scores
- 🌐 **CORS Enabled** - Seamlessly integrate with any frontend application
- 🧠 **Intelligent Model Selection** - Automatically loads the appropriate model based on your request
- 🔒 **Production-Ready** - Built with best practices for deployment on cloud platforms## Demo

🌐 **Live Application**: 

You can see this project live here : :[https://personalized-cancer-prediction-doctor.onrender.com/](https://personalized-cancer-prediction-doctor.onrender.com/)

Visit the live demo to see the API in action! The application is hosted on Render and its free so some time takes time to loading requests.

## Project Sample Image  :
1.
<img width="2522" height="2082" alt="screencapture-personalized-cancer-prediction-doctor-g2k6-onrender-2025-09-30-12_49_22 (1)" src="https://github.com/user-attachments/assets/32157bfe-40d9-4f7b-8a67-fba3aa65095e" />
2.
<img width="2522" height="2082" alt="screencapture-personalized-cancer-prediction-doctor-g2k6-onrender-2025-09-30-12_50_44" src="https://github.com/user-attachments/assets/25c68899-b725-4e9c-a19c-83eadbfbb682" />
3.
<img width="2522" height="2082" alt="screencapture-personalized-cancer-prediction-doctor-g2k6-onrender-2025-09-30-12_50_44 (1)" src="https://github.com/user-attachments/assets/66a6dcf1-3e6e-4295-a468-11a4d8fa2e15" />


## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps
1. **Clone the repository**
```bash
git clone <your-repo-url>
cd personalized-cancer-prediction-doctor
```

2. **Install required packages**
```bash
pip install fastapi uvicorn pandas python-multipart
```

3. **Add your trained model file**
Place your trained ML model (`.pkl` file) in the project directory. The application expects a pickle file containing your trained model.

4. **Run the application**
```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`
🚀## Deployment

This application is deployed on **Render** and can be deployed on other cloud platforms like Heroku, AWS, or Google Cloud.

### Deploying to Render (Recommended) 🎉

1. **Create a `requirements.txt` file**
```
fastapi
uvicorn
pandas
python-multipart
```

2. **Ensure your app uses `os.environ` for port configuration**
```python
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
```

3. **Push your code to GitHub**

4. **Connect to Render**
   - Go to [render.com](https://render.com)
   - Create a new Web Service
   - Connect your GitHub repository
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `uvicorn app:app --host 0.0.0.0 --port $PORT`

5. **Deploy!** 🚀

Your API will be live and ready to accept requests!
## Usage/Examples

### Making a Prediction Request
Send a POST request to the `/predict` endpoint with genetic mutation data.

**Required Input Fields:**

The API requires **ONLY** three fields for prediction:

- **gene**: The name of the gene where the mutation occurred (e.g., "BRCA1", "TP53", "EGFR")
- **variation**: The specific genetic variation or mutation (e.g., "D835Y", "V600E", "Amplification")
- **text**: Clinical evidence text describing the mutation and its context. This should include relevant medical literature, patient history, or clinical findings related to the genetic mutation.

### Example using cURL 💻
```bash
curl -X POST "https://personalized-cancer-prediction-doctor.onrender.com/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "gene": "BRCA1",
    "variation": "D835Y",
    "text": "The patient presents with a germline BRCA1 mutation. Clinical studies have shown that BRCA1 mutations are associated with increased risk of breast and ovarian cancer. Family history indicates multiple cases of breast cancer."
  }'
```

### Example using Python 🐍
```python
import requests

url = "https://personalized-cancer-prediction-doctor.onrender.com/predict"

data = {
    "gene": "TP53",
    "variation": "R273H",
    "text": "TP53 R273H is a hotspot mutation commonly found in various cancer types. This mutation affects the DNA-binding domain of the p53 protein, compromising its tumor suppressor function. The patient has a history of colorectal adenocarcinoma."
}

response = requests.post(url, json=data)
print(response.json())
```

**Response Format:**
```json
{
  "prediction": "Class_7",
  "probability": 0.89,
  "cancer_type": "Predicted cancer classification based on genetic mutation"
}
```
## Tech Stack

**Client:** React, Redux, TailwindCSS

**Server:** Python, FastAPI
## Authors


- [@Anukul Chandra](https://github.com/Anukul-Chandra)


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## License

[MIT](https://choosealicense.com/licenses/mit/)


