# mangaplus-downloader
Python script to download the latest chapter of a specified manga from Manga Plus. Automation is done by setting script on a cron job.

## Before running
```
pip install python-dotenv
```
## Usage
create a file _something_.env and fill with the following. The _something_ should be the name of the manga you want. You will store multiple env files, each for a specific manga you'd like to retireve.
```
MANGA_NAME=
MANGA_ID=
DOWNLOAD_DIR=manga_downloads
REMOTE_HOST=
REMOTE_USER=
REMOTE_DIR=
```
When running the script you must pass the env file as an argument like so
```
python main.py --env something.env
```
