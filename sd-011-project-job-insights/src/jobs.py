from functools import lru_cache
import csv


@lru_cache
def read(path):
    result = []
    with open(path, 'r', newline='') as file:
        csvReader = list(csv.DictReader(file))
        for row in csvReader:
            result.append(row)
    return result
