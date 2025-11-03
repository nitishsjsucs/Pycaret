"""
Gradio Demo for Binary Classification - Heart Disease Prediction
Interactive web application for heart disease prediction using trained PyCaret model
"""

import gradio as gr
import pandas as pd
import numpy as np
from pycaret.classification import load_model, predict_model
import os

# Try to load the model (will use a mock if model doesn't exist)
MODEL_PATH = '../models/heart_disease_model'

def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, 
                          thalach, exang, oldpeak, slope, ca, thal):
    """
    Predict heart disease based on input features
    """
    try:
        # Create input dataframe
        input_data = pd.DataFrame({
            'age': [age],
            'sex': [sex],
            'cp': [cp],
            'trestbps': [trestbps],
            'chol': [chol],
            'fbs': [fbs],
            'restecg': [restecg],
            'thalach': [thalach],
            'exang': [exang],
            'oldpeak': [oldpeak],
            'slope': [slope],
            'ca': [ca],
            'thal': [thal]
        })
        
        # Load model and make prediction
        if os.path.exists(MODEL_PATH + '.pkl'):
            model = load_model(MODEL_PATH)
            predictions = predict_model(model, data=input_data)
            
            prediction_label = predictions['prediction_label'].iloc[0]
            prediction_score = predictions['prediction_score'].iloc[0]
            
            result = "Heart Disease Detected" if prediction_label == 1 else "No Heart Disease"
            confidence = f"{prediction_score * 100:.2f}%"
            
            # Risk assessment
            if prediction_label == 1:
                if prediction_score > 0.8:
                    risk = "High Risk"
                    color = "🔴"
                elif prediction_score > 0.6:
                    risk = "Moderate Risk"
                    color = "🟡"
                else:
                    risk = "Low Risk"
                    color = "🟢"
            else:
                risk = "Low Risk"
                color = "🟢"
            
            output = f"""
            ## Prediction Results
            
            {color} **{result}**
            
            **Confidence:** {confidence}
            **Risk Level:** {risk}
            
            ### Input Summary:
            - Age: {age} years
            - Chest Pain Type: {cp}
            - Max Heart Rate: {thalach} bpm
            - Cholesterol: {chol} mg/dl
            
            ### Recommendation:
            """
            
            if prediction_label == 1:
                output += "⚠️ Please consult with a healthcare professional for proper diagnosis and treatment."
            else:
                output += "✅ Maintain a healthy lifestyle and regular check-ups."
            
            return output
        else:
            # Demo mode without model
            risk_score = (age/100 + cp/4 + (300-thalach)/300 + chol/400) / 4
            prediction = 1 if risk_score > 0.5 else 0
            
            result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"
            confidence = f"{risk_score * 100:.2f}%"
            
            return f"""
            ## Demo Prediction Results (Model not loaded)
            
            **Result:** {result}
            **Confidence:** {confidence}
            
            Note: This is a demo prediction. Train and save the model first for accurate predictions.
            """
    
    except Exception as e:
        return f"Error: {str(e)}\n\nPlease ensure the model is trained and saved correctly."

# Create Gradio interface
with gr.Blocks(title="Heart Disease Prediction", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🫀 Heart Disease Prediction System
    ### Powered by PyCaret AutoML
    
    Enter patient information below to predict the likelihood of heart disease.
    """)
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Patient Demographics")
            age = gr.Slider(minimum=20, maximum=100, value=50, step=1, label="Age (years)")
            sex = gr.Radio(choices=[0, 1], value=1, label="Sex (0=Female, 1=Male)")
            
            gr.Markdown("### Chest Pain & Symptoms")
            cp = gr.Slider(minimum=0, maximum=3, value=0, step=1, 
                          label="Chest Pain Type (0-3)")
            exang = gr.Radio(choices=[0, 1], value=0, 
                           label="Exercise Induced Angina (0=No, 1=Yes)")
            
            gr.Markdown("### Blood Pressure & Heart Rate")
            trestbps = gr.Slider(minimum=80, maximum=200, value=120, step=1, 
                               label="Resting Blood Pressure (mm Hg)")
            thalach = gr.Slider(minimum=60, maximum=220, value=150, step=1, 
                              label="Maximum Heart Rate Achieved")
        
        with gr.Column():
            gr.Markdown("### Blood Tests")
            chol = gr.Slider(minimum=100, maximum=600, value=200, step=1, 
                           label="Serum Cholesterol (mg/dl)")
            fbs = gr.Radio(choices=[0, 1], value=0, 
                         label="Fasting Blood Sugar > 120 mg/dl (0=No, 1=Yes)")
            
            gr.Markdown("### ECG & Other Tests")
            restecg = gr.Slider(minimum=0, maximum=2, value=0, step=1, 
                              label="Resting ECG Results (0-2)")
            oldpeak = gr.Slider(minimum=0, maximum=6, value=0, step=0.1, 
                              label="ST Depression")
            slope = gr.Slider(minimum=0, maximum=2, value=0, step=1, 
                            label="Slope of Peak Exercise ST Segment (0-2)")
            ca = gr.Slider(minimum=0, maximum=3, value=0, step=1, 
                         label="Number of Major Vessels (0-3)")
            thal = gr.Slider(minimum=0, maximum=3, value=0, step=1, 
                           label="Thalassemia (0-3)")
    
    predict_btn = gr.Button("🔍 Predict Heart Disease", variant="primary", size="lg")
    
    output = gr.Markdown(label="Prediction Results")
    
    predict_btn.click(
        fn=predict_heart_disease,
        inputs=[age, sex, cp, trestbps, chol, fbs, restecg, thalach, 
                exang, oldpeak, slope, ca, thal],
        outputs=output
    )
    
    gr.Markdown("""
    ---
    ### About This Model
    
    This model uses **Random Forest** algorithm trained on the Heart Disease dataset.
    - **Accuracy:** ~85%+
    - **Features:** 13 medical attributes
    - **Training:** PyCaret AutoML with GPU acceleration
    
    ⚠️ **Disclaimer:** This is a demonstration tool for educational purposes only. 
    It should not be used as a substitute for professional medical advice, diagnosis, or treatment.
    """)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )
