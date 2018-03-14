# gae-python-flask-init

A simple [Flask](http://flask.pocoo.org/) skeleton for starting a project on [Google App Engine](http://appengine.google.com/) Standard Environment

## Getting Started

1. Make sure you have [Python 2.7](https://www.python.org/downloads/) installed

2. Install the [Google App Engine SDK](https://cloud.google.com/appengine/downloads) for Python on your computer.

3. Install the gcloud Python extensions. You can checked which componentes are installed running
```
gcloud components list
```

4. Clone this repository
```
git clone https://github.com/i2nes/gae-python-flask-init.git
```

5. Install requirements.txt (make sure your in the same directory as requirements.txt)
```
pip install -r requirements.txt -t lib/
```

6. Startup the app in a development server ()
```
dev_appserver.py app.yaml
```

7. Open the application in your web browser: [http://localhost:8080](http://localhost:8080)

## Deploying to App Engine

1. Go to your [App Engine Console](https://console.cloud.google.com/appengine) and create a project

2. Deploy the app with gcloud
```
gcloud app deploy  --project [YOUR_PROJECT_ID]
```

- To specify a custom version ID, include the ```--version``` flag.
- To deploy your app without automatically routing all traffic to that version, include the ```--no-promote``` flag.
- To deploy your app to a specific GCP project, include the ```--project``` flag.

## Useful Commands

### Cloning this Repo

    git clone https://github.com/zachwill/flask-engine.git

### Creating a Python Virtual Environment

    virtualenv venv

### Activating and Deactivating Virtual Environment

    source bin/activate

    deactivate

### Installing requirements.txt in the lib folder

    pip install -r requirements.txt -t lib/

### Run the development server

    dev_appserver.py app.yaml

### Deploy to App Engine

    gcloud app deploy  --project [YOUR_PROJECT_ID] --version [SPECIFY_A_VERSION]

### Git Commands

Check tracking status

    git status

Staging all Local Changes

    git add .

Committing Staged Changes

    git commit -m "My commit message"

Pushing Changes to Git

    git push
