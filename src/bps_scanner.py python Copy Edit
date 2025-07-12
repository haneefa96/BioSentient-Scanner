import json
from ai_model import predict_bioscore

def scan_plastic_sample(sample_data):
    print("Scanning plastic sample...")
    bioscore = predict_bioscore(sample_data)
    print(f"BioScore: {bioscore}")
    if bioscore >= 80:
        recommendation = "Compostable"
    elif 40 <= bioscore < 80:
        recommendation = "Recycle with care"
    else:
        recommendation = "Landfill — not biodegradable"
    
    result = {
        "bioscore": bioscore,
        "recommendation": recommendation,
        "additives_detected": sample_data.get("additives", [])
    }
    return result

if __name__ == "__main__":
    with open("data/sample_scans.json") as f:
        sample_data = json.load(f)
    result = scan_plastic_sample(sample_data)
    print(json.dumps(result, indent=2))
