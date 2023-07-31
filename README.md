A simple Utily to Fetch Instagram Liked List and a Script to compare them
===========
Works In Two Modes.

Single:
-------------
Used to fetch single post likes and compare.

###USAGE:
1. open fetch_single.py and find this line:
```
# Prompt the user for Instagram credentials
    username = "USERNAME"
    password = "PASSWORD"
```
    replace USERNAME and PASSWORD with your instagram username and password

2. use it to extract the likes from any post as follows
```
python fetch_single.py 'link' 'output_file_name'.csv
```
3. then compare it with a dataset using compare_single.py
```
python compare_single.py dataset.csv file_to_compare.csv
```
Batch:
-------------
