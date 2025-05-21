"""
# Vysvětlení novinek

1. @pytest.fixture()	
    Funkce calc() se spustí před KAŽDÝM testem, vrátí instanci kalkulačky ⇒ zachová se izolace testů.

2. @pytest.mark.parametrize
	Jedna test-funkce, ale vstupní hodnoty tabulkově – testy jsou krátké a přehledné.

3. math.isclose()	
    Elegantní způsob porovnání desetinných čísel (bez nutnosti assertAlmostEqual).

4. pytest.raises(..., match="regex")	
    Ověří, že se vyhodí správná výjimka a obsahuje požadovanou zprávu.

-------------------------------------------------------------------


# Spouštění a filtry
pytest -q                        # tichý výstup (. = ok, F = fail)
pytest -v                        # verbose – vy­pi­še názvy
pytest tests/test_kalkulacka.py::test_secti[1-1-2]   # jeden konkrétní parametr
pytest -k "vynasob or vydel"     # spustí jen vybrané testy podle podřetězce


-------------------------------------------------------------------

## Pytest Markery

**Markery** jsou štítky, kterými můžete označovat testy a poté je cíleně spouštět nebo vynechávat.

### 1. Deklarace vlastních markerů

V souboru `pytest.ini` přidejte sekci `markers`:

```ini
[pytest]
markers =
  edge: test hraničních (edge) vstupů jako ∞, NaN, extrémní int
  slow: testy, které běží dlouho
```

Tím předejdete varováním `PytestUnknownMarkWarning`.

### 2. Označení testů markerem

V testovacím souboru jednoduše přidejte dekorátor:

```python
import pytest

@pytest.mark.edge
def test_inf_division():
    assert calculate(1, float('inf')) == 0
```

### 3. Spouštění dle markerů

* Spustit pouze označené testy:

  ```bash
  pytest -m edge
  ```
* Spustit všechny kromě označených:

  ```bash
  pytest -m "not edge"
  ```

### 4. Přeskakování uvnitř testu

V rámci testu můžete vynechat některé případy:

```python
import pytest, math

@pytest.mark.edge
@pytest.mark.parametrize("a,b", [(math.inf, 0), (1, 0)])
def test_divide(a, b):
    if math.isinf(a) and b == 0:
        pytest.skip("nelogická kombinace ∞ / 0")
    with pytest.raises(ValueError):
        divide(a, b)
```

---

*Rychlý přehled markerů pro úpravu a cílené spouštění vašich testů.*


----------------------------------------------