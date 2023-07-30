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

