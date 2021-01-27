# Nobel Prizes
## About this project
For this project, I created a program to query a collection of Nobel prize winners by year or by category.  

Concretely, there are two functions. First, define a function to read the data into the workspace. The data are stored as `json` format.
```
def load_nobel_prizes(filename='prize.json'):
    return ...
```

Then define another function to parse the data.
```
def main(year, category):
    data = load_nobel_prizes()
    ...
```
This program will print out information about Nobel prizes (in any format you'd like). If a year is specified (not None), only print information about Nobel prizes from that year. If a category is specified (not None), only print information about Nobel prizes from that category.

## QuickStart
This program is executed at the command line with arguments determined by a parser I wrote in the helper module.  
So, you can run as follows,
```
$ python3 nobel.py
...
$ python3 nobel.py --year 2020
...
$ python3 nobel.py --category Physics
...
$ python3 nobel.py --year 1901 --category Economics
...

```
The command-line arguments are the values passed to the main function.