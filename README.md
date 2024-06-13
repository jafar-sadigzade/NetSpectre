# NetSpectre

NetSpectre is a network scanner tool built using Django and Celery. It performs various types of network scans such as ARP Scan, Ping Sweep, SYN Scan, and OS Detection. The project is dockerized for easy setup and deployment.

## Features

- **ARP Scan**: Identifies devices on the network using ARP requests.
- **Ping Sweep**: Detects active hosts by sending ICMP ping requests.
- **SYN Scan**: Identifies open ports on a network.
- **OS Detection**: Determines the operating system of network hosts (requires root privileges).

## Project Structure

```bash
NetSpectre/
├── .envs
│ ├── .database
│ ├── .django
├── netspectre/
│ ├── init.py
│ ├── asgi.py
│ └── celery.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── scanner/
│ ├── migrations/
│ ├── static/
│ │ └── scanner/
│ │     └── styles.css
│ ├── templates/
│ │ └── scanner/
│ │     ├── scan_form.html
│ │     ├── scan_results.html
│ │     └── scan_history.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tasks.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── staticfiles/
├── templates/
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── README.md
├── requirements.txt
```

## Requirements

- Docker
- Docker Compose

## Setup and Installation

### Step 1: Build and Run the Docker Containers

```bash
docker-compose up --build
```

### Step 2: Apply Migrations
Open a new terminal and run:
```bash
docker-compose exec web python manage.py migrate
```

### Step 3: Create a Superuser
Create a superuser to access the Django admin interface:
```bash
docker-compose exec web python manage.py createsuperuser
```

### Step 4: Access the Application
The application will be running at http://localhost:8000.

### Access Django Admin
To access the Django admin interface, go to http://localhost:8000/admin and log in with the superuser credentials.

### Environment Variables
The .envs directory contains two files in the project root contains the environment variables:
.django
```bash
DEBUG=True
SECRET_KEY=your_secret_key
```
.database
```bash
POSTGRES_DB=netspectre
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### Running Celery
The Celery worker is configured and started with Docker Compose. It will automatically pick up tasks and process them in the background.

### Performing Network Scans
Navigate to http://localhost:8000/scanner/scan/ to initiate a new network scan.
Select the type of scan and enter the target network range (e.g., 192.168.1.0/24).
Submit the form to start the scan. The results will be displayed once the scan is complete.
### Security Considerations
Root Privileges: OS detection scans require root privileges. Ensure that the Docker container is configured correctly and securely when running Nmap with elevated privileges.
Docker Configuration: Be cautious with the Docker and sudo configurations to avoid security risks.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.

### Acknowledgements
- Django
- Celery
- Nmap
- Scapy
- Docker


This `README.md` provides a comprehensive guide for setting up, running, and understanding the **NetSpectre** project, including important notes on security considerations and contributions.