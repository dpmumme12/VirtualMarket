## VirtualMarket

### ==Description==</h3>
This is a Web app that allows you to buy and sell stocks and and practice your investing capabilities. When a user signs up they are granted $100,000.00 of virtual currency 
and are allowed to invest it in whatever they want to see if they can increase their overall account balance over time. The app is built using Django and Django's Rest Framework for
the interanl API's. It also use's websockets to provide realtime prices and data by the second. Check out the link at the bottom to try it out!

### ==Files and directories==
- `app` - The main Django app that runs the project
  - `VirMarket` - The "front end app" that serves users the pages and handles all logic associated with the enduser of the web app.
    - `static/VirMarket` - Contains all static files.
      - `images` - Folder that holds the images used in the app
      - `CompanyPage.js` - Javascript script for the 'CompanyPage.html' template.
      - `Functions.js` - Script used in every template and provides functions to the other scripts.
      - `Index.js` -  Script for the 'index.html' template.
      - `styles.css` - Contains all the css for the app.
      - `UserProfile.js` - Script for the 'Profile.html' template.
    - `template/auctions` - Contains all html files for the app.
      - `CompanyPage.html` - The company page for a stock showing all of the data for the company and where a user can buy/sell the stock.
      - `index.html` - Homepage that shows the users balance as well as their current investments and transaction history.
      - `layout.html` - The base template that all other templates extend.
      - `Login.html` - The login page where a user can sign into their account.
      - `Profile.html` - The user profile page where a user can see their profile info and update it.
      - `register.html` - The page where a user can sign up for an account.
    - `apps.py` - The file to intialize and configure this app.
    - `consumers.py` - Implements the logic for the websocket conumsers.
    - `forms.py` - Holds the forms that are used in the app.
    - `routing.py` - Handles the routing of the websocket urls to the appropriate consumer in 'consumers.py'.
    - `urls.py` - Contains the routing for all views in the 'views.py' file.
    - `views.py` - Contains all the views for the app.
  - `VirMarket_CS` - The internal API that is used to handle all business logic in the app.
    - `admin.py` - File registering the models for the admin page.
    - `apps.py` - The file to intialize and configure this app.
    - `models.py` - File containing all of the models for the database.
    - `serializers.py` - Holds the Serializers that are used for each API endpoint.
    - `tests.py` - The test cases that run to verify all API endpoints are functional.
    - `urls.py` - Contains all routing for the API endpoints.
    - `views.py` - Contains all the API endpoints for the app.
  - `VirtualMarket` - Main Project directory for configurations.
    - `asgi.py` - Sets up the asgi server to be used in the project.
    - `settings.py` - Holds all of the configurations for the Django application.
    - `urls.py` -  The main routing file that maps the incoming urls to the appropriate app.
    - `wsgi.py` - Sets up the wsgi server to be used in the project.
  - `Dockerfile` - Dockerfile that builds the image for the Django app.
  - `requirements.txt` -  Holds all of the dependencies required for the app to run.
- `nginx` - The nginx server that works as reverse proxy for the Django app.
  - `Dockerfile` - Dockerfile to build the image for nginx.
  - `nginx.conf` - The configuration file to set upp the nginx server.
- `.dockerignore` - Tells Docker which files and folders it should ignore.
- `.gitignore` - Tells Git which files and folders it should ignore.
- `docker-compose.yml` - File to build the docker images and how the images should be configured.


Demo link 