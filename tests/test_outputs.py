import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")
REQUIRED_FIELDS = {"total_requests", "unique_ips", "top_path"}


def _load_report():
    """Load the report while producing clear failures for the output contract."""
    assert REPORT_PATH.is_file(), "no report.json found"
    try:
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"report.json is not valid JSON: {exc}") from exc

    assert isinstance(report, dict), "report.json must contain a JSON object"
    return report


def test_output_contract():
    """Criterion 1 (Output contract): exact fields and JSON value types."""
    report = _load_report()

    assert set(report) == REQUIRED_FIELDS, (
        f"report fields must be exactly {sorted(REQUIRED_FIELDS)}, "
        f"got {sorted(report)}"
    )
    assert type(report["total_requests"]) is int, "total_requests must be an integer"
    assert type(report["unique_ips"]) is int, "unique_ips must be an integer"
    assert isinstance(report["top_path"], str), "top_path must be a string"


def test_total_requests():
    """Criterion 2 (Total requests): count every non-empty access-log line."""
    report = _load_report()
    assert report["total_requests"] == 6, "total_requests must equal 6"


def test_unique_clients():
    """Criterion 3 (Unique clients): count distinct first-field IP addresses."""
    report = _load_report()
    assert report["unique_ips"] == 3, "unique_ips must equal 3"


def test_most_popular_path():
    """Criterion 4 (Most popular path): report the most frequent request path."""
    report = _load_report()
    assert report["top_path"] == "/index.html", "top_path must be /index.html"
