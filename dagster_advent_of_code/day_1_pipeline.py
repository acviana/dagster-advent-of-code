from itertools import combinations
from math import prod
from typing import List, Tuple

from dagster import execute_pipeline, pipeline, solid


@solid
def load_data(context) -> List[int]:
    file_path = "data/day_1_input.txt"
    context.log.info(f"Attempting to load data from {file_path}")
    with open(file_path, "r") as f:
        dataset = [int(item.strip()) for item in f.readlines()]
    context.log.info(f"Loaded dataset with {len(dataset)} elements")
    return dataset


@solid
def match_by_sum(context, input_list: List[int]) -> Tuple:
    # , set_size: int, match_sum: int
    set_size = 2
    match_sum = 2020
    for combination in combinations(input_list, set_size):
        if sum(combination) == match_sum:
            context.log.info(f"Found combination {combination} with sum {match_sum}")
            return combination
    context.log.info(f"Found no combinations with sum {match_sum}")
    return ()


@solid
def summerize_result(context, combination: Tuple) -> str:
    result_summery = (
        f"Set: {*combination,}, Sum: {sum(combination)}, Product: {prod(combination)}"
    )
    context.log.info(result_summery)
    return result_summery


@pipeline
def day_1_pipeline():
    data = load_data()
    combination = match_by_sum(data)  # , 2, 2020)
    result_summery = summerize_result(combination)
    # print(summerize_result(combination))

    # combination = match_by_sum_and_multiply(data, 3, 2020)
    # print(summerize_result(combination))


if __name__ == "__main__":
    result = execute_pipeline(day_1_pipeline)
