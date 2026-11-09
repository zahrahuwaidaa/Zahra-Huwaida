import pytest
from exercise11_3_1 import Employee


@pytest.fixture
def employee():
    """Create a sample employee for testing."""
    return Employee('budi', 'santoso', 50000)


def test_give_default_raise(employee):
    """Test that a default raise of $5,000 works."""
    employee.give_raise()
    assert employee.annual_salary == 55000


def test_give_custom_raise(employee):
    """Test that a custom raise works."""
    employee.give_raise(10000)
    assert employee.annual_salary == 60000