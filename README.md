# stock_comparison

Got 2 files, with the similar information on daily returns % over one year of ordinary stock and preferred stock same company.
Bancolombia ordinaria y Pfbcolombia from 15 May 2022 to 15 May 2023.

I have done a visualization of relationship between both variables (daily returns of both stocks)

1. Check Relationship throgh Scatter plot of the variables
2. Check distribution through Pair plot
3. Finally check the sample correlation coefficient 
correlation_coef = np.corrcoef(pref_ordi["Variación porcentual_pref"], pref_ordi["Variación porcentual_ordi"])[0, 1]

Correlation coefficient -which only measures linear relationship-: 0.5928866169293966 
Indicates a moderate positive correlation between variables.
As it is moderate. Therefore, it is important to analyze the context and consider other variables or factors before making interpretations.
