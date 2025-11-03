# Gradio Demos - PyCaret Assignment

This folder contains interactive web applications built with Gradio to demonstrate the trained PyCaret models.

## 📁 Demo Applications

### 1. Classification Demo (`demo_classification.py`)
**Heart Disease Prediction System**

An interactive interface for predicting heart disease based on patient medical data.

**Features:**
- 13 input parameters (age, blood pressure, cholesterol, etc.)
- Real-time prediction with confidence scores
- Risk level assessment (Low/Moderate/High)
- User-friendly sliders and radio buttons
- Medical recommendations based on prediction

**To Run:**
```bash
cd gradio_demos
python demo_classification.py
```

Access at: `http://localhost:7860`

---

### 2. Regression Demo (`demo_regression.py`)
**California Housing Price Predictor**

An interactive interface for predicting house prices in California.

**Features:**
- 8 input parameters (income, location, house age, etc.)
- Price prediction with confidence intervals
- Market analysis and investment insights
- Sample locations for testing
- Interactive sliders with helpful descriptions

**To Run:**
```bash
cd gradio_demos
python demo_regression.py
```

Access at: `http://localhost:7861`

---

## 🚀 Quick Start

### Prerequisites
```bash
pip install gradio
pip install pycaret[full]
```

### Running Both Demos

**Option 1: Run Individually**
```bash
# Terminal 1
python demo_classification.py

# Terminal 2
python demo_regression.py
```

**Option 2: Run in Background**
```bash
# Windows
start python demo_classification.py
start python demo_regression.py

# Linux/Mac
python demo_classification.py &
python demo_regression.py &
```

---

## 📊 Demo Screenshots

### Classification Demo
```
┌─────────────────────────────────────────┐
│  Heart Disease Prediction System        │
├─────────────────────────────────────────┤
│  Patient Demographics                   │
│  Age: [========50========] 50 years     │
│  Sex: ○ Female ● Male                   │
│                                         │
│  Chest Pain Type: [===0===] 0-3        │
│  Blood Pressure: [===120===] mm Hg     │
│  ...                                    │
│                                         │
│  [🔍 Predict Heart Disease]            │
│                                         │
│  Results:                               │
│  🟢 No Heart Disease                    │
│  Confidence: 87.5%                      │
└─────────────────────────────────────────┘
```

### Regression Demo
```
┌─────────────────────────────────────────┐
│  California Housing Price Predictor     │
├─────────────────────────────────────────┤
│  Median Income: [===3.5===] $35,000    │
│  House Age: [===25===] 25 years        │
│  Location:                              │
│    Latitude: [===37.5===]              │
│    Longitude: [===-122===]             │
│  ...                                    │
│                                         │
│  [💵 Predict House Price]              │
│                                         │
│  Results:                               │
│  Predicted Price: $275,000              │
│  Category: 🏡 Mid-Range                │
└─────────────────────────────────────────┘
```

---

## 🎯 Features

### Both Demos Include:
- ✅ Clean, modern UI with Gradio Soft theme
- ✅ Real-time predictions
- ✅ Input validation
- ✅ Helpful tooltips and descriptions
- ✅ Error handling
- ✅ Demo mode (works without trained models)
- ✅ Responsive design
- ✅ Professional styling

### Classification Demo Specific:
- Risk level categorization
- Medical recommendations
- Confidence scoring
- Color-coded results

### Regression Demo Specific:
- Price range estimation
- Market analysis
- Investment insights
- Sample location suggestions
- Price categorization

---

## 🔧 Configuration

### Change Port Numbers

**Classification Demo:**
```python
# In demo_classification.py, line ~200
demo.launch(server_port=7860)  # Change to desired port
```

**Regression Demo:**
```python
# In demo_regression.py, line ~200
demo.launch(server_port=7861)  # Change to desired port
```

### Enable Public Sharing

To create a public link:
```python
demo.launch(share=True)  # Creates a public gradio.live link
```

### Custom Theme

