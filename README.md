# Dagster Advent of Code

This project is a proof of concept to attempt to implement some of my solutions from the [2020 Advent of Code](https://adventofcode.com/2020) challenge in the [Dagster](https://docs.dagster.io/) data orchestration framework.

The solutions are ported from my original implementations in this [repo](https://github.com/acviana/advent-of-code-2020/).

Note, to install grpcio with Poetry 1.1.4 and Python 3.8.6 on OSX 11.2.2 you need to set the following flag `export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=true` ([source](https://github.com/grpc/grpc/issues/24677#issuecomment-728721822)).

- 0.0.1: Project setup and working pure Python implementation of Day 1 solution. No Dagster elements
- 0.0.2: Working non-parameterized Dagster pipeline with basic type hints
- 0.0.3: Parameterized Dagster pipeline with YAML configuration files
- 0.0.4: Added pre-commit package and hooks
