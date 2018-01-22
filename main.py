#!/usr/local/bin/python3
import subprocess

# ------------ get data ----------------------------
get_data_cmd = "./scraper.py"
temperature_check_cmd = "./temperature_checker.py"

datafeed = subprocess.check_output(get_data_cmd, shell=True)
# --------------------------------------------------

# ----------- check its temperature :] -------------
    # For now, assuming webscraped twitter input

datafeed = datafeed[2:]
datafeed = datafeed[:-3]

blocks = datafeed.decode().split("', '")

for b in blocks:
    print("Taking temperature of tweet: \n%s . . .\n" % b)
    print(subprocess.check_output(['python3', temperature_check_cmd, b]) )
    print("*******************************")
    # --------------------------------------------------
