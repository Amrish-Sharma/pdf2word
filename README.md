# 📄 PDF2Word - Convert PDF to Word Online

**PDF2Word** is a lightweight web application built using **Flask** that allows users to upload a PDF file and download its converted Word document (`.docx`) format. It features a sleek drag-and-drop interface powered by **Dropzone.js**.

---

### ✨ Features

- 📥 Drag-and-drop PDF upload
- 🔄 Automatic conversion to `.docx`
- 📤 Download ready in seconds
- 📁 Temporary storage of uploaded and converted files
- 🧼 Clean and simple UI

---

### 🚀 Getting Started

#### 1. Clone the repository

```bash
git clone https://github.com/Amrish-Sharma/pdf2word.git
cd pdf2word
```

#### 2. Set up a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### ▶️ Run the App

```bash
python app.py
```

Visit the app at: [http://localhost:5000](http://localhost:5000)

---

### 📁 Project Structure

```
pdf2word/
├── app.py               # Main Flask application
├── templates/
│   └── index.html       # UI for upload
├── static/
│   └── js/css           # CSS/JS for Dropzone
├── uploads/             # Uploaded PDFs (.gitkeep included)
├── converted/           # Converted Word files (.gitkeep included)
├── requirements.txt     # Python package requirements
└── .gitignore           # Ignore uploaded/converted files but keep folders
```

---

### 🧪 Tech Stack

- Python 3.7+
- Flask
- pdf2docx
- Dropzone.js
- HTML5, CSS3

---

### 🐳 Docker Setup

You can easily run this app using Docker. Here’s how:

#### 1. Build the Docker image

```bash
docker build -t pdf2word .
```

#### 2. Run the Docker container

```bash
docker run -d -p 5000:5000 --name pdf2word-app pdf2word
```

This will run the app on [http://localhost:5000](http://localhost:5000).

---

### 📦 Deployment

This app can be deployed easily using:
- Gunicorn + Nginx
- Render
- Railway
- Docker (using the `Dockerfile` above)

---

### 🙏 Credits

- [Flask](https://flask.palletsprojects.com/)
- [pdf2docx](https://pypi.org/project/pdf2docx/)
- [Dropzone.js](https://www.dropzone.dev/)

---

### 📜 License

This project is licensed under the MIT License.  
Feel free to fork and contribute!

---

### 👤 Author

**Amrish Sharma**  
GitHub: [@Amrish-Sharma](https://github.com/Amrish-Sharma)
```

---

This update includes Docker instructions so you can easily build and run your app in a container. Let me know if you'd like to further enhance the `README`, or if you'd prefer me to include deployment instructions for cloud platforms like Heroku or AWS!