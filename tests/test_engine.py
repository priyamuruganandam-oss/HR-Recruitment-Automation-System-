import pandas as pd
from src.engine import valid_email, validate_candidates, screen_candidates

def sample_row(**updates):
    row = {
        "candidate_id":"T001", "full_name":"Test Candidate", "email":"test@example.com",
        "phone":"9876543210", "education":"Bachelor of Engineering",
        "experience_years":3, "skills":"Python, SQL", "location":"Chennai",
        "notice_period_days":30, "expected_salary":400000, "applied_role":"Python Developer"
    }
    row.update(updates)
    return row

def test_email_validation():
    assert valid_email("person@example.com")
    assert not valid_email("personexample.com")

def test_invalid_candidate_is_exception():
    valid, exceptions = validate_candidates(pd.DataFrame([sample_row(full_name="")]))
    assert len(valid) == 0
    assert len(exceptions) == 1

def test_eligible_candidate_score():
    valid, exceptions = validate_candidates(pd.DataFrame([sample_row()]))
    result = screen_candidates(valid, ["Python","SQL"], 2, ["Bachelor"], 60, 60)
    assert len(result) == 1
    assert result.iloc[0]["match_score"] == 100.0
