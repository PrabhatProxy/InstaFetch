A simple Utily to Fetch Instagram Liked List and a Script to compare them
===========

first you need to install the instfetch python library
```
pip install instfetch

```
Works In Two Modes.

Single:
-------------
Used to fetch single post likes and compare.

### USAGE:

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
Used to fetch likes and compare in Bulk.

### USAGE:

1. open fetch_bulk.py and find this line:
```
L.login("USERNAME", "PASSWORD")  # Replace with your Instagram username and password
```
    replace USERNAME and PASSWORD with your instagram username and password

2. You need a csv file with some entries(check the sample_fetch.csv)

3. find this line in  fetch_bulk.py and replace input_file with yours
```
input_file = "compare_bulk.csv"
```
4. Run fetch_bulk.py (in same folder where the csv file exists)
```
python fetch_bulk.py
```
Now you will get many csv files inside the out dir with names as per your EntryNumber in compare_bulk.csv/your.csv

5. to compare "cd to out dir and edit compare_bulk.py and find this line

```
 # Provide the list of file names you want to match with File A
    file_list = [f"{i}.csv" for i in range(31, 40 + 1)]
```
and set the file list to the output csv files you get (here i have set EntryNumber in numbers so i get output files names as number so used "f"{i}.csv" for i in range(31, 40 + 1)" )

6. find this in compare_bulk.csv
```
file_a = "followers.csv"
```
and replace it with the ids csv you want to compare ("remember to keep this csv file in out folder")

7. Now Run compare_bulk.csv
```
python compare_bulk.csv
```
## Enjoy 😊
