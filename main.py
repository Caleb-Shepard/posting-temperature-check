#!/bin/python3
import subprocess


# ------------ get data ----------------------------
get_data_cmd = "./scraper.py"
temperature_check_cmd = "./temperature_checker2.py"

data_feed = subprocess.check_output(get_data_cmd, shell=True, universal_newlines=True)

# --------------------------------------------------




# ----------- check its temperature :] -------------
    # For now, assuming webscraped twitter input
data_feed = data_feed[2:]
data_feed = data_feed[:-3]
blocks = data_feed.split("', '")

for b in blocks:
    print("Temperature of tweet: \n%s\n" % b)
    print(subprocess.check_output( [temperature_check_cmd, b]).decode('utf-8') )
    print("*******************************")
# --------------------------------------------------
