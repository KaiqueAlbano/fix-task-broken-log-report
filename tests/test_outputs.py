import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")
EXPECTED_REPORT = {
    "total_requests": 6,
    "unique_ips": 3,
    "top_path": "/index.html",
}


def test_report_exists():
    """The agent produced a report file."""
    assert REPORT_PATH.is_file(), "no report.json found"


def test_report_is_valid_json_object():
    """The report is valid JSON with an object at the top level."""
    try:
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"report.json is not valid JSON: {exc}") from exc

    assert isinstance(report, dict), "report.json must contain a JSON object"


def test_report_has_exact_expected_summary():
    """The report contains the exact schema and values required by the task."""
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    assert report == EXPECTED_REPORT, (
        f"unexpected report contents: expected {EXPECTED_REPORT!r}, got {report!r}"
    )
