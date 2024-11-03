# OCR Application

This OCR (Optical Character Recognition) application is designed to process PDF files by converting them into images, extracting text using OCR, classifying pages, and extracting key-value pairs and tables from each page. The results are then post-processed and saved for further use.

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Modules](#modules)
6. [Function Overview](#function-overview)
7. [License](#license)

## Features

- Converts PDF files to images for OCR processing.
- Classifies pages based on content.
- Extracts key-value pairs and tables from images.
- Saves the extracted information into JSON files for further processing.
- Allows for modular post-processing of classified data.

## Requirements

Ensure the following packages are installed:

- `pdf_reader`
- `argparse`
- `ocr_extraction`
- `page_classification`
- `key_value_extraction`
- `table_extraction`
- `post_processing`

You may also need other dependencies such as `paddleOCR` for OCR and image handling.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/dilukshashamal/Intelligine_Doc_Reader.git
    cd Intelligine_Doc_Reader
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the application, execute the following command:

```bash
python main.py <pdf_path>
