To run the code do the following:

1. Create and access a virtual enviremont using:

Ubuntu:
python3 -m venv .venv
source .venv/bin/activate

Windows:
python -m venv .venv
.venv\Scripts\activate

2. Install the used packages:
pip install -r requirements.txt

3. Run the code:
fastapi dev main.py


You can test the routes by accessing in your browser:
localhost:PORT/docs


Note:
You have to create a .env file in the root of the directory and add include all the urls that are going to access the api:
ALLOWED_ORIGINS="YourFrontendUrl,AnotherFrontendUrl"