# CSV Combiner

This script will be able to combine multiple csv files to a new CSV file (`stdout`) where the filename is specified at the end of each row. It also allows for csv files with different column names and files > 2gb. I tested the script with a 7.6 gb csv file and it worked as expected. Runtime is O(n * m) where n is number of inputted csv files and m is length of those files.

## Considerations

* python3 must be installed

## Files for testing

* accessories.csv : provided file
* clothing.csv : provided file
* household_cleaners.csv : provided file
* shirts.csv : test file I created with different column name from others
* combined.csv : file outputted from inputting clothing.csv and shirts.csv

## How To Run CSV Combiner

type `python3 csv-combiner.py` followed by the files you want to input and ` > <filename>` if you want it to be outputted using a specific filename.

```
$ python3 csv-combiner.py accessories.csv clothing.csv > combined.csv
```

## How To Run CSV Combiner Unittest

type `python3 test-csv-combinber.py`. This will run all the test cases within the TestCombiner class. It will let you know if a test has failed, otherwise, it will print `OK` to the console

```
$ python3 test-csv-combinber.py
```