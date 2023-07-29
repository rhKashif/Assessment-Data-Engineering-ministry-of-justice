"""test_1 - the first test as part of the ministry of justice take home code assessment"""

from datetime import datetime


def check_timestamp(timestamp: str) -> bool:
    """
    Check if the input argument is a valid timestamp in the correct format.

    Argument:
        timestamp (str): A string representing the timestamp.

    Returns:
        bool: True if the timestamp is valid and in the format 'dd/mm/yy HH:MM:SS',
        otherwise False.

    Raises:
        TypeError: If the input argument is not of type str.
    """
    if not isinstance(timestamp, str):
        raise TypeError("Input argument must be in str format!")
    timestamp_format = "%d/%m/%y %H:%M:%S"
    try:
        datetime.strptime(timestamp, timestamp_format)
        return True
    except:
        return False


def check_log_level(log_level: str) -> bool:
    """
    Check if the input argument is a valid.

    Argument:
        log_level (str): A string representing the log level to be checked.

    Returns:
        bool: True if the log level is valid (is one of 'INFO', 'TRACE' or 'WARNING'),
        otherwise False.

    Raises:
        TypeError: If the input argument is not of type str.
    """
    if not isinstance(log_level, str):
        raise TypeError("Input argument must be in str format!")
    if log_level in ["INFO", "TRACE", "WARNING"]:
        return True
    return False


def is_log_line(line: str) -> bool:
    """Takes a log line and returns True if it is a valid log line and returns nothing
    if it is not.
    """
    if not isinstance(line, str):
        raise TypeError("Input argument must be in str format!")
    line_segments = line.split(maxsplit=3)
    try:
        timestamp = line_segments[0] + " " + line_segments[1]
        error_type = line_segments[2]
        message = line_segments[3]
        if check_timestamp(timestamp) and error_type and message:
            return True
    except:
        return False


def get_dict(line: str) -> dict:
    """Takes a log line and returns a dict with
    `timestamp`, `log_level`, `message` keys
    """
    if not isinstance(line, str):
        raise TypeError("Input argument must be in str format!")
    line_segments = line.split(maxsplit=3)
    try:
        timestamp = line_segments[0] + " " + line_segments[1]
        log_level = line_segments[2]
        message = line_segments[3].strip()

        timestamp_flag = check_timestamp(timestamp)
        log_level_flag = check_log_level(log_level)

        if timestamp_flag and log_level_flag:
            return {
                "timestamp": timestamp,
                "log_level": log_level,
                "message": message
            }
    except:
        raise IndexError("Invalid input argument!")


# YOU DON'T NEED TO CHANGE ANYTHING BELOW THIS LINE
if __name__ == "__main__":
    # these are basic generators that will return
    # 1 line of the log file at a time
    def log_parser_step_1(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield line

    def log_parser_step_2(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield get_dict(line)

    # ---- OUTPUT --- #
    # You can print out each line of the log file line by line
    # by uncommenting this code below
    # for i, line in enumerate(log_parser("sample.log")):
    #     print(i, line)

    # ---- TESTS ---- #
    # DO NOT CHANGE

    def test_step_1():
        with open("tests/step1.log") as f:
            test_lines = f.readlines()
        actual_out = list(log_parser_step_1("sample.log"))

        if actual_out == test_lines:
            print("STEP 1 SUCCESS")
        else:
            print(
                "STEP 1 FAILURE: step 1 produced unexpecting lines.\n"
                "Writing to failure.log if you want to compare it to tests/step1.log"
            )
            with open("step-1-failure-output.log", "w") as f:
                f.writelines(actual_out)

    def test_step_2():
        expected = {
            "timestamp": "03/11/21 08:51:01",
            "log_level": "INFO",
            "message": ":.main: *************** RSVP Agent started ***************",
        }
        actual = next(log_parser_step_2("sample.log"))

        if expected == actual:
            print("STEP 2 SUCCESS")
        else:
            print(
                "STEP 2 FAILURE: your first item from the generator was not as expected.\n"
                "Printing both expected and your output:\n"
            )
            print(f"Expected: {expected}")
            print(f"Generator Output: {actual}")

    try:
        test_step_1()
    except Exception:
        print("step 1 test unable to run")

    try:
        test_step_2()
    except Exception:
        print("step 2 test unable to run")
