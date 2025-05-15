import pandas as pd

def reconcile_price(new_price):
    # Load the CSV file
    df = pd.read_csv('/Users/vinumihewamadduma/Desktop/Vinumi EY TEST/stock_data.csv')

    #Filter rows for Apple Inc
    aapl_data = df[df['Company'] == 'AAPL']

    if aapl_data.empty:
        print("No stored price found for AAPL in the dataset.")
        return
    
    #Get stored price
    stored_price= aapl_data.iloc[0]['Price']

    #Calculate price difference and percentage change
    difference = new_price-stored_price
    percentage_change = (difference/stored_price)* 100

    #Print the results
    print(f"stored price: ${stored_price}")
    print(f"new scrapped price: ${new_price}")
    print(f"difference: ${difference:.2f}")
    print(f"percentage change: ${percentage_change:.2f}%")

#example
if __name__ == "__main__":
    new_scrapped_price = 5888.52
    reconcile_price(new_scrapped_price)