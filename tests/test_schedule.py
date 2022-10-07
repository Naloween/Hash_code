
from pytest import fixture

from hash_code.Schedule import Schedule

@fixture
def input_file_name():
    return "input_data_test.txt"

def test_load_schedule(input_file_name):
    Schedule.load(input_file_name)
