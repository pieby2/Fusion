# 🧠 SwinFusion Medical Image Fusion App

A Streamlit-based web application for fusing **CT (Computed Tomography)** and **MRI (Magnetic Resonance Imaging)** scans using the **SwinFusion** deep learning model.

This app features a modern, dark-themed dashboard interface for visualizing medical image fusion results and quality metrics.

## 🌐 Live Demo
👉 **[Try the Live App Here](https://imagefused.streamlit.app/)**

## ✨ Features

*   **Deep Learning Fusion**: Uses a pre-trained Swin Transformer-based model for high-quality image fusion.
*   **Interactive Dashboard**: 3-column layout for Input, Processing, and Metrics.
*   **Privacy-First**: Images are processed in memory and not saved to the server's disk.
*   **Visual Metrics**: Displays PSNR, SSIM, and other quality indicators (Demo Mode).
*   **Dark Mode UI**: Custom-styled for a professional clinical look.

## 🛠️ Installation

### Prerequisites
*   **Python 3.10** (Recommended)
    *   *Note: Python 3.14 (Preview) causes known DLL errors with PyTorch on Windows. Please use Python 3.9 - 3.11.*
*   CUDA-capable GPU (Optional, defaults to CPU if unavailable).

### Setup
1.  Clone the repository:
    ```bash
    git clone https://github.com/pieby2/SWIN_fusion.git
    cd SWIN_fusion/SwinFusion_App
    ```

2.  Install dependencies:
    ```bash
    # Using specific python version (if you have multiple)
    py -3.10 -m pip install -r requirements.txt
    
    # Or standard pip
    pip install -r requirements.txt
    ```

## 🚀 Usage

Run the Streamlit application from the `SwinFusion_App` directory:

```bash
# Recommended for Windows users with multiple Python versions
py -3.10 -m streamlit run app.py

# Standard launch
streamlit run app.py
```

Open your browser to `http://localhost:8501` (or the port shown in the terminal).

## 📂 Project Structure

```
SwinFusion_App/
├── app.py                  # Main Streamlit application entry point
├── requirements.txt        # Python dependencies
├── model/                  # Pre-trained SwinFusion model weights
├── models/                 # Neural network architecture definitions
└── utils/                  # Image processing utility functions

DSA_Problems/
├── data_structures/        # Data structure implementations (Stack, Queue, Trees, etc.)
├── algorithms/             # Algorithm implementations (Sorting, Searching, Graphs)
└── problems/               # Solutions to popular DSA problems
```

## 📚 DSA Problems

This repository also includes a comprehensive collection of **Data Structures and Algorithms** implementations and problem solutions. Perfect for:
- 🎓 Learning fundamental data structures and algorithms
- 💼 Interview preparation
- 🧩 Practicing algorithmic problem-solving

**Quick Start:**
```bash
cd DSA_Problems
python3 data_structures/linked_list.py  # Run individual example
python3 run_examples.py                 # Run all examples
```

📖 See [DSA_Problems/README.md](DSA_Problems/README.md) for detailed documentation and [INDEX.md](DSA_Problems/INDEX.md) for a complete catalog of all implementations.

## ℹ️ Disclaimer
This application is for research and demonstration purposes. The quality metrics shown in the dashboard are currently simulated for UI demonstration purposes as Ground Truth data is rarely available in real-world clinical inference scenarios.

## 🔗 Credits
Based on the **SwinFusion** architecture.
*Original Paper*: [SwinFusion: Cross-domain Long-range Learning for General Image Fusion via Swin Transformer]

## 👥 Contributors
*   **[pieby2](https://github.com/pieby2)**
