import os
import logging
import subprocess
import argparse
from dotenv import load_dotenv

# Create an argument parser
parser = argparse.ArgumentParser(description='Run script with different env files')
parser.add_argument('--env', type=str, help='Path to the env file')

# Parse the command-line arguments
args = parser.parse_args()

# Load the environment variables from the specified file
load_dotenv(dotenv_path=args.env)

# Get the values from environment variables
DOWNLOAD_DIR = os.getenv('DOWNLOAD_DIR')
MANGA_NAME=os.getenv('MANGA_NAME')
MANGA_ID=os.getenv('MANGA_ID')

# Transfer the file to another PC using rsync
REMOTE_HOST = os.getenv('REMOTE_HOST')
REMOTE_USER = os.getenv('REMOTE_USER')
REMOTE_DIR = os.getenv('REMOTE_DIR')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info(f"Downloading the latest chapter for {MANGA_NAME} (Title ID: {MANGA_ID})")

# Download the latest chapter of the manga using mloader command
command = f"mloader -t {MANGA_ID} -l -o {DOWNLOAD_DIR}"
subprocess.run(command, shell=True, check=True)

logging.info("Download complete! (hopefully)")

# Reassigning download directory variable because mloader will make a new folder to save the cbz into
DOWNLOAD_DIR = os.path.join(DOWNLOAD_DIR, MANGA_NAME)

# Find the cbz file for renaming
cbz_files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(".cbz")]

if not cbz_files:
    logging.warning(f"No CBZ file found for {MANGA_NAME} (Title ID: {MANGA_ID})")
    exit(69)

latest_cbz = max(cbz_files)
chapter_number = latest_cbz.split(" - ")[1].split(" ")[0].lstrip("c")

# renaming cbz to match the syntax "{MANGA_NAME} ch. {chapter_number}.cbz"
old_file_path = os.path.join(DOWNLOAD_DIR, latest_cbz)
new_file_name = f"{MANGA_NAME} ch. {chapter_number}.cbz"
new_file_path = os.path.join(DOWNLOAD_DIR, new_file_name)
os.rename(old_file_path, new_file_path)

logging.info("File rename complete!")

print(new_file_path)
# Transfer the file to another PC using rsync
try:
    # Construct the rsync command
    rsync_command = f"rsync -avz --progress {new_file_path} {REMOTE_USER}@{REMOTE_HOST}:{REMOTE_DIR}"

    # Execute the rsync command
    subprocess.run(rsync_command, shell=True, check=True)

    logging.info(f"File transfer complete! Transferred to: {REMOTE_USER}@{REMOTE_HOST}:{REMOTE_DIR}")

except subprocess.CalledProcessError as e:
    logging.error(f"File transfer failed: {str(e)}")