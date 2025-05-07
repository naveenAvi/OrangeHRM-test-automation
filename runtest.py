import pytest

def run_tests():
    pytest.main([
        "testCases/",              
        "--html=Reports/report.html",  
        "--self-contained-html",      
        "--capture=tee-sys"           
    ])

if __name__ == "__main__":
    run_tests()