Change the theme:
```python
with gr.Blocks(theme=gr.themes.Base()) as demo:  # or Monochrome, Glass, etc.
```

---

## 📝 Model Requirements

### For Full Functionality:

1. **Train the models** using the notebooks:
   - `01_binary_classification.ipynb` → saves `heart_disease_model.pkl`
   - `03_regression.ipynb` → saves `california_housing_model.pkl`

2. **Place models** in the correct location:
   ```
   pycaret_assignment/
   ├── models/
   │   ├── heart_disease_model.pkl
   │   └── california_housing_model.pkl
   └── gradio_demos/
       ├── demo_classification.py
       └── demo_regression.py
   ```

3. **Update paths** if needed:
   ```python
   MODEL_PATH = '../models/heart_disease_model'  # Adjust as needed
   ```

### Demo Mode:

Both demos work without trained models using simplified prediction logic for demonstration purposes.

---

## 🎥 Video Tutorial Integration

### Recording the Demos:

1. **Start the demo:**
   ```bash
   python demo_classification.py
   ```

2. **Open in browser:**
   - Navigate to `http://localhost:7860`

3. **Record demonstration:**
   - Show the interface
   - Input sample data
   - Generate predictions
   - Explain the results

4. **Repeat for regression demo**

### Suggested Script:

**Classification Demo (1 minute):**
```
"This is the heart disease prediction demo built with Gradio.
I'll input patient data - age 55, male, with chest pain type 2...
[Input data]
Click predict... and we get a prediction with 85% confidence.
The model identifies this as moderate risk and recommends 
consulting a healthcare professional."
```

**Regression Demo (1 minute):**
```
"This is the housing price predictor for California.
I'll set median income to $50,000, house age 20 years,
location in San Francisco area...
[Input data]
The model predicts a price of $425,000 with a confidence range.
It categorizes this as a premium property in a desirable location."
```

---

## 🐛 Troubleshooting

### Issue: Port Already in Use
```bash
# Find process using port
netstat -ano | findstr :7860  # Windows
lsof -i :7860  # Linux/Mac

# Kill process or change port in code
```

### Issue: Model Not Found
```
Error: Model file not found
```
**Solution:** Train the model first or run in demo mode.

### Issue: Import Error
```
ModuleNotFoundError: No module named 'gradio'
```
**Solution:**
```bash
pip install gradio
```

### Issue: PyCaret Version Mismatch
```
Error loading model: version mismatch
```
**Solution:** Ensure same PyCaret version for training and inference:
```bash
pip install pycaret==3.1.0
```

---

## 🌐 Deployment Options

### Option 1: Hugging Face Spaces
1. Create account on [huggingface.co](https://huggingface.co)
2. Create new Space with Gradio SDK
3. Upload demo files and models
4. Auto-deploys with public URL

### Option 2: Gradio Share
```python
demo.launch(share=True)  # Creates temporary public link
```

### Option 3: Local Network
```python
demo.launch(server_name="0.0.0.0")  # Accessible on local network
```

### Option 4: Docker
```dockerfile
FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "demo_classification.py"]
```

---

## 📚 Additional Resources

- [Gradio Documentation](https://gradio.app/docs/)
- [PyCaret Documentation](https://pycaret.gitbook.io/docs/)
- [Gradio Themes](https://gradio.app/theming-guide/)
- [Deployment Guide](https://gradio.app/sharing-your-app/)

---

## ✅ Checklist for Assignment

- [ ] Both demos run successfully
- [ ] Models are loaded correctly
- [ ] UI is responsive and user-friendly
- [ ] Predictions are accurate
- [ ] Demos are recorded in video tutorial
- [ ] Screenshots/recordings included in submission
- [ ] Code is well-commented
- [ ] Error handling works properly

---

## 📧 Support

If you encounter issues:
1. Check the troubleshooting section
2. Verify model paths
3. Ensure all dependencies are installed
4. Check Python version (3.8+)

---

**Created for PyCaret Assignment**
**Last Updated:** November 2024
