# DIT Internship 2026 – HR Recruitment Automation System (Professional Starter)

## Features
- CSV / Excel candidate upload
- Multiple text-based PDF resume parsing (best-effort extraction)
- Candidate data validation: required fields, email, phone, numeric fields, duplicate email
- Configurable job criteria
- Transparent weighted match score: skills 40%, experience 30%, education 15%, notice period 15%
- SQLite screening history and dashboard
- HR review statuses
- Excel and CSV report downloads
- Automated unit tests

## Requirements
- Python 3.10 or newer
- Windows / macOS / Linux

## Windows setup
Open PowerShell in the folder containing `app.py` and `requirements.txt`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

If PowerShell blocks activation, run commands without activating:
```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Run tests
```powershell
python -m pytest -v
```

## Try the sample dataset
Upload `data/sample_candidates.csv` in the app.

## Candidate spreadsheet columns
`candidate_id, full_name, email, phone, education, experience_years, skills, location, notice_period_days, expected_salary, applied_role`

## PDF notes
Upload one or more selectable-text PDF resumes. Scanned PDFs require OCR, which is not included in this starter. Extraction is heuristic and must be reviewed by HR. Missing or uncertain fields should be corrected before screening.

## Responsible use and limitations
This is an internship prototype and decision-support tool, not a production hiring platform. Use synthetic data for demos or real data only with documented authorization and appropriate security controls. Match scores are based only on job-related criteria entered by HR; they are not proof of candidate quality. HR must verify extracted information and make all interview and hiring decisions. Do not use protected characteristics or proxies for them. Do not send confidential resumes to public AI services.

## Suggested demo flow
1. Open the app.
2. Configure role and job criteria in the sidebar.
3. Upload `data/sample_candidates.csv` and/or text-based PDF resumes.
4. Click Process Candidates.
5. Review exceptions, match scores and HR review statuses.
6. Download the Excel report.
7. Show dashboard analytics.
