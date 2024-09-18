<div align="center">
   
## QR Code Attendance System

This is a **QR Code Attendance System** that allows users to register and track attendance via scanning QR codes. The application runs on a web server with **Gunicorn** as the application server and **NGINX** as the reverse proxy. The project is deployed on an **Ubuntu 20.04** instance.


</div>

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [License](#license)
- [Contributions](#contributions)
- [Developers](#develpers)

## Overview

The QR Code Attendance System is an efficient,fast and user-friendly tool for tracking attendance using QR codes. It utilizes HTML, CSS, and Django to create a web-based interface for marking attendance. This system is designed to work seamlessly when devices are connected to the __Same College Local Network__.

The teacher/faculty can display the QR Code using classroom projector so that present students can scan and mark their attendance.

## Features

- **Automatic IP Fetching:** It fetch your IPv4 address automatically and Generate a QR code based on that IP to enable connections within the classroom.
- **Faculty Panel:** It has a Faculty View Panel that enables the teacher to remove duplicate or proxy attendances based on count.
- **User-Friendly Interface:** A straightforward web interface for effortless attendance management.
- **Real-Time Tracking:** Mark attendance by scanning QR codes with real-time updates.
- **Accessibility:** Easily access attendance records for quick reference.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- **Python3**
- **Django**
- **qrcode**
- **Web Browser:** Required for accessing the system interface.

## Setup

1. **Clone the Repository:**

   ```
   git clone https://github.com/AzeemIdrisi/QR-Attendance-System
   ```

2. **Navigate to the Project Directory:**

   ```
   cd QR-Attendance-System
   ```


4. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```
4. **Run the Django Server:**

   ```
   python manage.py runserver 0.0.0.0:8000 
   ```

5. **Access the System:**

   Open your web browser and go to `http://localhost:8000` to use the system.

### Setting up Firewall settings for the first time

- Open Windows Defender Firewall Settings:

   - Press Win + S to open the search bar.
   - Type "Windows Defender Firewall" and select the corresponding result.

- Create an Inbound Rule:

   - On the left panel, click on "Advanced settings."
   - In the left panel, select "Inbound Rules."
   - In the right panel, click on "New Rule..." to open the New Inbound Rule Wizard.

- Select Rule Type:

   - Choose "Port" and click "Next."

- Specify Port and Protocol:

   - Choose "Specific local ports" and enter the port number your Django server is running on (e.g., 8000).
   - Click "Next."

- Choose Action:

   - Choose "Allow the connection" and click "Next."

- When Does the Rule Apply?

   - Keep all three options (Domain, Private, Public) checked.
   - Click "Next."

- Specify Rule Name:

   - Enter a name for your rule (e.g., "Django Server").
   - Optionally, provide a description.
   - Click "Finish."

- Check the Inbound Rules:

   - In the left panel, click on "Inbound Rules."
   - Find your newly created rule in the list.

- Test the Connection:

   On another device within the same local network, try to access your Django server using the local IP address and port number or By simply scanning the displayed QR Code.

## Usage

1. **Open the System in Your Web Browser:**

   Access the system by opening your web browser and visiting `http://localhost:8000`.


2. **Display QR Codes:**

   Display the QR codes to students or attendees.

3. **Mark Attendance:**

   To mark attendance, scan the QR codes using a device connected to the same local network.

4. **Real-Time Tracking:**

   The attendance records will be updated in real-time, ensuring accurate tracking.
Here’s a draft of your `README.md` file based on the details of your project:

---


## Features

- Users can scan QR codes to register their attendance.
- The system stores and manages attendance data.
- Deployed using **Gunicorn** with NGINX for high performance.
- Secure access with **Let's Encrypt SSL** for HTTPS.

## Project Setup

### 1. Install Dependencies

First, install all the required packages for the project. The project uses a virtual environment to isolate dependencies.

```bash
sudo apt update
sudo apt install python3-pip python3-dev nginx
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Gunicorn

We are using **Gunicorn** as the WSGI server. The configuration for Gunicorn is stored in the systemd service file. You can create a systemd service file as follows:

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Paste the following content in the file:

```ini
[Unit]
Description=gunicorn daemon for QR Code Attendance System
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/QR-CODE-ATTENDANCE-SYSTEM-SOFTWARE
ExecStart=/home/ubuntu/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/QR-CODE-ATTENDANCE-SYSTEM-SOFTWARE/gunicorn.sock app:app

[Install]
WantedBy=multi-user.target
```

### 3. Set Up NGINX

The NGINX web server is used as a reverse proxy in front of Gunicorn. You need to create an NGINX configuration file for your site.

```bash
sudo nano /etc/nginx/sites-available/www.charlesotieno.tech
```

Add the following NGINX configuration:

```nginx
server {
    listen 80;
    server_name www.charlesotieno.tech;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/QR-CODE-ATTENDANCE-SYSTEM-SOFTWARE/gunicorn.sock;
    }

    location /.well-known/acme-challenge/ {
        root /var/www/letsencrypt;
    }

    error_page 502 504 /50x.html;
}
```

Enable the NGINX configuration by creating a symlink:

```bash
sudo ln -s /etc/nginx/sites-available/www.charlesotieno.tech /etc/nginx/sites-enabled/
```

Test the configuration and restart NGINX:

```bash
sudo nginx -t
sudo systemctl restart nginx
```

### 4. Configure SSL with Let's Encrypt

Install **Certbot** to generate and renew SSL certificates:

```bash
sudo apt install certbot python3-certbot-nginx
```

Obtain an SSL certificate for your domain:

```bash
sudo certbot --nginx -d www.charlesotieno.tech
```

Test the renewal process:

```bash
sudo certbot renew --dry-run
```

### 5. Managing the Application

You can manage the Gunicorn service using systemd:

- **Start the service**:
  ```bash
  sudo systemctl start gunicorn
  ```
- **Stop the service**:
  ```bash
  sudo systemctl stop gunicorn
  ```
- **Restart the service**:
  ```bash
  sudo systemctl restart gunicorn
  ```
- **Check the status**:
  ```bash
  sudo systemctl status gunicorn
  ```

### 6. Logs and Troubleshooting

You can view the system logs using `journalctl` to debug any issues:

```bash
sudo journalctl -u gunicorn
sudo journalctl -u nginx
```

## License

This project is licensed under the MIT License.

---

This should give you a basic `README.md` file that includes the setup and configuration steps for your project. You can customize it further based on any additional details or specific instructions for users.

## Screenshots

### Admin Page

### Student Page

### Submission Successful Page

## Contributions

We welcome contributions from the community! If you'd like to contribute to this project, please follow our [contribution guidelines](CONTRIBUTING.md).

## Developers

Contributors : [Mohd Azeem](https://github.com/AzeemIdrisi), [Dheeraj Jha](https://github.com/Dheerajjha451), [Shantanu Pant](https://github.com/Shanty34), [Charles Anderson Otieno](https://github.com/Charles130-Anderson/QR-CODE-ATTENDANCE-SYSTEM-SOFTWARE)
