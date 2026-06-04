from fastapi import FastAPI

app = FastAPI(
    title="AE-CNN Ensemble NIDS",
    description="Network Intrusion Detection System using Autoencoder and CNN Ensemble",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "AE-CNN Ensemble Network Intrusion Detection System is running successfully"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
