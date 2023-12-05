#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def correlated_random_walk(steps, start_price, drift, volatility, correlation,day,gap):
    """
    Simulate a correlated random walk.
    
    Parameters:
        steps (int): Number of steps to simulate.
        start_price (float): Initial price of the instrument.
        drift (float): Expected return per step.
        volatility (float): Expected volatility or standard deviation of returns.
        correlation (float): Correlation factor with the previous step.
    Returns:
        list: A list of simulated prices.
    """
    prices = [start_price]
    last_return = 0

    for i in range(steps - 1):
        filtered_a = a[(a['day_of_week'] == day) & (a['gap'] >= gap)]
        selected_rows = drift_table.loc[filtered_a['date']]
        rand_return = np.random.normal(abs(selected_rows.iloc[:,i].mean()), selected_rows.iloc[:,i].std())
        column_consecutive_minutes = combined_pivot['Consecutive_Minutes'].iloc[:, i]
        correlated_return = (1/ column_consecutive_minutes.mean()) * last_return + (1 - (1/ column_consecutive_minutes.mean())) * rand_return
    
        new_price = prices[-1] + prices[-1] * correlated_return
        prices.append(new_price)

        last_return = correlated_return

    return prices

