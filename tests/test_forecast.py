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
    forecast_ufcf,
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

def test_forecast_ufcf():
    ufcfs = forecast_ufcf(
        starting_revenue=1000,
        growth_rates=[0.10, 0.08, 0.06, 0.05, 0.04],
        ebit_margins=[0.15, 0.15, 0.15, 0.15, 0.15],
        tax_rates=[0.25, 0.25, 0.25, 0.25, 0.25],
        d_and_a_percents=[0.03, 0.03, 0.03, 0.03, 0.03],
        capex_percents=[0.04, 0.04, 0.04, 0.04, 0.04],
        nwc_percents=[0.02, 0.02, 0.02, 0.02, 0.02],
    )

    assert len(ufcfs) == 5

    assert round(ufcfs[0], 2) == 90.75
    assert round(ufcfs[1], 2) == 120.01
    assert round(ufcfs[2], 2) == 127.65
    assert round(ufcfs[3], 2) == 134.27
    assert round(ufcfs[4], 2) == 139.89