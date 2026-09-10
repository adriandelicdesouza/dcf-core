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

def forecast_ufcf(
    starting_revenue: float,
    growth_rates: list[float],
    ebit_margin: float,
    tax_rate: float,
    d_and_a_percent: float,
    capex_percent: float,
    nwc_percent: float,
) -> list[float]:
    revenues = []
    ufcfs = []

    previous_revenue = starting_revenue
    previous_nwc = starting_revenue * nwc_percent

    for growth_rate in growth_rates:
        revenue = project_revenue(previous_revenue, growth_rate)
        ebit = calculate_ebit(revenue, ebit_margin)
        nopat = calculate_nopat(ebit, tax_rate)
        d_and_a = calculate_d_and_a(revenue, d_and_a_percent)
        capex = calculate_capex(revenue, capex_percent)

        nwc = calculate_nwc(revenue, nwc_percent)
        change_in_nwc = calculate_change_in_nwc(nwc, previous_nwc)

        ufcf = calculate_ufcf(
            nopat=nopat,
            d_and_a=d_and_a,
            capex=capex,
            change_in_nwc=change_in_nwc,
        )

        revenues.append(revenue)
        ufcfs.append(ufcf)

        previous_revenue = revenue
        previous_nwc = nwc

    return ufcfs