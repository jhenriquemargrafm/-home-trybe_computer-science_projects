from src.sorting import sort_by


def test_sort_by_criteria():
    pass
    jobs = [
        {'max_salary': 25, 'min_salary': 15, 'date_posted': '2021-12-01'},
        {'max_salary': 50, 'min_salary': 2, 'date_posted': '2021-12-02'},
        {'max_salary': 100, 'min_salary': 10, 'date_posted': '2021-12-03'},
    ]
    sort_by(jobs, 'max_salary')
    assert jobs == [
        {'max_salary': 100, 'min_salary': 10, 'date_posted': '2021-12-03'},
        {'max_salary': 50, 'min_salary': 2, 'date_posted': '2021-12-02'},
        {'max_salary': 25, 'min_salary': 15, 'date_posted': '2021-12-01'},
    ]

    sort_by(jobs, 'min_salary')
    assert jobs == [
        {'max_salary': 50, 'min_salary': 2, 'date_posted': '2021-12-02'},
        {'max_salary': 100, 'min_salary': 10, 'date_posted': '2021-12-03'},
        {'max_salary': 25, 'min_salary': 15, 'date_posted': '2021-12-01'},
    ]
