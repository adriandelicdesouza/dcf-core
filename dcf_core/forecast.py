def project_revenue(previous_revenue: float, growth_rate: float) -> float:
    return previous_revenue * (1 + growth_rate)


def calculate_ebit(revenue: float, ebit_margin: float) -> float:
    return revenue * ebit_margin


def calculate_taxes(ebit: float, tax_rate: float) -> float:
    return ebit * tax_rate


def calculate_nopat(ebit: float, tax_rate: float) -> float:
    return ebit * (1 - tax_rate)


def calculate_d_and_a(revenue: float, d_and_a_percent: float) -> float:
    return revenue * d_and_a_percent


def calculate_capex(revenue: float, capex_percent: float) -> float:
    return revenue * capex_percent


def calculate_nwc(revenue: float, nwc_percent: float) -> float:
    return revenue * nwc_percent


def calculate_change_in_nwc(
    current_nwc: float,
    previous_nwc: float,
) -> float:
    return current_nwc - previous_nwc


def calculate_ufcf(
    nopat: float,
    d_and_a: float,
    capex: float,
    change_in_nwc: float,
) -> float:
    return nopat + d_and_a - capex - change_in_nwc