#function that cleans the data by interpolating missing business days for each contract

import pandas as pd
import numpy as np

def interpolate_missing_business_days(df):
    """
    Fill missing business days for each contract in the DataFrame.
    Interpolates 'open', 'high', 'low', 'close' linearly between previous and next business days.
    Orders contracts by numeric maturity extracted from contract_id.

    Parameters
    ----------
    df : pd.DataFrame
        Must contain at least ['contract_id', 'date', 'open', 'high', 'low', 'close'].
    
    Returns
    -------
    pd.DataFrame
        DataFrame with missing business days filled per contract.
    """
        
    df = df.copy()
    df['date'] = pd.to_datetime(df['date'])
    #create a maturity order column based on the numeric part of contract_id (e.g., 'm003' -> 3)
    filled_all = []

    for contract_id in df['contract_id'].unique():
        contract_df = df[df['contract_id'] == contract_id].sort_values('date').reset_index(drop=True)
        
        #list of all business days between min and max date in the df -> missing dates will be the ones not in this list
        full_dates = pd.date_range(contract_df['date'].min(), contract_df['date'].max(), freq='B')
        missing_dates = full_dates.difference(contract_df['date'])
        
        rows_to_add = []

        for missing_date in missing_dates:
            #get previous and next date wrt to the missing date
            prev_rows = contract_df[contract_df['date'] < missing_date]
            next_rows = contract_df[contract_df['date'] > missing_date]

            if prev_rows.empty or next_rows.empty:
                continue
            
            prev_row = prev_rows.iloc[-1]
            next_row = next_rows.iloc[0]
            #interpolate linearly the values for the m# compute number of business days between prev and next
            #business-day-aware interpolation
            bdays_total = len(pd.bdate_range(prev_row['date'], next_row['date'])) - 1
            bdays_elapsed = len(pd.bdate_range(prev_row['date'], missing_date)) - 1
            interpolated_row = prev_row.copy()
            interpolated_row['date'] = missing_date
            for col in ['open', 'high', 'low', 'close']:
                interpolated_row[col] = prev_row[col] + (next_row[col] - prev_row[col]) * (bdays_elapsed / bdays_total)
            rows_to_add.append(interpolated_row)
        #concat to the original df
        if rows_to_add:
            contract_df = pd.concat([contract_df, pd.DataFrame(rows_to_add)], ignore_index=True)
            contract_df = contract_df.sort_values('date').reset_index(drop=True)

        filled_all.append(contract_df)

    filled_all = pd.concat(filled_all, ignore_index=True).reset_index(drop=True)
    return filled_all

