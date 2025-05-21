# What's New in Our Pytest Suite

This document provides an overview of the latest features and best practices we've introduced to improve our tests.

## 1. Test Fixtures with `@pytest.fixture()`

* The `calc()` fixture runs **before each test**, returning a new calculator instance to ensure test isolation.

## 2. Parameterized Tests with `@pytest.mark.parametrize`

* Define a single test function and supply inputs in a table-like format. This keeps tests concise and easy to read.

## 3. Floating-Point Comparisons with `math.isclose()`

* A clean way to compare decimal numbers without using `assertAlmostEqual`.

## 4. Exception Assertions with `pytest.raises(..., match="regex")`

* Verify that the correct exception is raised and that its message matches a specific pattern.

---

# Running Tests and Applying Filters

* `pytest -q`
  Runs in quiet mode (`.` = pass, `F` = fail).
* `pytest -v`
  Verbose mode, prints full test names.
* `pytest tests/test_calculator.py::test_add[1-1-2]`
  Run a single parameterized case.
* `pytest -k "multiply or divide"`
  Run only tests whose names match the given substring.

---

## Pytest Markers

Markers let you tag tests so you can include or exclude them during test runs.

### 1. Declaring Custom Markers

Add your markers under the `markers` section in `pytest.ini`:

```ini
[pytest]
markers =
  edge: mark tests for edge cases (∞, NaN, extreme ints)
  slow: mark tests that take a long time to run
```

This prevents `PytestUnknownMarkWarning`.

### 2. Tagging Tests with Markers

Use the decorator in your test file:

```python
import pytest

@pytest.mark.edge
def test_inf_division():
    assert calculate(1, float('inf')) == 0
```

### 3. Running Tests by Marker

* Run only marked tests:

  ```bash
  pytest -m edge
  ```
* Exclude a marker:

  ```bash
  pytest -m "not edge"
  ```

### 4. Skipping Specific Cases at Runtime

You can skip certain parameter combinations within a test:

```python
import pytest, math

@pytest.mark.edge
@pytest.mark.parametrize("a,b", [(math.inf, 0), (1, 0)])
def test_divide(a, b):
    if math.isinf(a) and b == 0:
        pytest.skip("Skipping invalid ∞ / 0 combination")
    with pytest.raises(ValueError):
        divide(a, b)
```

---

*Quick reference to help you organize and run your tests efficiently using pytest markers.*
