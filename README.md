# Automatic File Sorter

This Python script automatically sorts files in a specified directory based on their file types. It organizes files into folders such as CSV, PDF, Word documents, images, videos, presentations, and AWS key pairs, making your downloads or any other specified directory neat and organized.

## Features

- Automatically organizes files into designated folders based on file type.
- Supports the following file types:
  - CSV files (`.csv`)
  - PDF files (`.pdf`)
  - Word documents (`.docx`)
  - Images (`.png`, `.jpg`, `.jpeg`)
  - Videos (`.mp4`)
  - Presentations (`.pptx`)
  - AWS key pairs (`.pem`)
- Easily customizable to support additional file types and folders.

## Prerequisites

Make sure you have Python installed on your system. This script works with Python 3.x.

## Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/khushi-rathore/Automatic-File-Sorter.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd automatic-file-sorter
    ```

3. **Run the script**:
    - Update the `path` variable in `file_sorter.py` to the directory you want to organize (e.g., `Path`).
    - Run the script using the command:
    ```bash
    python file_sorter.py
    ```

## How It Works

The script scans the specified directory for files and moves them into appropriate subfolders based on their file extensions. If the subfolders do not exist, they are created automatically.

## Folder Structure

The script will create the following folders if they don't already exist:

- `CSV Folder`
- `PDF Folder`
- `Word Folder`
- `Image Folder`
- `Video Folder`
- `PPT Folder`
- `AWS Key pairs`

## Supported File Types

You can customize the script to support additional file types or modify the folder names as needed. Below are the default file extensions handled by the script:

| File Type     | Extensions                    |
|---------------|-------------------------------|
| CSV           | `.csv`                        |
| PDF           | `.pdf`                        |
| Word Documents| `.docx`                       |
| Images        | `.png`, `.jpg`, `.jpeg`       |
| Videos        | `.mp4`                        |
| Presentations | `.pptx`                       |
| AWS Key Pairs | `.pem`                        |

## Customization

To add support for more file types or change the folder structure:

1. Update the `folder_names` list with the new folder.
2. Add a new condition in the `for` loop to check for the desired file extension and move the file to the appropriate folder.
