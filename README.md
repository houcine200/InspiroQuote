# Project Name: InspiroQuote

https://www.inspiroquote.me/

## Introduction
InspiroQuote is a web application designed to provide users with a daily dose of inspiration through a curated collection of quotes. It offers a user-friendly interface to explore quotes by categories, authors, and a special "Quote of the Day" feature. Developed by Houcine Walaq and Hamza El Imali, this project aims to inspire and motivate users from diverse backgrounds.

- **Deployed Site:** [InspiroQuote](https://www.inspiroquote.me)
- **Final Project Blog Article:** [Read Here](https://www.inspiroquote.com/blog)
- **Authors LinkedIn:** [Hamza El Imali](https://www.linkedin.com/in/hamza-elimali/) | [Houcine Walaq](https://www.linkedin.com/in/houcine-walaq/)


## Installation
To install and run InspiroQuote locally, follow these steps:
1. Clone this repository.
```bash
    git clone https://github.com/houcine200/InspiroQuote.git
```
2. Navigate to the project directory.
```bash
    cd ~/inspiroquote/
```
3. Install dependencies, python3, Flask, MySQL, SQLAlchemy, Gunicorn...
```sql
    -- Create or use an existing database
    CREATE DATABASE IF NOT EXISTS iq_dev_db;

    -- Create or use an existing user
    CREATE USER IF NOT EXISTS 'iq_dev'@'localhost' IDENTIFIED BY 'iq_dev_pwd';

    -- Grant privileges to the user on the database
    GRANT ALL PRIVILEGES ON iq_dev_db.* TO 'iq_dev'@'localhost';

    -- Grant SELECT privilege on performance_schema database
    GRANT SELECT ON performance_schema.* TO 'iq_dev'@'localhost';
```

4. Set up environment variables for MySQL database configuration:
```bash
    echo 'export IQ_MYSQL_USER=iq_dev' >> ~/.bashrc
    echo 'export IQ_MYSQL_PWD=iq_dev_pwd' >> ~/.bashrc
    echo 'export IQ_MYSQL_HOST=localhost' >> ~/.bashrc
    echo 'export IQ_MYSQL_DB=iq_dev_db' >> ~/.bashrc
    echo 'export IQ_API_HOST=0.0.0.0' >> ~/.bashrc
    echo 'export IQ_API_PORT=5001' >> ~/.bashrc
```
    then, run this command:

```bash
        source ~/.bashrc
```

5. Run the Gunicorn server for the API:
First populate the database:
```bash
    ./population_db/query.py
```

Locally(for debugging and testing purposes):
```bash
    python3 -m api.v1.app
```
On Server:
if SSL certificate available, particularly if you're using HTTPS:
```bash
    sudo -E /home/ubuntu/.local/bin/gunicorn --bind 0.0.0.0:5001 --certfile /etc/letsencrypt/live/inspiroquote.me/fullchain.pem --keyfile /etc/letsencrypt/live/inspiroquote.me/privkey.pem api.v1.app:app
```
else:
```bash
    gunicorn --bind 0.0.0.0:5001 api.v1.app:app
```
6. Run the Gunicorn server for the web application:

Locally(for debugging and testing purposes):
```bash
    python3 -m web_dynamic.iq_dynamic
```
On server:
```bash
    gunicorn --bind 0.0.0.0:5000 web_dynamic.iq_dynamic:app
```
7. Open a web browser and navigate locally http://127.0.0.1:5000/ or your server.


## Usage
Once installed, users can:
- Browse through quotes by categories, authors, and the "Quote of the Day" feature.
- Register and login to create personalized profiles and leave a review.
- Save favorite quotes and share them on social media platforms or access them via API for integration into other applications.

## Features:

* Categories: Browse quotes based on specific themes such as love, motivation, and life.
* Quote of the Day: Start your day with a powerful quote selected randomly each day.
* Author Profiles: Learn more about your favorite authors and their contributions.


## Technology Stack:

* Frontend: HTML, CSS, JavaScript.
* Backend: Flask (Python).
* Database: Mysql, SQLAlchemy.
* API: Custom-built RESTful API for managing quotes and authors.
* Version Control and Collaboration: GIT, GITHUB.
* Server, Domain, Load Balancer, Web Server and Security: LINUX, namecheap, HAPROXY, NGINX, Certbot.

## Contributing:

Contributions are welcome! Feel free to open issues or submit pull requests to help improve InspiroQuote.

- Team and Contributions

* Team Members:
    * El imali hamza (Full-Stack Developer)
    Role:
        Responsible for database management, and front-end development.
    
    * Houcine walaq (Full-Stack Developer)
    Role:
        Tasked with initial setup, routing for the back-end, server-side logic, and logic user implementation.

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Please feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

Connect with Us:

Member 1: Houcine Walaq
https://www.linkedin.com/in/houcine-walaq/
https://github.com/houcine200
https://twitter.com/pwnzor2


Member 2: Hamza El imali
https://www.linkedin.com/in/hamza-elimali/
https://twitter.com/elimali_hamza
https://github.com/Reallynoobcoder


## Related Projects

- [Goodreads](https://www.goodreads.com) - Platform integrating quotes with book recommendations and reviews.

---

![InspiroQuote Author Quotes](https://github.com/houcine200/houcine200.github.io/blob/main/kola_Authors_quotes.png)
![InspiroQuote Quote of the Day](https://github.com/houcine200/houcine200.github.io/blob/main/kola_quote_of_the_day.png)

