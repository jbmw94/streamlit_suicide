import pandas as pd
def suicide_df(master):
    df_suicide = pd.read_csv(master)
    df_suicide_2016 = df_suicide[df_suicide["year"]==2016]
    df_suicide_2016[" gdp_for_year ($) "] = df_suicide_2016[" gdp_for_year ($) "].str.replace(',','').astype(float)
    mean_groupby = df_suicide_2016.groupby('country').mean()[['gdp_per_capita ($)', ' gdp_for_year ($) ']]
    

    sum_groupby = df_suicide_2016.drop('suicides/100k pop', axis = 1).groupby('country').sum()[['population', 'suicides_no', 'gdp_per_capita ($)']]

    df_suicide_2016_processed = pd.concat([mean_groupby, sum_groupby], axis=1)

    df_suicide_2016_processed['suicide_rate_per_100k'] = (df_suicide_2016_processed['suicides_no']/df_suicide_2016_processed['population'])*100_000

    df_suicide_2016_processed.to_csv('suicide.csv')
    return df_suicide_2016_processed
