# 🌿 Plant Leaf Health Detection – Learning & Development Roadmap

This project roadmap outlines a 12+ week guided learning path to build a **Plant Disease Detection System** using **Python**, **OpenCV**, and **Deep Learning**. The goal is to detect whether a leaf is **healthy**, **infected**, or **dead** from an image input.

---

## 🗓️ Weekly Roadmap Overview

### ⚙️ Phase 1: Python & Image Handling (Weeks 1–3)

#### Week 1: Python Essentials

- ✅ Learn variables, control flow, functions
- ✅ Practice lists, dictionaries
- ✅ File I/O basics – read/write image files

#### Week 2: Object-Oriented Programming + Libraries

- ✅ Learn classes, objects, and modules
- ✅ Learn to use `pip` and install:
  - OpenCV (`opencv-python`)
  - NumPy (`numpy`)

#### Week 3: OpenCV Basics

- ✅ Load, display, and resize images
- ✅ Convert between RGB, Grayscale, HSV
- ✅ Apply basic filters: blur, edge detection

🎯 **Mini-project**: Edge or color pattern detection on leaf images

---

### 📷 Phase 2: Image Processing & Disease Indicators (Weeks 4–5)

#### Week 4: Preprocessing & Segmentation

- ✅ Perform color segmentation in HSV
- ✅ Detect contours to isolate leaf region

#### Week 5: Feature Extraction

- ✅ Extract shape, texture, color features
- ⭕ (Optional) Calculate disease severity (e.g., spot area ratio)

🎯 **Mini-project**: Segment leaf and highlight suspect diseased patches

---

### 🤖 Phase 3: Machine Learning Model (Weeks 6–8)

#### Week 6: Intro to CNNs & Keras/TensorFlow

- ✅ Understand layers, activations, loss, optimizers
- ✅ Install TensorFlow/Keras

#### Week 7: Dataset Preparation

- ✅ Download datasets (e.g., [PlantVillage](https://www.kaggle.com/datasets/emmarex/plantdisease))
- ✅ Organize train/test/validation folders
- ✅ Use `ImageDataGenerator` for preprocessing

#### Week 8: Model Training & Evaluation

- ✅ Build and train CNN (5–10 epochs)
- ✅ Aim for accuracy ~90%+
- ✅ Save model (`.h5` format)

🎯 **Mini-project**: Train a model to classify Healthy vs Infected vs Dead leaves

---

### 🌐 Phase 4: App Integration (Weeks 9–11)

#### Week 9: Choose a Framework

- ✅ Use **Streamlit** for faster UI
- ⭕ (Optional) Learn Flask or FastAPI for REST API

#### Week 10: Upload → Inference Pipeline

- ✅ Build front-end image uploader
- ✅ Preprocess and pass image to model
- ✅ Return predicted class

#### Week 11: UI Polish & Testing

- ✅ Display uploaded leaf and predicted label
- ✅ Show confidence scores
- ✅ Add minimal UI styling

---

### 🚀 Phase 5: Deployment & Enhancement (Week 12+)

- ⭕ Deploy to **Render**, **Heroku**, or **Hugging Face Spaces**
- ⭕ Add mobile image upload support
- ⭕ Train model for more plant types
- ⭕ Improve model with:
  - Data augmentation
  - Transfer learning (e.g., MobileNetV2)
  - Image segmentation for better accuracy

---

## ⏱️ Weekly Study Session Format (1-Hour / Day)

| Time   | Task                                   |
| ------ | -------------------------------------- |
| 10 min | Read docs or watch a short tutorial    |
| 20 min | Code & experiment with examples        |
| 20 min | Build a small part of the mini-project |
| 10 min | Log progress and save work             |

---

## 🧠 Progress Log Template (Daily)

```text
📅 Date: YYYY-MM-DD
📍 Topic: [e.g., HSV Segmentation]
✅ What I did:
- Watched a video on HSV color thresholding
- Applied OpenCV's `cv2.inRange()` on a test leaf

🤔 What I learned:
- HSV makes color filtering easier than RGB
- Hue = color, Saturation = vibrance, Value = brightness

📌 What's next:
- Try contour detection on segmented leaves
```
