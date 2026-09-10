from dcf_core.forecast import (
    project_revenue,
    calculate_ebit,
    calculate_taxes,
    calculate_nopat,
    calculate_d_and_a,
    calculate_capex,
    calculate_nwc,
    calculate_change_in_nwc,
    calculate_ufcf,
)


def test_project_revenue():
    assert project_revenue(1000, 0.10) == 1100


def test_calculate_ebit():
    assert calculate_ebit(1100, 0.15) == 165


def test_calculate_taxes():
    assert calculate_taxes(165, 0.25) == 41.25


def test_calculate_nopat():
    assert calculate_nopat(165, 0.25) == 123.75


def test_calculate_d_and_a():
    assert calculate_d_and_a(1100, 0.03) == 33


def test_calculate_capex():
    assert calculate_capex(1100, 0.04) == 44


def test_calculate_nwc():
    assert calculate_nwc(1100, 0.02) == 22


def test_calculate_change_in_nwc():
    assert calculate_change_in_nwc(22, 20) == 2


def test_calculate_ufcf():
    assert calculate_ufcf(
        nopat=123.75,
        d_and_a=33,
        capex=44,
        change_in_nwc=2,
    ) == 110.75