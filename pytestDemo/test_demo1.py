#Any pytest file should start with test_ or end with _test
#Pytest method names should start with test
#Any code should be wrapped in method only
#Method name Should have same
# -k stands for method names execution, -s logs in output -v stands for more info metadata
#you can run specific file with pytest <filename>
#you can mark(tag) tests @pytest.mark.smoke and then run with -m
#you can skip test with @pytest.mark.skip
#@pytest.mark.xfail
#fixture are used as setup and tear down methods for testcases - conftest file to generalize fixture
#and make it available to all testcases(fixtures name into parameters of method)

#datadriven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiated and at the end
import pytest

@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")

@pytest.mark.xfail
def test_secondGreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])