# BioSentient-Scanner
# 🧪 BioSentient Plastics Scanner (BPS)

### A Smart Biodegradability Grader for Real Plastics, Real Time

## 🚀 Problem Tackled

Many plastics labeled “biodegradable” aren’t. Mislabeling causes confusion, improper disposal, and worsens global pollution.

## 💡 Solution: BioSentient Plastics Scanner

BPS is a handheld or drone-mounted device that uses **multi-spectrum scanning**, **AI-powered spectroscopy**, and **chemical analysis** to:

- **Analyze** a plastic’s chemical structure in real-time.
- **Assign a BioScore** — a biodegradability and environmental impact score.
- **Detect greenwashing** — verify false eco-claims on packaging.
- **Recommend correct disposal methods** (recycle, compost, landfill).

---

## 🎯 Key Features

- ✅ AI modeling to predict degradation under various conditions (ocean, compost, landfill).
- ✅ Detects additives that prevent biodegradation.
- ✅ Scalable to drones, robots, and sorting centers.
- ✅ Helps consumers and governments make smarter decisions.

---

## 📊 Tech Stack

- Python 🐍
- AI/ML Model: PyTorch / Scikit-learn (placeholder)
- Spectral Analysis: OpenCV + SciPy + NumPy
- Data Format: JSON-based Scan Output

---

## 🧠 How It Works

1. **Scan**: Multi-spectral light scans a plastic object.
2. **Analyze**: AI model evaluates chemical structure and additives.
3. **Score**: Outputs a `BioScore` (0-100) + recommended action.
4. **Verify**: Labels and packaging claims are validated.

---

## 📁 File Structure
## ⚙️ Setup & Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/haneefa96/BioSentient-Scanner.git
   cd BioSentient-Scanner
## Technical Architecture
- **Hardware**: Compact NIR spectrometer (e.g., Texas Instruments DLP NIRscan), ARM-based microcontroller, OLED display for BioScore.
- **Software**: Python-based AI model (TensorFlow) trained on polymer degradation datasets to predict BioScore and degradation timelines.
- **Workflow**: 
  1. Scan plastic using NIR spectroscopy.
  2. Extract chemical composition (e.g., polymer type, additives).
  3. AI model predicts biodegradability and environmental impact.
  4. Output BioScore (0-100) and disposal recommendation.
