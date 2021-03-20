from itertools import combinations
from math import prod
from typing import List, Tuple

from dagster import pipeline, solid  # type: ignore


@solid
def load_data(context, file_path: str) -> List[int]:
    context.log.info(f"Attempting to load data from {file_path}")
    with open(file_path, "r") as f:
        dataset = [int(item.strip()) for item in f.readlines()]
    context.log.info(f"Loaded dataset with {len(dataset)} elements")
    return dataset


@solid
def match_by_sum(
    context, input_list: List[int], set_size: int, match_sum: int
) -> Tuple:
    for combination in combinations(input_list, set_size):
        if sum(combination) == match_sum:
            context.log.info(
                f"Found {set_size} item combination {combination} with sum {match_sum}"
            )
            return combination
    context.log.info(f"Found no {set_size} item combinations with sum {match_sum}")
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
    summerize_result(combination)
