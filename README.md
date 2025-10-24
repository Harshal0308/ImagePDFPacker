# 🧩 ImagePDFPacker

This project provides a Python script to efficiently pack multiple images into a single PDF document, optimizing for space and preserving image aspect ratios. It supports `.png`, `.jpg`, and `.jpeg` image formats.

## ✨ Features

- **Multi-format Support:** Processes PNG, JPG, and JPEG images.
- **Aspect Ratio Preservation:** Images are scaled down to fit within PDF pages while maintaining their original aspect ratio.
- **Space Optimization:** Utilizes a bin-packing algorithm to minimize wasted space on each PDF page.
- **Configurable Page Size:** Supports standard PDF page sizes like A4 and Letter.
- **Error Handling:** Gracefully handles unreadable or corrupted image files.

## ⚙️ Setup

To get started with the project, follow these steps:

### 1️⃣ Clone the Repository
```bash
git clone <repository_url>
cd ImagePDFPacker
```
(Replace `<repository_url>` with the actual URL of your repository.)

### 2️⃣ Create a Virtual Environment (Recommended)
```bash
py -m venv venv
```

### 3️⃣ Activate the Virtual Environment

**Windows:**
```bash
.env\Scriptsctivate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies
```bash
py -m pip install -r requirements.txt
```

## 🧪 Usage

### 1. Prepare Your Images

You have two options for providing images:

- **Use your own images:** Place your `.png`, `.jpg`, or `.jpeg` image files into a dedicated folder (e.g., `my_images/`).  
- **Generate sample images:** If you don't have images ready, you can generate a set of random sample images:
  ```bash
  py sample_data_generation.py
  ```
  This will create an `input_images/` folder containing 10 randomly generated PNG images.

### 2. Generate the PDF

Run the `task_1_starter_code.py` script with the desired input folder and output file name.

```bash
py task_1_starter_code.py --input <your_image_folder> --output <output_filename>.pdf [--page-size <size>]
```

**Arguments:**

- `--input <your_image_folder>`: **Required.** The path to the folder containing your images (e.g., `input_images`, `my_images`, `College`).  
- `--output <output_filename>.pdf`: **Required.** The name of the PDF file to be generated (e.g., `my_document.pdf`).  
- `--page-size <size>`: **Optional.** The desired page size for the PDF. Choose from `A4` (default) or `Letter`.

## 💡 Examples

- **Using generated sample images:**
  ```bash
  py task_1_starter_code.py --input input_images --output sample_output.pdf
  ```

- **Using your own images in a folder named `my_photos`:**
  ```bash
  py task_1_starter_code.py --input my_photos --output family_album.pdf --page-size Letter
  ```

- **Using the `College` images (as tested during development):**
  ```bash
  py task_1_starter_code.py --input College --output College_document.pdf
  ```

The script will print statistics about the packing process, including the number of images packed, pages used, and wasted space.

## 📦 Dependencies

The project relies on the following Python libraries, listed in `requirements.txt`:

- `Pillow`: For image processing (opening, resizing, cropping).  
- `reportlab`: For PDF generation.  
- `numpy`: A dependency for `rectpack`.  
- `rectpack`: For the 2D bin-packing algorithm.
