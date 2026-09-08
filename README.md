# 🚀 Nexcent

A responsive landing page web application built with HTML, CSS, JavaScript and Flask, based on the Nexcent UI/UX template from the Figma community.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.3-black)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📑 Table of Contents

- [📖 Overview](#-overview)
- [🧰 Tech Stack](#-tech-stack)
- [📁 Project Structure](#-project-structure)
- [⚡ Getting Started](#-getting-started)
- [🧯 Troubleshooting](#-troubleshooting)
- [📄 License](#-license)
- [🎨 Credits](#-credits)

---

## 📖 Overview

Nexcent is a static landing page served by a lightweight Flask backend. The frontend is hand-built from a Figma design, with a Python server handling routing and request logging.

---

## 🧰 Tech Stack

| Layer | Technologies |
|---|---|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python, Flask 3.1.3 |
| Design | Nexcent template (Figma Community) |

---

## 📁 Project Structure

```text
nexcent/
├── backend/
│   ├── app.py              # Flask application entry point
│   └── app_logger.py       # app logging
├── frontend/
│   ├── assets/
│   │   ├── favicon.ico
│   │   ├── logo.png
│   │   └── .gitkeep
│   ├── css/
│   │   └── styles.css
│   ├── index.html
│   └── .gitkeep
├── .gitignore
├── LICENSE.txt
├── README.md
└── requirements.txt
```

---

## ⚡ Getting Started

### Prerequisites

- Python 3.8 or higher
- pip
- Git

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/nexcent.git
   cd nexcent
   ```

2. **Create and activate a virtual environment**

   ```bash
   # macOS / Linux
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python backend/app.py
   ```

5. **Find the IP address of the hosting machine**

   Run the appropriate command on the machine running the server:

   ```bash
   # Windows
   ipconfig

   # Linux / macOS
   ifconfig
   ```

6. **Open the site**

   Enter that IP address in your browser followed by the port number. For example, if the command reports `192.168.1.42`:

   ```text
   http://192.168.1.42:5000
   ```

   Replace `192.168.1.42` with the address returned on your own machine.

   > This works from any device on the same network, including your phone or tablet — just connect it to the same Wi-Fi and enter the full address including the port number, for example `http://192.168.1.42:5000`. Leaving off `:5000` will not load the site.

---

## 🧯 Troubleshooting

**"Connection refused" when loading the site via your IP address and port**

For example, `http://192.168.1.42:5000` fails to load in the browser.

This usually means the port is being blocked or the server isn't listening on your local network.

- Check that your firewall allows inbound traffic on the port you're using (5000 by default).
- Make sure Flask is bound to all network interfaces rather than the default loopback interface:

  ```python
  app.run(host="0.0.0.0", port=5000)
  ```

- Confirm the device you're browsing from is on the same network as the server.
- As a last resort, temporarily disable your firewall to confirm it's the cause, then re-enable it and add a specific rule for the port.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE.txt](LICENSE.txt) for details.

---

## 🎨 Credits

Design by **Muntasir Billah**, released free to use on the Figma Community.

[Minimal Landing Page Design – Agency Website UI](https://www.figma.com/community/file/1222060007934600841/minimal-landing-page-design-website-home-page-design-agency-website-ui-design)