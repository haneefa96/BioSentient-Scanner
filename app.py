from flask import Flask, request, render_template, jsonify
from src.ai_model import predict_bioscore

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.get_json() or request.form
        material = data.get("material", "")
        additives = data.get("additives", [])

        sample_data = {
            "material": material,
            "additives": additives if isinstance(additives, list) else []
        }
        bioscore = predict_bioscore(sample_data)

        if bioscore >= 80:
            recommendation = "Compostable"
        elif 40 <= bioscore < 80:
            recommendation = "Recycle with care"
        else:
            recommendation = "Landfill — not biodegradable"

        result = {
            "bioscore": bioscore,
            "recommendation": recommendation,
            "additives_detected": sample_data["additives"]
        }

        # Return JSON if requested (API style)
        if request.is_json:
            return jsonify(result)

        # Or render result on webpage
        return render_template("result.html", result=result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
