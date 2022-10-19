
from pytest import fixture

from hash_code.Schedule import Schedule, find_solution
from hash_code.Task import CreateEmptyBinary

@fixture
def input_file_name():
    return "tests/input_data_test.txt"

@fixture
def schedule(input_file_name):
    return Schedule.load(input_file_name)

@fixture
def solution_schedule(schedule):
    return find_solution(schedule)


def test_load_schedule_sizes(schedule):

    assert schedule.time_limit == 10
    assert len(schedule.engineers) == 2
    assert len(schedule.services) == 5
    assert len(schedule.binaries) == 3
    assert len(schedule.features) == 2
    assert CreateEmptyBinary.nb_of_days == 5

def test_load_schedule_content(schedule):

    assert schedule.services[2].name == "sc"
    assert schedule.features[1].name == "bar"
    assert schedule.features[1].nb_daily_users == 20
    assert schedule.features[1].difficulty == 1
    assert schedule.features[0].services[1].name == "sb"

def test_find_solution_end_time(solution_schedule):
    assert solution_schedule.end_time < solution_schedule.time_limit
