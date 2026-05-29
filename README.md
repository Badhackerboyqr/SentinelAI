# SentinelAI – AI-Powered SOC Analyst & Threat Detection Dashboard

## Project Overview

SentinelAI is an AI-powered Security Operations Center (SOC) platform designed to simulate real-world threat monitoring and incident detection workflows. The project combines Cybersecurity, Machine Learning, and Data Visualization to identify suspicious activities from security logs and present actionable insights through an interactive dashboard.

The platform analyzes network traffic, login activity, and email data to detect potential threats such as port scanning, brute-force attacks, phishing attempts, and anomalous network behavior. Detected incidents are automatically classified, prioritized, and displayed in a SOC-style dashboard to assist security analysts during investigations.

This project was built as a practical demonstration of Blue Team operations, Security Monitoring, Threat Detection Engineering, and Applied Machine Learning in Cybersecurity.

---

## Architecture

```text
                    +-------------------+
                    |   Security Logs   |
                    | Network / Email   |
                    | Authentication    |
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    | Data Ingestion    |
                    | Log Collection    |
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    | Preprocessing     |
                    | Feature Extraction|
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    | AI Detection      |
                    | Isolation Forest  |
                    | Logistic Regression|
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    | Alert Engine      |
                    | Severity Scoring  |
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    | SQLite Database   |
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    | Streamlit SOC     |
                    | Dashboard         |
                    +-------------------+
```

---

## Features

### Threat Detection

* Network anomaly detection using Isolation Forest
* Detection of unusual traffic patterns
* Port scan identification
* Failed login monitoring
* Phishing email classification
* Automated threat scoring

### Alert Management

* Real-time alert generation
* Alert severity classification
* Confidence score calculation
* Threat categorization
* Historical alert tracking

### SOC Dashboard

* Executive security overview
* Alert monitoring panel
* Threat analytics dashboard
* Incident investigation interface
* Threat distribution visualization
* Interactive filtering and search

### Machine Learning

* Unsupervised anomaly detection
* Text classification for phishing detection
* Feature engineering pipeline
* Model evaluation metrics
* False-positive monitoring

### Data Storage

* SQLite-based alert database
* Historical event retention
* Query support for investigations

---

## Tech Stack

### Programming Language

* Python 3.12

### Machine Learning

* Scikit-Learn
* Joblib

### Data Processing

* Pandas
* NumPy

### Dashboard

* Streamlit
* Plotly

### Database

* SQLite
* SQLAlchemy

### Development Tools

* Git
* GitHub
* VS Code

---

## Dataset

### Network Traffic Dataset

The project uses simulated security logs and publicly available network traffic datasets to train anomaly detection models.

Example Features:

* Source IP
* Destination IP
* Source Port
* Destination Port
* Protocol
* Packet Count
* Bytes Sent
* Bytes Received
* Connection Duration

### Phishing Email Dataset

Email samples are processed using Natural Language Processing (NLP) techniques.

Example Features:

* Email Subject
* Sender Domain
* URL Count
* Suspicious Keywords
* Email Body Content

### Synthetic Data Generation

For demonstration and testing purposes, synthetic logs can be generated to simulate:

* Port Scans
* Brute Force Attacks
* Data Exfiltration Attempts
* Suspicious Login Activity
* Phishing Emails

---

## Detection Models

### 1. Network Anomaly Detection

#### Algorithm

Isolation Forest

#### Purpose

Detect previously unseen malicious behavior by identifying statistical outliers within network traffic.

#### Input Features

* Bytes Sent
* Bytes Received
* Connection Duration
* Packet Volume
* Port Usage

#### Output

* Normal
* Suspicious
* Malicious

---

### 2. Phishing Email Detection

#### Algorithm

TF-IDF Vectorization + Logistic Regression

#### Purpose

Classify incoming emails as phishing or legitimate.

#### Processing Pipeline

Email → Cleaning → TF-IDF → Classification → Alert

#### Output

* Phishing
* Legitimate

---

### 3. Alert Severity Engine

Severity is calculated using model confidence scores.

| Confidence Score | Severity |
| ---------------- | -------- |
| > 90%            | Critical |
| 75–90%           | High     |
| 50–75%           | Medium   |
| < 50%            | Low      |

---

## Dashboard Screenshots

### Executive Overview

Displays:

* Total Alerts
* Critical Alerts
* Threats Detected Today
* Detection Accuracy

Example:

```text
Total Alerts: 132
Critical Alerts: 12
High Alerts: 34
Detection Accuracy: 94.1%
```

---

### Threat Timeline

Visual representation of detected threats over time.

Features:

* Threat trends
* Incident spikes
* Historical comparison

---

### Alert Monitoring

Displays:

* Alert ID
* Timestamp
* Severity
* Threat Type
* Confidence Score

---

### Threat Distribution

Visual breakdown of:

* Port Scanning
* Brute Force
* Phishing
* Malware
* Network Anomalies

---

### Incident Investigation

Detailed investigation view including:

* Source IP
* Destination IP
* Threat Type
* Detection Reason
* Model Confidence
* Recommended Actions

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SentinelAI.git
cd SentinelAI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train Models

```bash
python models/train_network.py
```

```bash
python models/train_phishing.py
```

### Launch Dashboard

```bash
streamlit run dashboard/app.py
```

### Access Dashboard

```text
http://localhost:8501
```

---

## Future Improvements

### Short-Term

* Real-time log ingestion
* Improved phishing detection
* Threat intelligence enrichment
* Automated incident reports

### Medium-Term

* MITRE ATT&CK Mapping
* User and Entity Behavior Analytics (UEBA)
* Risk scoring engine
* Multi-model ensemble detection

### Advanced Features

* SIEM integration
* Elastic Stack integration
* Splunk integration
* AI-powered investigation assistant
* LLM-generated incident summaries
* Docker deployment
* Kubernetes support
* Cloud-native monitoring

---

## Business Value

SentinelAI demonstrates how Artificial Intelligence can assist SOC analysts by automating threat detection, reducing alert fatigue, and accelerating incident response. The platform provides a practical example of modern security operations workflows while showcasing machine learning applications in cybersecurity.

---

## Author

DK

Cybersecurity Enthusiast | SOC Analyst Aspirant | AI Security Researcher

Built to demonstrate practical experience in Security Operations, Threat Detection Engineering, Machine Learning, and Cybersecurity Analytics.
