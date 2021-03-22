from dagster import execute_solid

from dagster_advent_of_code.day_1_pipeline import match_by_sum


def test_match_by_sum():
    input_values = {
        "input_list": [1721, 979, 366, 299, 675, 1456],
        "set_size": 2,
        "match_sum": 2020,
    }
    result = execute_solid(match_by_sum, input_values=input_values)
    assert result.success
    assert result.output_value() == (1721, 299)

    input_values["set_size"] = 3
    result = execute_solid(match_by_sum, input_values=input_values)
    assert result.success
    assert result.output_value() == (979, 366, 675)
