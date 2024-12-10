# CNN Image Classifier with Pretrained Models

This project implements an image classifier using three popular Convolutional Neural Network (CNN) architectures: **ResNet-18**, **AlexNet**, and **VGG16**. The models are pretrained on the ImageNet dataset and can classify images into one of 1,000 ImageNet classes. Users can run the classifier locally, choose their preferred CNN architecture, and evaluate the model's predictions.

## Table of Contents

- [Overview](#overview)
- [Pretrained Models](#pretrained-models)
- [Project Features](#project-features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Future Improvements](#future-improvements)

---

## Overview

The goal of this project is to leverage pretrained CNN models to classify images effectively. The three models — ResNet-18, AlexNet, and VGG16 — are known for their outstanding performance in image recognition tasks. The project supports:

- Loading an image from the local system.
- Preprocessing the image to make it compatible with the CNN model.
- Generating predictions using the selected CNN architecture.

## Pretrained Models

### 1. **ResNet-18**
   - ResNet-18 introduces residual connections that mitigate the vanishing gradient problem in deep networks.
   - It's a lightweight and efficient model for image classification tasks.

### 2. **AlexNet**
   - AlexNet was one of the first models to demonstrate the power of CNNs on the ImageNet challenge.
   - It uses ReLU activations and dropout layers to reduce overfitting.

### 3. **VGG16**
   - VGG16 is known for its simplicity and uniform architecture.
   - It uses smaller convolution filters and more layers for better feature extraction.

![Result by AlexNet](https://github.com/user-attachments/assets/65a38adc-8416-4d36-8729-9d3a7282a450)
![Result by VGG](https://github.com/user-attachments/assets/29debda9-3d46-4d85-9431-642b286e5cc7)


## Project Features

- Classification using three CNN architectures.
- Easy selection of the desired model.
- Preprocessing pipeline for resizing, cropping, and normalizing input images.
- ImageNet class labels for detailed predictions.

---

## Setup and Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.7 or higher
- PyTorch and torchvision
- Other required libraries listed in `requirements.txt`

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cnn-image-classifier.git
   cd cnn-image-classifier
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the ImageNet class labels file:
   - Save the file `imagenet1000_clsid_to_human.txt` in the project directory. It maps class indices to human-readable labels.

---

## Usage

1. **Run the Classifier**
   ```bash
   python classifier.py --img_path <path_to_image> --model_name <model>
   ```
   - Replace `<path_to_image>` with the path to your input image.
   - Replace `<model>` with one of the following options:
     - `resnet`
     - `alexnet`
     - `vgg`

   Example:
   ```bash
   python classifier.py --img_path ./test_image.jpg --model_name resnet
   ```

2. **Expected Output**
   - The program will print the top predicted class label for the input image.

---

## How It Works

1. **Input Image**: 
   - Load the image using Python's `Pillow` library.

2. **Preprocessing**:
   - Resize the image to 256x256.
   - Center crop to 224x224.
   - Normalize pixel values using ImageNet's mean and standard deviation.

3. **Model Inference**:
   - The selected CNN model (ResNet-18, AlexNet, or VGG16) processes the image.
   - The model outputs probabilities for 1,000 ImageNet classes.

4. **Class Label Mapping**:
   - The output class index is mapped to a human-readable label using the ImageNet class labels file.

---

## Future Improvements

- Add support for batch image classification.
- Implement top-5 predictions display.
- Include additional CNN architectures like DenseNet or MobileNet.
- Provide a web interface for easier interaction.

---

## License

This project is licensed under the [GPL-3.0 license](LICENSE).

Feel free to contribute or raise issues in the repository. Happy coding!

--- 
