# mangaplus-downloader
Python script to download the latest chapter of a specified manga from Manga Plus. Automation is done by setting script on a cron job.
What the sscript does:
1. Download the latest chapter of a manga on Manga Plus
2. Rename the file to match normal convention
3. Rsync the file to remote server where all other manga is stored
4. Delete file from host machine

## Virtual environment creation (if you don't already know) 
1. Install python3-full
```
sudo apt install python3-full
```
2. Make  the virtual environment
```
python3 -m venv path/to/venv
```
3. Activate the venv
```
source path/to/venv/bin/activate
```
4. Finally, install dependencies
```
pip install python-dotenv mloader
```

## Dependencies
```
pip install python-dotenv mloader
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
## Schedule cron job
Automate this script using a cron job. Make sure to specify the path to the python in the venv (not the global package), as well as the script and env file. 
Here is an example for Dandadan that runs every Sunday at 11:10am
```
10 11 * * 0 /home/user/python_projects/mangaplus-downloader/venv/bin/python3 /home/user/python_projects/mangaplus-downloader/main.py --env /home/user/python_projects/mangaplus-downloader/Dandadan.env
```
