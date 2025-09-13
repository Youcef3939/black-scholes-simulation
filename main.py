from black_scholes import black_scholes_call, black_scholes_put

# parameters
S = 100      # current stock price
K = 105      # strike price
T = 1        # time to maturity in years
r = 0.05     # risk-free interest rate
sigma = 0.2  # volatility

print("=== Black–Scholes ===")
print("Call price:", black_scholes_call(S, K, T, r, sigma))
print("Put price: ", black_scholes_put(S, K, T, r, sigma))
