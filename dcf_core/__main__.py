from dcf_core.forecast import forecast_ufcf


def main() -> None:
    print("DCF Valuation")
    print("=============")

    starting_revenue = float(input("Starting revenue ($M): "))

    print(f"Starting revenue: ${starting_revenue:.2f}M")

    growth_rates = []

    for year in range(1, 6):
        growth = float(input(f"Year {year} revenue growth (%): "))
        growth_rates.append(growth / 100)

    print(f"Growth rates: {growth_rates}")

    ebit_margins = []

    for year in range(1, 6):
        margin = float(input(f"Year {year} EBIT margin (%): "))
        ebit_margins.append(margin / 100)

    print(f"EBIT margins: {ebit_margins}")

    tax_rate = float(input("Tax rate (%): ")) / 100

    print(f"Tax rate: {tax_rate}")

    da_percent_revenue = float(input("D&A as % of revenue (%): ")) / 100

    print(f"D&A as % of revenue: {da_percent_revenue}")

    capex_percent_revenue = float(input("CapEx as % of revenue (%): ")) / 100

    print(f"CapEx as % of revenue: {capex_percent_revenue}")

    nwc_percent_revenue = float(input("Change in NWC as % of revenue (%): ")) / 100

    ufcfs = forecast_ufcf(
        starting_revenue=starting_revenue,
        growth_rates=growth_rates,
        ebit_margin=ebit_margins[0],
        tax_rate=tax_rate,
        d_and_a_percent=da_percent_revenue,
        capex_percent=capex_percent_revenue,
        nwc_percent=nwc_percent_revenue,
    )

    print("\nForecast UFCF")
    print("=============")

    for year, ufcf in enumerate(ufcfs, start=1):
        print(f"Year {year}: ${ufcf:.2f}M")

    wacc = float(input("WACC (%): ")) / 100

    print(f"WACC: {wacc}")


if __name__ == "__main__":
    main()