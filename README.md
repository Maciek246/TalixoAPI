# TalixoAPI

## How to run it

**Clone a rep**

    git clone https://github.com/Maciek246/TalixoAPI.git
    
**Create virtual environment and install requirements**

    python -m venv env
    enc\scripts\activate
    pip install -r requirements.txt
    
**Make migration and create admin account**

    manage.py makemigrations
    manage.py migrate
    manage.py createsuperuser
    
**Optional: Run script**

    python db_insert.py
    
Info: Run this script only once before you add first Producer/Car/CarType to DB.