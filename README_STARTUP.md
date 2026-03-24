# ML Chronic Disease Indicator

A machine learning-based web application that predicts the likelihood of chronic diseases including **breast cancer**, **diabetes**, and **heart disease**.

## Quick Start

### Option 1: Click to Run (Easiest)
1. Open File Explorer
2. Navigate to: `ML-Chronic-Disease-Indicator` folder
3. **Double-click** `START.bat`
4. Browser opens automatically with the app!

### Option 2: Run from Terminal
```powershell
cd "c:\Users\madhumitha\OneDrive\Documents\ML Project\ML-Chronic-Disease-Indicator"
py open.py
```

## What Happens

When you run either option:
- ✓ Backend API starts on port **10000**
- ✓ Frontend Server starts on port **5500**
- ✓ Browser opens automatically to the app
- ✓ Terminal shows the URL to use

You'll see in terminal:
```
======================================================================
  LOCAL:   http://127.0.0.1:5500/index.html
======================================================================

  Backend:  http://127.0.0.1:10000
  Frontend: http://127.0.0.1:5500

  Press Ctrl+C to stop all servers
======================================================================
```

## How to Use

1. Open the app in browser (happens automatically)
2. Click on a disease: **Breast Cancer**, **Diabetes**, or **Heart Disease**
3. Enter patient health values
4. Click **Predict** button
5. See the prediction result instantly!

## Sample Test Values

### Breast Cancer Prediction
- Mean Radius: 14
- Mean Texture: 20
- Mean Perimeter: 90
- Mean Area: 600
- Mean Smoothness: 0.09

**Expected Result:** Cancerous

### Diabetes Prediction
- Pregnancies: 2
- Glucose: 120
- Blood Pressure: 70
- Skin Thickness: 20
- Insulin: 80
- BMI: 32
- Diabetes Pedigree Function: 0.5
- Age: 30

**Expected Result:** Non-Diabetic

### Heart Disease Prediction
- Age: 54
- Sex: 1
- Chest Pain Type: 3
- Resting Blood Pressure: 130
- Serum Cholestoral: 250
- Fasting Blood Sugar: 0
- Resting ECG: 1
- Max Heart Rate: 150
- Exercise Angina: 0
- Oldpeak: 1.4
- ST Segment: 2
- Major Vessels: 0
- Thal: 7

**Expected Result:** Heart Disease Detected

## Project Structure

```
ML-Chronic-Disease-Indicator/
├── START.bat                    # Click to run everything
├── open.py                      # Python startup script
├── terminal_test.py             # Test predictions from terminal
├── ml-app/
│   ├── apps.py                  # Flask backend API
│   ├── requirements.txt          # Python dependencies
│   ├── adaboost_breast_cancer.pkl
│   ├── adaboost_diabetes.pkl
│   └── adaboost_heart_disease.pkl
├── frontend/
│   ├── index.html               # Home page
│   ├── breast.html              # Breast cancer predictor
│   ├── diabetes.html            # Diabetes predictor
│   ├── heart.html               # Heart disease predictor
│   └── test.html                # API test page
├── Breast_cancer_data.csv
├── dataset_heart.csv
├── diabetes1.csv
└── README.md
```

## URLs to Use

- **App:** http://127.0.0.1:5500/index.html
- **Backend API:** http://127.0.0.1:10000
- **API Test Page:** http://127.0.0.1:5500/test.html

## Machine Learning Models

| Disease | Accuracy | Model |
|---------|----------|-------|
| Breast Cancer | 95.61% | AdaBoost |
| Diabetes | 83.77% | AdaBoost |
| Heart Disease | 85.19% | AdaBoost |

## Technology Stack

- **Backend:** Flask, Python, Scikit-learn
- **Frontend:** HTML, CSS, JavaScript
- **Models:** AdaBoost (trained and saved as .pkl files)

## Stopping the App

**Option 1:** Close the terminal window(s)

**Option 2:** Press `Ctrl+C` in the terminal

## Troubleshooting

### Browser doesn't open
- Manually open: http://127.0.0.1:5500/index.html
- Or: http://localhost:5500/index.html

### Port already in use
- Close any other Flask/HTTP apps running on ports 10000 or 5500
- Or modify the port in `START.bat` or `open.py`

### scikit-learn version warning
- This is normal - the models were trained on sklearn 1.6.1, you may have 1.7.0
- The predictions still work correctly despite the warning

### Dependencies missing
The first time you run, Python will install dependencies from `ml-app/requirements.txt`:
- Flask
- NumPy
- Scikit-learn
- Flask-CORS

## Alternative Methods

### Test Predictions from Terminal
```powershell
cd "c:\Users\madhumitha\OneDrive\Documents\ML Project\ML-Chronic-Disease-Indicator"
py terminal_test.py
```

This will test all three diseases and show predictions in the terminal.

## Assignment Comparison

**Model Accuracies Range:**
- Decision Tree: ~92%
- Random Forest: ~94%
- Logistic Regression: ~76%
- SVM: ~95%
- KNN: ~91%
- Naive Bayes: ~76%
- **AdaBoost: ~96% ✓ BEST** (selected for deployment)

## License

This is an educational ML project for Chronicle Disease Indication using AdaBoost classifier.

---

**Need Help?**
1. Check both terminal windows are running (no red errors)
2. Make sure you're in the correct folder
3. Try refreshing the browser with Ctrl+Shift+R
4. Close and run START.bat again
