# 📂 EUDR GIS Auditor

<image src="./EudrGisAuditor.png"><image>

The **EUDR GIS Auditor** is a web-based tool designed to **validate, audit, and clean geospatial data**, specifically tailored to the requirements of the **European Union Deforestation Regulation (EUDR)**. It processes common GIS file formats, identifies and fixes errors, and provides an **interactive dashboard and map** for thorough review.

---

## 🛠️ Setup & Installation

The simplest way to run this application is with **Docker** and **Docker Compose**, which handle all dependencies automatically.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/julio-collazos/EudrGisAuditor.git
   cd EudrGisAuditor
   ```

2. **Start the application (using a Python environment):**
   
   **Step 1:** Create and Activate the Conda Environment:
   
   Create a new environment with Python 3.10:

   ```bash
   conda create -n eudrgisauditor python=3.10 -y
   conda activate eudrgisauditor
   ```
   **Step 2:** Install Dependencies

   Install GDAL via Conda, then install the remaining packages from requirements.txt:
   ```bash
   conda install -c conda-forge gdal=3.6.2 -y
   pip install -r requirements.txt
   ```
   **Step 3:** Launch the Application


   Run the main script:
   ```bash
   python start.py
   ```

   Once launched, you're ready to explore the tool!

3. **Access the app:**
   Open your browser and navigate to 👉 [http://localhost:5000](http://localhost:5000)

---

## 🚀 Features

* **Geospatial Auditing** → Checks for geometry issues (e.g., self-intersections) and validates against standards like **WGS84**.
* **Automatic Fixes** → Corrects minor geometry errors to save you time.
* **Data Partitioning** → Classifies features as **valid**, **needs review**, or **conversion candidates** (e.g., small polygons → points).
* **Interactive Visualization** → Audit findings are displayed in a **dashboard** and on a **Leaflet-based map**, making flagged entities easy to inspect.

---

## ➡️ Roadmap / Next Steps

* 🔑 **User Authentication** → Add login system for managing sessions and data access.
* 📂 **Support Additional Formats** → Expand compatibility with more GIS formats.
* 🗄️ **Database Integration** → Store and manage audit results for long-term tracking.
* 🐳 **Production-Ready Docker** → Stabilize the container for reliable deployment in production environments (currently experimental).
---


 ```bash
 podman compose -f .\docker-compose.yml up
 ```
