def describe_city(city, country='Indonesia'):
    """Describe a city and its country."""
    print(f"{city.title()} is in {country.title()}.")

describe_city('jakarta')
describe_city('reykjavik', 'iceland')
describe_city('tokyo', 'japan')