import pytest

# Specify the test directory and options you want to use with pytest
def run_tests():
    # Run pytest programmatically
    pytest.main([
        "testCases/",               # The test directory you want to run
        "--html=Reports/report.html",  # Generate the HTML report
        "--self-contained-html",      # Self-contained HTML report (useful for sharing)
        "--capture=tee-sys"           # Capture stdout and stderr
    ])

if __name__ == "__main__":
    run_tests()
