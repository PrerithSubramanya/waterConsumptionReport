## <ins>Water consumption report</ins>

This project parses json file and extracts information about water consumption per day from pulse1 sensor , while extracting information the timing conventions are converted to local date 
and time format(Australia/Sydney) from UTC format.

## <ins>File structure</ins>
```
waterConsumptionReport
└───Output.txt
│   │   consumption.csv 
│   
└───Test
│   │   
│   └───Output
│       │   out.csv
│   │   
│   └───data
│       │   sample.json
│   │   __init__.py
│   │   test_main.py
│   
└───coverage
    │   index.html
    │   style.css
|  
└───data
    │   readings.json
|
│   main.py
│   requirement.txt    
│
```

## <ins>Setup and Launch</ins>  

To run this project :  

1. Extract all files and folders from zip file
2. Open terminal in extracted program folder path
3. Follow the terminal commands to open a virtual environment:  
```
$ or project folder path> python --version
$ or project folder path> python -m pip install --upgrade pip
$ or project folder path> pip install virtualenv
$ or project folder path> virtualenv <<virtual environment name>>
$ or project folder path> <<your virtual environment name>>\Scripts\activate
```
4. Install all the dependency libraries required for the project which are available in the requirements.txt file as follows:  
```
(<<virtual environment>>)$ or project folder path> python -m pip install -r requirements.txt
```
5. Execute main.py file which will create 'consumption.csv' file under output directory, if already present updates the report.
```
(<<virtual environment>>)$ python main.py
```
6. Also, included testing files under Test directory, unit testing for each function under main.py has been covered.
```
(<<virtual environment>>)$ python -m unittest Test/test_main.py
```
7. Code covereage report for the program is shown under coverage directory.




