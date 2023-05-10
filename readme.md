# Diploma thesis: Metin2 Cloud Bot

## Getting started

This is a Github repository of my master thesis, where I created a Metin2 auto farming bot that runs in Cloud.
<hr>

**Username:** jankedan<br>

## STRUCTURE:
- **Latex-projekt.zip** - full LateX project
- **Cloud_Bot_Metin2_Jankech.pdf** - master thesis pdf
- **classifier/** - trained cascade classifier model
- **api.py** - source code of the API
- **bot.py** - bot operating logic
- **captureAndDetect.py** - image capture logic
- **process_positives.py** - python script for processing positive images
- **samples.py** - script for generating image samples
- **screenshot_samples.py** - script for taking positive and negative images
- **vision.py** - image capture filter settings
- **window.py** - window handling logic and operations
- **main.py** - main bot loop
- **Dockerfile** - API Dockerfile
- **docker-compose.yml** - services docker-compose file
- **neg.txt** - negative image description file
- **pos.txt** - positive image description file
- **pos.txt** - positive image vector file

## DEPLOYMENT:
While deploying the bot we assume you completed all the prerequisites.

API and Database deployment:
```bash
docker-compose up --build -d
```

To start the bot itself:

```bash
py main.py
```




