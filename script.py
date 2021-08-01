import pandas as pd

def main():
    df = pd.read_csv('source.csv')


    # Remove spaces
    df = df.replace('\n',' ', regex=True)
  
    # Added Year column
    new_df = df.assign(Year='2018')

    new_df.loc[:, ['Country', 'Area', 'Population', 'GDP per capita','Population density','Vehicle ownership','Total Road Deaths','Road deaths per Million Inhabitants', 'Year']]

    # Sort by Road deaths per Million Inhabitants
    new_df = new_df.sort_values(['Road deaths per Million Inhabitants'])
    

    # Write new_df to csv
    new_df.dropna().to_csv('result.csv', sep=',', index=False)
    

if __name__ == '__main__':
    main()