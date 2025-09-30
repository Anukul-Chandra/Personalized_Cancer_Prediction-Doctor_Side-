import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import pickle
import logging
import os

# Logging setup
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# CORS setup (allow frontend at port 5501)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins for stricter CORS
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load pipelines/models
models = {}
performances = {}

try:
    with open("final_pipeline1.pkl", "rb") as f:
        saved = pickle.load(f)

        if isinstance(saved, dict):
            models = saved.get("models", {})
            performances = saved.get("performance", {})
            if models:
                logging.info("✅ Multiple models loaded successfully")
            else:
                logging.warning("⚠️ Pickle file loaded but no models found in dictionary")
        else:
            models = {"DefaultModel": saved}
            performances = {"DefaultModel": "N/A"}
            logging.info("✅ Single model pipeline loaded successfully")

except Exception as e:
    logging.error(f"❌ Error loading pipelines: {e}")
    models, performances = {}, {}

# Serve index.html
@app.get("/", response_class=HTMLResponse)
async def index():
    try:
        with open("index.html", "r") as f:
            return f.read()
    except Exception as e:
        logging.error(f"❌ Error loading index.html: {e}")
        return f"<h2>❌ Error loading index.html: {e}</h2>"

# Input schema
class InputData(BaseModel):
    Gene: str
    Variation: str
    Text: str

# Prediction route
@app.post("/predict")
async def predict(data: InputData):
    try:
        if not models:
            raise ValueError("No models loaded")

        # Prepare input
        input_df = pd.DataFrame([{
            "Gene": data.Gene.lower().replace(" ", "_"),
            "Variation": data.Variation.lower().replace(" ", "_"),
            "Text": data.Text.lower()
        }])

        all_results = {}
        final_prediction = None
        max_acc_model = None
        max_acc = -1.0

        for name, model in models.items():
            pred = int(model.predict(input_df)[0])

            # Confidence (if available)
            try:
                proba = model.predict_proba(input_df)[0]
                confidence = round(max(proba) * 100, 2)
            except Exception:
                confidence = None

            # Safely parse accuracy
            raw_acc = performances.get(name, "N/A")
            try:
                model_acc = float(raw_acc)
            except (ValueError, TypeError):
                model_acc = 0.0

            all_results[name] = {
                "accuracy": raw_acc,
                "prediction": pred,
                "confidence": confidence
            }

            # Track best model
            if model_acc > max_acc:
                max_acc = model_acc
                max_acc_model = name
                final_prediction = pred

        return {
            "all_models": all_results,
            "prediction": final_prediction,
            "confidence": (
                f"{all_results[max_acc_model]['confidence']}%" if max_acc_model and all_results[max_acc_model]['confidence'] else "N/A"
            ),
            "most_accurate_model": max_acc_model
        }

    except Exception as e:
        logging.error(f"❌ Prediction error: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Run server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=8000)
