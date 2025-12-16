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
```

## ⚙️ Configuring Fusion Algorithm (F2A) Settings

To modify the fusion algorithm parameters, edit the `load_model()` function in `SwinFusion_App/app.py` (around lines 121-123):

```python
model = net(upscale=1, in_chans=1, img_size=128, window_size=8,
            img_range=1., depths=[6, 6, 6, 6], embed_dim=60, num_heads=[6, 6, 6, 6],
            mlp_ratio=2, upsampler=None, resi_connection='1conv')
```

### Key Parameters:
*   **`upscale`**: Upscale factor (1 for fusion, 2/4/8 for super-resolution)
*   **`in_chans`**: Input channels (1 for grayscale, 3 for RGB)
*   **`img_size`**: Input image size for model (default: 128)
*   **`window_size`**: Window size for Swin Transformer attention (default: 8)
*   **`img_range`**: Image value range (1.0 for normalized [0,1])
*   **`depths`**: Number of transformer blocks per stage (e.g., [6, 6, 6, 6])
*   **`embed_dim`**: Embedding dimension (default: 60)
*   **`num_heads`**: Number of attention heads per stage (e.g., [6, 6, 6, 6])
*   **`mlp_ratio`**: MLP expansion ratio (default: 2)
*   **`upsampler`**: Upsampling method (None for fusion, 'pixelshuffle' for SR)
*   **`resi_connection`**: Residual connection type ('1conv' recommended)

**Note**: After modifying these settings, restart the Streamlit app for changes to take effect.

## ℹ️ Disclaimer
This application is for research and demonstration purposes. The quality metrics shown in the dashboard are currently simulated for UI demonstration purposes as Ground Truth data is rarely available in real-world clinical inference scenarios.

## 🔗 Credits
Based on the **SwinFusion** architecture.
*Original Paper*: [SwinFusion: Cross-domain Long-range Learning for General Image Fusion via Swin Transformer]

## 👥 Contributors
*   **[pieby2](https://github.com/pieby2)**
