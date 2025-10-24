# Coding Standards Lab (Python)

This workspace contains the deliverables for the Coding Standards lab.

Files:
- `student_original.py` - intentionally messy / non-PEP8 code (input)
- `student_fixed.py` - corrected, PEP8-compliant version
- `requirements.txt` - flake8 and flake8-html
- `.github/workflows/lint.yml` - optional GitHub Actions workflow (bonus)
- `CodingStandards_Report.md` - template for the lab report

How to run locally (PowerShell):

1. Create / activate your virtual environment (optional but recommended):
```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```
2. Install dependencies:
```powershell
pip install -r requirements.txt
```
3. Run flake8 and generate HTML reports (example):
```powershell
flake8 student_original.py --format=html --htmldir=flake8_report_before
flake8 student_fixed.py --format=html --htmldir=flake8_report_after
```

Report: fill `CodingStandards_Report.md` with the before/after findings and screenshots.
