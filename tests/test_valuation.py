import pytest
from pytest import approx
from dcf_core.valuation import (
    discount_factor,
    present_value,
    terminal_value,
    present_value_terminal_value,
)

def test_terminal_value():
    assert terminal_value(
        final_ufcf=100,
        terminal_growth=0.03,
        wacc=0.10,
    ) == approx(1471.43)


def test_terminal_value_rejects_invalid_growth():
    with pytest.raises(ValueError):
        terminal_value(
            final_ufcf=100,
            terminal_growth=0.10,
            wacc=0.10,
        )


def test_present_value_terminal_value():
    assert present_value_terminal_value(
        terminal_value=1471.43,
        wacc=0.10,
        final_period=5,
    ) == approx(913.64, abs=0.01)

def test_discount_factor():
    assert round(discount_factor(0.10, 1), 4) == 0.9091


def test_present_value():
    assert round(present_value(100, 0.10, 1), 2) == 90.91