"""test_3 - the third test as part of the ministry of justice take home code assessment"""

from datetime import datetime

# [TODO]: fix the function


def sum_current_time(time_str: str) -> int:
    """
    Expects data in the format HH:MM:SS

    Argument:
        time_str (str): A string representing time in the format HH:MM:SS

    Returns:
        int: Sum of numbers present in the input argument

    Raises:
        TypeError: If input argument is not of type str.
        ValueError: If input argument contains inappropriate data 
    """

    if not isinstance(time_str, str):
        raise TypeError("Input argument must be in str format!")

    list_of_nums = time_str.split(":")

    if len(list_of_nums) != 3:
        raise ValueError("Invalid data in input argument")

    summed_time = 0

    for index, num in enumerate(list_of_nums):
        num = int(num)

        if num < 0:
            raise ValueError("Invalid data in input argument")

        if index == 0 and num > 24:
            raise ValueError("Invalid data in input argument")

        if index != 0 and num > 60:
            raise ValueError("Invalid data in input argument")

        summed_time += num
    return summed_time


if __name__ == "__main__":
    time_str = datetime.now().strftime("%H:%M:%S")
    sum = sum_current_time(time_str)
    print(f"Input String: {time_str}\nOutput Sum: {sum}")
