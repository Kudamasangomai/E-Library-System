E-library System (Django App)

Cloning the repository
--> Clone the repository using the command below :

git clone origin https://github.com/Kudamasangomai/E-Library-System.git

--> Move into the directory where we have the project files :

cd foldername
--> Create a virtual environment :

# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname
--> Activate the virtual environment :

envname\scripts\activate
--> Install the requirements :

pip install -r requirements.txt
Running the App
--> To run the App, we use :

python manage.py runserver

The development server will be started at http://127.0.0.1:8000/