from src.jobs import read


def get_unique_job_types(path):
    list_CSV = read(path)
    job_types = set()
    for item in list_CSV:
        for job in item["job_type"].split(","):
            job_types.add(job)
    return job_types


def filter_by_job_type(jobs, job_type):
    jobs_filtered = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobs_filtered.append(job)
    return jobs_filtered


def get_unique_industries(path):
    list_CSV = read(path)
    industries = set()
    for item in list_CSV:
        industry = item["industry"]
        if industry != "":
            industries.add(industry)
    return industries


def filter_by_industry(jobs, industry):
    industry_filtered = []
    for job in jobs:
        if job['industry'] == industry:
            industry_filtered.append(job)
    return industry_filtered


def get_max_salary(path):
    list_CSV = read(path)
    max_salary = 0
    for item in list_CSV:
        if (
            item["max_salary"] != ""
            and item["max_salary"] != "invalid"
            and int(item["max_salary"]) > max_salary
        ):
            max_salary = int(item["max_salary"])
    return max_salary


def get_min_salary(path):
    list_CSV = read(path)
    min_salary = 100000000
    for item in list_CSV:
        if (
            item["min_salary"] != ""
            and item["min_salary"] != "invalid"
            and int(item["min_salary"]) < min_salary
        ):
            min_salary = int(item["min_salary"])
    return min_salary


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Salários não existem")
    elif (
        not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or not isinstance(salary, int)
    ):
        raise ValueError("entradas são inválidas")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary não pode que ser maior que max_salary")
    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    salary_filtered = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary_filtered.append(job)
        except ValueError:
            pass
        return salary_filtered
