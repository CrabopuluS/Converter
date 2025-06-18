from pathlib import Path
import subprocess
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_help_output():
    result = subprocess.run([
        sys.executable,
        str(PROJECT_ROOT / 'converter.py'),
        '--help'
    ], capture_output=True, text=True)
    assert result.returncode == 0
    assert 'pdf2docx' in result.stdout

