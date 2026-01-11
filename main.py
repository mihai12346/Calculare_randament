import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf


tickers = ["DIGI.RO", "M.RO", "WINE.RO"]
start_date = '2020-01-01'
end_date = '2026-01-01'
data = yf.download(tickers, start=start_date, end=end_date)

log_returns = np.log(data["Close"] / data["Close"].shift(1)).dropna()

weights = np.array([0.6, 0.2, 0.2])


mean_returns = log_returns.mean()
portfolio_mean_return = (np.dot(weights, mean_returns))
annual_return = portfolio_mean_return * 252
print("randamentul")
print(annual_return)
portfolio_returns = np.dot(log_returns,weights)
#vol
portfolio_volatility = portfolio_returns.std() * np.sqrt(252)
vol = portfolio_volatility/ np.sqrt(252)
print("risk")
print(portfolio_volatility)
#matrice de covarianta
cov_matrix = log_returns.cov() * 252
print(cov_matrix)
#sharpe

sharpe = annual_return / portfolio_volatility
print(sharpe)

num_sim = 100
orizont =252

initial_portfolio_value = 10000 

port_mean = np.sum(weights * mean_returns)

port_vol = np.sqrt(np.dot(weights.T, np.dot((cov_matrix/252), weights)))
print(port_vol)
print(f"asta e test {vol:.12f}")
daily_returns_simulated = np.random.normal(port_mean, port_vol, (orizont, num_sim))
#daily_returns_simulated = np.random.normal(portfolio_mean_return, port_vol, (orizont, num_sim))
portfolio_cumulative_returns = (1 + daily_returns_simulated).cumprod(axis=0)
portfolio_values = initial_portfolio_value * portfolio_cumulative_returns

plt.figure(figsize=(11,9))
plt.plot(portfolio_values)
plt.title('Simulare Monte Carlo: 100 de scenarii pentru Portofoliul (1 An)')
plt.xlabel('Zile')
plt.ylabel('Valoare Portofoliu (RON)')
plt.show()


final_values = portfolio_values[-1, :]
print(f"Valoarea medie estimată peste 1 an: {np.mean(final_values):.2f} RON")
print(f"Cel mai prost scenariu (95% incredere): {np.percentile(final_values, 5):.2f} RON")


plt.figure(figsize=(10,6))
plt.hist(final_values, bins=30,alpha=0.7)
plt.axvline(np.mean(final_values), linestyle='--', color='black', label='Media')
plt.axvline(np.percentile(final_values, 5), linestyle='--',color = 'red', label='Percentila 5%')
plt.title('Distribuția valorii finale a portofoliului (1 an)')
plt.xlabel('Valoare portofoliu (RON)')
plt.ylabel('Frecvență')
plt.legend()
plt.show()



weights_var = np.array([0.0, 0.0, 0.0])
nume_firme = np.array(["Digi","Medlife","Purcari"])
for i in range (3) :
    weights_var[i] = 1.0
    p100_mean= np.dot(weights_var,mean_returns)
    print('randamentul mediu zilnic '+nume_firme[i])
    print(p100_mean*100)
    print("anual")
    print((p100_mean*252*100))
    return_port100 = np.dot(log_returns,weights_var)
    vol100 = return_port100.std() * np.sqrt(252)
    print(f"Volatilitatea : {(vol100 * 100) :.2f}")
    sharpe100 = (p100_mean*252)/vol100
    print("raport rentabilitate risc ")
    print(sharpe100)
    #Monte carlo
    port_vol_100 =np.sqrt(np.dot(weights_var.T, np.dot((log_returns.cov()), weights_var)))
    sim_return_port100_Zi = np.random.normal(p100_mean,port_vol_100,(orizont,num_sim))
    cum_prod = (1 + sim_return_port100_Zi).cumprod(axis = 0 )
    port_value100 = initial_portfolio_value * cum_prod
    plt.figure(figsize=(11,9))
    plt.plot(port_value100)
    plt.title('Simulare Monte Carlo : 100 de scenarii pentru Portofoliul (1 An) la firma '+nume_firme[i])
    plt.xlabel('Zile')
    plt.ylabel('Valoare Portofoliu (RON)')
    plt.show()
    tot_values = port_value100[-1,:]
    
    print(f"Valoarea medie estimată peste 1 an: {np.mean(tot_values):.2f} RON {nume_firme[i]}")
    print(f"Cel mai prost scenariu (95% incredere): {np.percentile(tot_values, 5):.2f} RON {nume_firme[i]}")

    plt.figure(figsize=(10,6))
    plt.hist(tot_values, bins=30,alpha=0.7)
    plt.axvline(np.mean(tot_values), linestyle='--', color='black', label='Media')
    plt.axvline(np.percentile(tot_values, 5), linestyle='--',color = 'red', label='Percentila 5%')
    plt.title('Distribuția valorii finale a portofoliului (1 an) la firrma ' + nume_firme[i])
    plt.xlabel('Valoare portofoliu (RON)')
    plt.ylabel('Frecvență')
    plt.legend()
    plt.show()
    print(weights_var)
    weights_var [i] = 0.0
    

    
