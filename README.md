Image to Text Recognition Model

This project is a simple Image to Text Recognition model designed to extract text from images. It is built on top of the Ollama platform and leverages the LLaVA image recognition models for efficient processing.
PrerequisitesBefore running the project, you need to install Ollama. Ollama is a platform that allows you to easily use large language models and vision models. Follow these steps:

    Install Ollama:
    To install Ollama, run the following command in your terminal:

curl -sSL https://ollama.com/install | bash

Download the LLaVA Model:
Once Ollama is installed, you can pull the LLaVA model by running:

    ollama pull llava

    LLaVA is a vision language model designed for image-to-text tasks. There are three versions of the model available based on the available VRAM of your graphics card:
        LLaVA 7B (low VRAM usage)
        LLaVA 13B (medium VRAM usage)
        LLaVA 38B (high VRAM usage)

    Choose the model according to your system’s VRAM.

Usage

    Configure the Model in the app.py Script:
    In the app.py script, locate the process_image function. Inside this function, set the model name to match the one you are using. For example, if you're using the LLaVA 13B model, change the line as follows:

model= "llava-13b"

Ensure that you select the correct model name that corresponds to your GPU's VRAM.

Run the Script:
After setting up the model, you can start processing images using the following command:

    python app.py

    The script will prompt you to provide the path to the image, and it will return the extracted text.

System Requirements

    Operating System: Linux

    Hardware: A compatible GPU with sufficient VRAM for running the LLaVA model.
        LLaVA 7B: Requires at least 4GB VRAM.
        LLaVA 13B: Requires at least 16GB VRAM.
        LLaVA 38B: Requires at least 24GB VRAM.

Notes

    This project is designed to run on Linux systems.
    Make sure your system has the necessary dependencies to run Ollama and the models.
    In this project llava 7B model is use.
