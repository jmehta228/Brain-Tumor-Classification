# 🧠 Brain Tumor Classification

This project classifies brain tumors using MRI images and the machine learning algorithms: **K-Nearest Neighbors (K-NN), Decision Trees, Random Forest, and CNN**. It involves preprocessing image data, training models, and evaluating performance using accuracy, precision, recall, and F1-score.

---

## 📁 Dataset

- **Source**: [Kaggle - Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)
- **Classes**:
  - Glioma Tumor
  - Meningioma Tumor
  - Pituitary Tumor
  - No Tumor

---

## ⚙️ Workflow

1. **Preprocessing**:
   - Resize images to `256x256` using OpenCV
   - Flatten and label images

2. **Model Training**:
   - k-NN: Tested with `k = 3, 5, 7, 9, 11`
   - Decision Tree: Used `max_depth` variations

3. **Evaluation**:
   - Confusion matrix per class (one-vs-all)
   - Metrics: Accuracy, Precision, Recall, F1-Score
   - Visualized using Seaborn heatmaps
