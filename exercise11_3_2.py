from exercise11_3_1 import Employee


def test_give_default_raise():
    """Test that a default raise of $5,000 works."""
    employee = Employee('budi', 'santoso', 50000)
    employee.give_raise()
    assert employee.annual_salary == 55000


def test_give_custom_raise():
    """Test that a custom raise works."""
    employee = Employee('siti', 'rahma', 60000)
    employee.give_raise(10000)
    assert employee.annual_salary == 70000