import yfinance as yf
ticks = ["JPM", "BAC", "HSBC", "WFC", "RY", "TD", "C", "MUFG", "BMO", "UBS", "BNS", "SAN", "SMFG", "ING", "BBVA", "CM", "NWG", "BCS", "NU", "EWBC", "CS", "NTB", "SIVB", "SBNY"]
yf.download(ticks, start = "2020-03-01", end = "2023-03-31")["Adj Close"]