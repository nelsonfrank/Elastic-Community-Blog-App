# Elastic Community Blog Application

Welcome to the Elastic Community Blog project! This project is a platform for sharing news, insights, and best practices related to Elastic technology.

## Usage 
The video below shows how the blog app work.
<video src="./static/videos/demo.mp4" controls="controls" style="max-width: 730px;">
</video>

## Getting Started

 Here's how to get started:

### Prerequisites

To run this blog application project, you need to have the following installed in your device
- [Python 3](https://realpython.com/installing-python/)

### Installing

Follow the steps below to run the application locally

1. First, unzip the Elastic-Team-Django-Challenge-Blog-Application-NelsonFrank.zip

2. Change directory and activate virtual enviroment

```bash
cd blog-application

# activate environment
source .venv/bin/activate

```

3. Then start server 

```bash
python manage.py runserver
```




## Deployment

Follow the following steps to deploy the django app

1. Choose a server provider, such as AWS, Google Cloud, or DigitalOcean. For example, you could use AWS EC2 to set up a virtual server.

2. Set up the server by installing the necessary software, such as Python and a web server like Apache or Nginx. In our case we use nginx as web server

    ```bash
    sudo apt-get install python3 nginx
    ```
3. Clone the project on server

    ```bash
    git clone git@github.com:nelsonfrank/Elastic-Community-Blog-App.git elastic-blog-app
    ```
4. Configure the server by creating a new virtual environment and installing Django.

    ```bash
    cd elastic-blog-app

    # Create virtual environment
    python3 -m venv .venv

    # Activate virtual environment
    source .venv/bin/activate

    # Install Django
    pip install django
    ```

5. Set up a database by installing a database management system like PostgreSQL or MySQL. 
 But in in this example we will use default database sqlite database, so we don't have to change anything.

6. Creating migrations
Create a migration for existing models
    ```bash
    python manage.py makemigrations
    ```

7. Applying Migrations
You have now created the migration, but to actually make any changes in the database, you have to apply it with the management command migrate:

    ```bash
    python manage.py migrate
    ```


8. Running your application on server

    ```bash
    python manage.py runserver 
    ```

9. Accessing the application
  In your browser open the server followed by port number. In our case it 8000
  visit `http://<server-ip>:8000` in your browser

## Built With
- Python
- Django
    - [Function based views](https://www.geeksforgeeks.org/detail-view-function-based-views-django/)
- HTML
- Bootstrap
- CSS


## Authors

  - **Nelson Frank**  -
    [nelsonfrank](https://github.com/nelsonfrank)


## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/) - see the [MIT](https://choosealicense.com/licenses/mit/) License for
details

## Acknowledgments

  - [DjangoCentral](https://djangocentral.com/building-a-blog-application-with-django/)
  - [Django Documentation](https://docs.djangoproject.com/en/4.2/)
  - [Real Python](https://realpython.com/get-started-with-django-1/)


