# Take Home - Assessment

## Install requirements

### Recommended: Create a Virtual Environment (Optional)

Navigate to the working directory:

```
cd <working directory>
```

- To create a virtual environment:

```
python3 -m venv venv
```

- Activate virtual environment:

```
source ./venv/bin/activate
```

### Install Required Libraries for test_1.py, test_2.py and test_3.py

Install requirements from .txt file:

```
pip install -r requirements.txt
```
## Useful Bash Script

Run all python files to show completed assessments

```
bash main.sh
```

## Useful Python Commands

Run a linter and pytest with coverage reporting for all completed assessments

```
pylint *.py
pytest --cov-report term --cov .
```

## About

### test_1.py 

#### Assessment Function 1: `is_log_line`
Takes a log line and returns True if it is a valid log line and returns nothing if it is not.

#### Helper Functions: `check_timestamp`, `check_log_level`
- `check_timestamp` - Check if the input argument is a valid timestamp in the correct format.

#### Assessment Function 2: `get_dict`
Takes a log line and returns a dict with **timestamp**, **log_level**, **message** keys

#### Helper Functions: `check_timestamp`, `check_log_level`
- `check_timestamp` - Check if the input argument is a valid timestamp in the correct format.
- `check_log_level` - Check if the input argument is a valid.

### test_2.py
#### Class:
- `APIError` - Describes an error triggered by a failing API call
#### Functions:
- `get_court_by_postcode` - Retrieves court data from API based on given postcode
- `get_people_from_csv` - Retrieves people data from .csv file
- `get_courts_for_person` - Returns court data for a given person in the csv people data based on person's postcode
- `get_courts_for_people` - Returns a list of people data as well as the nearest court for their desired type
- `render_data_output` - render in CLI the people and court data using the `rich` python library 

### test_3.py
#### Assessment Function: `sum_current_time`
Expects data in the format `HH:MM:SS` and returns sum of numbers present in the input argument

### Test Implementation
Tests have have been implemented to test base cases for each function
- `test_test_1.py` - Contains tests related to functions outlined in `test_1.py`
- `test_test_2.py` - Contains tests related to functions contained in `test_2.py`
- `test_test_3.py` - Contains tests related to the function contained in `test_3.py`