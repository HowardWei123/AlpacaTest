import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ-API-KEY")
)

completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "system",
            "content":"""
            You are helping me with my financial goals providing analysis and suggestions based on my financial portfolio and the stock data, both provided below. 
            Do not pose any suggestions as financial advice, just possible actions.
            
            \n\n\n\nStart by providing some analysis using bullet points LABELED WITH WHAT IS BEING ANALYZED,. Each of the following questions is in its own section of bullet points. 
            Then, in each section, provide a subcategory with some suggestions (not financial advice, just possible actions that align with financial goals) as sub-bullet points 
            within the subcategory that are related to the bullet points in that section.
            \nExample Output to Answer one of the Following Questions: 
            \n**Portfolio Health Analysis:**\n- **Sector Coverage:** The portfolio includes ESG funds, renewable energy, consumer goods, and bonds.
            \n- **Risk Exposure:** Heavy allocation towards renewable energy and ESG sectors may expose the portfolio to sector-specific volatility and regulatory risks.
            \n- **Market Dependence:** Market downturns could heavily impact growth stocks like Tesla, which are more sensitive to economic cycles than bonds or cash.
            \n- **Suggestions:**\n- Consider diversifying by adding sectors like healthcare or technology, which can balance potential sector-specific risks.
            \n- Monitor and adjust renewable energy allocations as regulatory landscapes shift.
            
            \n\n\nFinally, print a paragraph summary of the analysis and some suggestions (not financial advice, just possible actions) going forward that are specific 
            to my financial goals and based on analysis from the data below.
            \nExample Final Summary Paragraph:
            \n**Summary:** The portfolio is moderately diversified across ESG, renewable energy, and consumer goods sectors, with a balanced 7%% annual return 
            that slightly underperforms the S&P 500. Risk exposure is moderate, rated around 6, due to renewable energy holdings, with bonds providing some stability. 
            Expanding into sectors like healthcare or information technology could enhance diversification and growth potential. 
            Rebalancing is recommended to reduce high-volatility stocks and reinforce stability with defensive assets. 
            To manage costs, reducing trade frequency and considering commission-free options is suggested. Lastly, focusing on a long-term strategy can mitigate emotional 
            investing tendencies, aligning investments with structured goals in sustainable sectors.
            
            \n\n\nDO NOT RECOMMEND STOCKS TO PURCHASE. DO NOT WRITE ANY EXTRA COMMENTARY WHATSOEVER.
            \n\n\n1. Give me a portfolio health analysis, covering what sectors my portfolio covers and what risks there may be with my stocks and the market. 
            \n\n\n2. Go over risk assessment and mitigation, covering risk exposure and how I would be able to lower risks. Cover how high my risk is on a scale of 1-10 and explain. 
            \n\n\n3. Go over sector-based investment recommendations, going over what sectors I should invest in more based on my portfolio and where strong growth potential could be. 
            \n\n\n4. Go over performance benchmarking while not giving stock recommendations. Explain what my 12-month return is and if it is underperforming or overperforming compared to the S&P 500. Only use the most recent S&P 500 stock data that is provided below (SPY).
            \n\n\n5. Go over some rebalancing alerts, discussing how my profile may be too heavily weighted towards one sector and how it would be advised to reallocate to be more stable. Include some other sectors I could invest in to stabilize it.
            \n\n\n6. Give some cost-effective trading advice on how to optimize profits and minimize current costs based on my portfolio. 
            \n\n\n7. discuss emotional investment analysis. For example, investments could be made because of FOMO (fear of missing out), decisions based on fear instead of strategy, attachments to stocks (ignoring performance), and other emotionally driven reasons. Explain some possibilities of these and give advice.
            """
        },
        {
            "role": "user",
            "content": """
            \n\n\nFinancial Portfolio:
            \n\tPortfolio Composition:
            \n\t\t30% Real Estate (Direct Property or REITs)
            \n\t\t25% Private Equity or Venture Capital
            \n\t\t20% Stocks (Large-cap, International, Emerging Markets)
            \n\t\t15% Bonds
            \n\t\t10% Alternative Investments (Art, Commodities, Hedge Funds)
            \n\tStocks Held
            \n\t\tBerkshire Hathaway (BRK.B) - A diversified holding company.
            \n\t\tJohnson & Johnson (JNJ) - Stable dividend payer with a strong brand.
            \n\t\tAlphabet Inc. (GOOGL) - Investment in tech with growth potential.
            \n\t\tVisa Inc. (V) - Financial services with solid growth prospects.
            \n\tMetrics
            \n\t\tGains and losses: +10%% annual gain
            \n\t\tFrequency of transactions: Quarterly, around 10 transactions per year
            \n\t\tStock-specific gains and losses:
            \n\t\t\tBRK.B: +8%%
            \n\t\t\tJNJ: +6%%
            \n\t\t\tGOOGL: +12%%
            \n\t\t\tV: +10%%
            \n\tIndustries of invested stocks: Financial Services, Technology, Healthcare
            \n\tEmotion involved: Low; decisions are well-planned, with little reaction to market fluctuations.
            \n\tGoals: Preserve and grow wealth, diversify across asset classes
            
            \n\n\nMonthly Stock Bar Data from October 2023 to October 2024:
            \nData for SPY:
            \nsymbol='SPY' timestamp=datetime.datetime(2023, 10, 1, 4, 0, tzinfo=TzInfo(UTC)) open=426.62 high=438.14 low=409.21 close=418.2 volume=1999352317.0 trade_count=14396248.0 vwap=425.225192
            \nsymbol='SPY' timestamp=datetime.datetime(2023, 11, 1, 4, 0, tzinfo=TzInfo(UTC)) open=419.2 high=458.32 low=418.6499 close=456.4 volume=1500345293.0 trade_count=10625022.0 vwap=443.259471
            \nsymbol='SPY' timestamp=datetime.datetime(2023, 12, 1, 5, 0, tzinfo=TzInfo(UTC)) open=455.77 high=477.55 low=454.31 close=475.31 volume=1644457511.0 trade_count=10405014.0 vwap=467.002748
            \nsymbol='SPY' timestamp=datetime.datetime(2024, 1, 1, 5, 0, tzinfo=TzInfo(UTC)) open=472.16 high=491.62 low=466.43 close=482.88 volume=1700467173.0 trade_count=11444098.0 vwap=478.106674
            \nsymbol='SPY' timestamp=datetime.datetime(2024, 2, 1, 5, 0, tzinfo=TzInfo(UTC)) open=484.63 high=510.13 low=483.8 close=508.08 volume=1393523106.0 trade_count=10501089.0 vwap=498.776892
            \nsymbol='SPY' timestamp=datetime.datetime(2024, 3, 1, 5, 0, tzinfo=TzInfo(UTC)) open=508.98 high=524.61 low=504.91 close=523.07 volume=1474556175.0 trade_count=10998850.0 vwap=515.299571
            \nsymbol='SPY' timestamp=datetime.datetime(2024, 4, 1, 4, 0, tzinfo=TzInfo(UTC)) open=523.83 high=524.38 low=493.86 close=501.98 volume=1593191488.0 trade_count=13405768.0 vwap=509.556514
            \nsymbol='SPY' timestamp=datetime.datetime(2024, 5, 1, 4, 0, tzinfo=TzInfo(UTC)) open=501.38 high=533.07 low=499.55 close=527.37 volume=1153554057.0 trade_count=9384133.0 vwap=520.495667
            \nsymbol='SPY' timestamp=datetime.datetime(2024, 6, 1, 4, 0, tzinfo=TzInfo(UTC)) open=529.02 high=550.28 low=522.6 close=544.22 volume=888703716.0 trade_count=7206259.0 vwap=540.290544
            \nsymbol='SPY' timestamp=datetime.datetime(2024, 7, 1, 4, 0, tzinfo=TzInfo(UTC)) open=545.63 high=565.16 low=537.45 close=550.81 volume=1038489736.0 trade_count=8875961.0 vwap=551.709082
            \nsymbol='SPY' timestamp=datetime.datetime(2024, 8, 1, 4, 0, tzinfo=TzInfo(UTC)) open=552.57 high=564.2 low=510.27 close=563.68 volume=1244598926.0 trade_count=11020334.0 vwap=541.78697
            \nsymbol='SPY' timestamp=datetime.datetime(2024, 9, 1, 4, 0, tzinfo=TzInfo(UTC)) open=560.47 high=574.71 low=539.44 close=573.76 volume=1045159530.0 trade_count=9511932.0 vwap=559.749023
            \nsymbol='SPY' timestamp=datetime.datetime(2024, 10, 1, 4, 0, tzinfo=TzInfo(UTC)) open=573.4 high=586.12 low=565.27 close=568.64 volume=976134821.0 trade_count=9347479.0 vwap=576.573781
            \nsymbol='SPY' timestamp=datetime.datetime(2024, 11, 1, 4, 0, tzinfo=TzInfo(UTC)) open=571.32 high=575.55 low=570.62 close=571.04 volume=45667533.0 trade_count=464571.0 vwap=572.658516
            \n\nData for BRK.B:
            \nsymbol='BRK.B' timestamp=datetime.datetime(2023, 10, 1, 4, 0, tzinfo=TzInfo(UTC)) open=349.64 high=350.0 low=330.58 close=341.33 volume=64981496.0 trade_count=1383133.0 vwap=342.113555
            \nsymbol='BRK.B' timestamp=datetime.datetime(2023, 11, 1, 4, 0, tzinfo=TzInfo(UTC)) open=341.21 high=363.1919 low=340.58 close=360.0 volume=66630106.0 trade_count=1384016.0 vwap=354.09946
            \nsymbol='BRK.B' timestamp=datetime.datetime(2023, 12, 1, 5, 0, tzinfo=TzInfo(UTC)) open=359.94 high=364.05 low=350.85 close=356.66 volume=70954140.0 trade_count=1441012.0 vwap=356.7685
            \nsymbol='BRK.B' timestamp=datetime.datetime(2024, 1, 1, 5, 0, tzinfo=TzInfo(UTC)) open=356.32 high=387.92 low=355.94 close=383.74 volume=73467728.0 trade_count=1559979.0 vwap=370.156276
            \nsymbol='BRK.B' timestamp=datetime.datetime(2024, 2, 1, 5, 0, tzinfo=TzInfo(UTC)) open=384.0 high=430.0 low=381.475 close=409.4 volume=72797009.0 trade_count=1709075.0 vwap=403.668563
            \nsymbol='BRK.B' timestamp=datetime.datetime(2024, 3, 1, 5, 0, tzinfo=TzInfo(UTC)) open=409.48 high=421.44 low=398.78 close=420.52 volume=72549178.0 trade_count=1574678.0 vwap=408.031214
            \nsymbol='BRK.B' timestamp=datetime.datetime(2024, 4, 1, 4, 0, tzinfo=TzInfo(UTC)) open=421.49 high=424.52 low=395.661 close=396.73 volume=63887005.0 trade_count=1590485.0 vwap=407.988068
            \nsymbol='BRK.B' timestamp=datetime.datetime(2024, 5, 1, 4, 0, tzinfo=TzInfo(UTC)) open=396.61 high=417.33 low=396.35 close=414.4 volume=68082334.0 trade_count=1528065.0 vwap=408.16813
            \nsymbol='BRK.B' timestamp=datetime.datetime(2024, 6, 1, 4, 0, tzinfo=TzInfo(UTC)) open=414.89 high=417.0 low=403.33 close=406.8 volume=78704799.0 trade_count=1452591.0 vwap=409.226719
            \nsymbol='BRK.B' timestamp=datetime.datetime(2024, 7, 1, 4, 0, tzinfo=TzInfo(UTC)) open=408.09 high=449.25 low=403.82 close=438.5 volume=79773873.0 trade_count=1708480.0 vwap=427.512351
            \nsymbol='BRK.B' timestamp=datetime.datetime(2024, 8, 1, 4, 0, tzinfo=TzInfo(UTC)) open=439.67 high=476.95 low=406.11 close=475.92 volume=86490268.0 trade_count=1835932.0 vwap=442.008624
            \nsymbol='BRK.B' timestamp=datetime.datetime(2024, 9, 1, 4, 0, tzinfo=TzInfo(UTC)) open=475.0 high=484.82 low=445.25 close=460.26 volume=86547115.0 trade_count=1837869.0 vwap=459.736191
            \nsymbol='BRK.B' timestamp=datetime.datetime(2024, 10, 1, 4, 0, tzinfo=TzInfo(UTC)) open=459.11 high=467.8393 low=450.57 close=450.92 volume=74184206.0 trade_count=1628556.0 vwap=458.667422
            \nsymbol='BRK.B' timestamp=datetime.datetime(2024, 11, 1, 4, 0, tzinfo=TzInfo(UTC)) open=451.49 high=455.12 low=437.9 close=442.29 volume=8704741.0 trade_count=212427.0 vwap=445.489833
            \n\nData for GOOGL:
            \nsymbol='GOOGL' timestamp=datetime.datetime(2023, 10, 1, 4, 0, tzinfo=TzInfo(UTC)) open=131.21 high=141.22 low=120.2057 close=124.08 volume=681123927.0 trade_count=7768771.0 vwap=132.577712
            \nsymbol='GOOGL' timestamp=datetime.datetime(2023, 11, 1, 4, 0, tzinfo=TzInfo(UTC)) open=124.07 high=139.42 low=123.715 close=132.53 volume=536826114.0 trade_count=5631913.0 vwap=133.025049
            \nsymbol='GOOGL' timestamp=datetime.datetime(2023, 12, 1, 5, 0, tzinfo=TzInfo(UTC)) open=131.86 high=142.68 low=127.9 close=139.69 volume=620089435.0 trade_count=6433461.0 vwap=135.13123
            \nsymbol='GOOGL' timestamp=datetime.datetime(2024, 1, 1, 5, 0, tzinfo=TzInfo(UTC)) open=138.55 high=153.78 low=135.15 close=140.1 volume=581907078.0 trade_count=7086192.0 vwap=143.921579
            \nsymbol='GOOGL' timestamp=datetime.datetime(2024, 2, 1, 5, 0, tzinfo=TzInfo(UTC)) open=142.12 high=149.44 low=135.41 close=138.46 volume=647510427.0 trade_count=8083748.0 vwap=141.946549
            \nsymbol='GOOGL' timestamp=datetime.datetime(2024, 3, 1, 5, 0, tzinfo=TzInfo(UTC)) open=138.43 high=152.256 low=130.665 close=150.93 volume=673168428.0 trade_count=8182172.0 vwap=141.505307
            \nsymbol='GOOGL' timestamp=datetime.datetime(2024, 4, 1, 4, 0, tzinfo=TzInfo(UTC)) open=150.69 high=174.71 low=149.6 close=162.78 volume=659869364.0 trade_count=8283280.0 vwap=158.497406
            \nsymbol='GOOGL' timestamp=datetime.datetime(2024, 5, 1, 4, 0, tzinfo=TzInfo(UTC)) open=164.3 high=178.77 low=163.05 close=172.5 volume=542248194.0 trade_count=6858252.0 vwap=171.097346
            \nsymbol='GOOGL' timestamp=datetime.datetime(2024, 6, 1, 4, 0, tzinfo=TzInfo(UTC)) open=172.54 high=186.05 low=171.16 close=182.15 volume=460848567.0 trade_count=5803780.0 vwap=177.877329
            \nsymbol='GOOGL' timestamp=datetime.datetime(2024, 7, 1, 4, 0, tzinfo=TzInfo(UTC)) open=183.03 high=191.75 low=164.06 close=171.54 volume=526148198.0 trade_count=8626277.0 vwap=179.012123
            \nsymbol='GOOGL' timestamp=datetime.datetime(2024, 8, 1, 4, 0, tzinfo=TzInfo(UTC)) open=170.25 high=174.05 low=154.93 close=163.38 volume=550739537.0 trade_count=8344622.0 vwap=162.790899
            \nsymbol='GOOGL' timestamp=datetime.datetime(2024, 9, 1, 4, 0, tzinfo=TzInfo(UTC)) open=161.72 high=166.15 low=147.215 close=165.85 volume=532684063.0 trade_count=7336551.0 vwap=157.768196
            \nsymbol='GOOGL' timestamp=datetime.datetime(2024, 10, 1, 4, 0, tzinfo=TzInfo(UTC)) open=167.685 high=182.02 low=159.74 close=171.11 volume=569355454.0 trade_count=8125196.0 vwap=167.211872
            \nsymbol='GOOGL' timestamp=datetime.datetime(2024, 11, 1, 4, 0, tzinfo=TzInfo(UTC)) open=170.07 high=172.32 low=168.011 close=169.74 volume=71518332.0 trade_count=1004338.0 vwap=170.236899
            \n\nData for JNJ:
            \nsymbol='JNJ' timestamp=datetime.datetime(2023, 10, 1, 4, 0, tzinfo=TzInfo(UTC)) open=155.42 high=159.27 low=144.95 close=148.34 volume=152897643.0 trade_count=2195972.0 vwap=153.249406
            \nsymbol='JNJ' timestamp=datetime.datetime(2023, 11, 1, 4, 0, tzinfo=TzInfo(UTC)) open=149.19 high=155.14 low=145.64 close=154.66 volume=131237109.0 trade_count=1864141.0 vwap=150.252814
            \nsymbol='JNJ' timestamp=datetime.datetime(2023, 12, 1, 5, 0, tzinfo=TzInfo(UTC)) open=156.44 high=160.02 low=151.77 close=156.74 volume=146547844.0 trade_count=1827417.0 vwap=155.986828
            \nsymbol='JNJ' timestamp=datetime.datetime(2024, 1, 1, 5, 0, tzinfo=TzInfo(UTC)) open=156.93 high=163.58 low=156.79 close=158.9 volume=138206713.0 trade_count=1881209.0 vwap=160.45963
            \nsymbol='JNJ' timestamp=datetime.datetime(2024, 2, 1, 5, 0, tzinfo=TzInfo(UTC)) open=158.16 high=162.25 low=154.84 close=161.38 volume=158290166.0 trade_count=2001166.0 vwap=158.016618
            \nsymbol='JNJ' timestamp=datetime.datetime(2024, 3, 1, 5, 0, tzinfo=TzInfo(UTC)) open=161.83 high=163.11 low=154.76 close=158.19 volume=140395970.0 trade_count=1903154.0 vwap=158.45246
            \nsymbol='JNJ' timestamp=datetime.datetime(2024, 4, 1, 4, 0, tzinfo=TzInfo(UTC)) open=157.72 high=158.15 low=143.13 close=144.59 volume=176033430.0 trade_count=2548299.0 vwap=148.911498
            \nsymbol='JNJ' timestamp=datetime.datetime(2024, 5, 1, 4, 0, tzinfo=TzInfo(UTC)) open=148.735 high=154.86 low=143.71 close=146.67 volume=174619298.0 trade_count=2275486.0 vwap=149.353049
            \nsymbol='JNJ' timestamp=datetime.datetime(2024, 6, 1, 4, 0, tzinfo=TzInfo(UTC)) open=147.25 high=149.7199 low=143.88 close=146.16 volume=132508851.0 trade_count=1867935.0 vwap=146.907792
            \nsymbol='JNJ' timestamp=datetime.datetime(2024, 7, 1, 4, 0, tzinfo=TzInfo(UTC)) open=146.07 high=161.58 low=144.5 close=157.85 volume=151363123.0 trade_count=2560032.0 vwap=153.347685
            \nsymbol='JNJ' timestamp=datetime.datetime(2024, 8, 1, 4, 0, tzinfo=TzInfo(UTC)) open=158.48 high=165.98 low=156.44 close=165.86 volume=150665081.0 trade_count=2207943.0 vwap=161.337149
            \nsymbol='JNJ' timestamp=datetime.datetime(2024, 9, 1, 4, 0, tzinfo=TzInfo(UTC)) open=165.24 high=168.85 low=160.02 close=162.06 volume=120357670.0 trade_count=1932893.0 vwap=164.726192
            \nsymbol='JNJ' timestamp=datetime.datetime(2024, 10, 1, 4, 0, tzinfo=TzInfo(UTC)) open=162.43 high=166.75 low=158.775 close=159.86 volume=133028984.0 trade_count=2177545.0 vwap=162.113652
            \nsymbol='JNJ' timestamp=datetime.datetime(2024, 11, 1, 4, 0, tzinfo=TzInfo(UTC)) open=160.58 high=161.06 low=156.35 close=158.35 volume=16447317.0 trade_count=267355.0 vwap=158.862766
            \n\nData for V:
            \nsymbol='V' timestamp=datetime.datetime(2023, 10, 1, 4, 0, tzinfo=TzInfo(UTC)) open=229.24 high=241.48 low=227.78 close=235.1 volume=129130151.0 trade_count=2053258.0 vwap=234.526276
            \nsymbol='V' timestamp=datetime.datetime(2023, 11, 1, 4, 0, tzinfo=TzInfo(UTC)) open=236.14 high=256.77 low=235.68 close=256.68 volume=131302017.0 trade_count=1758293.0 vwap=247.884996
            \nsymbol='V' timestamp=datetime.datetime(2023, 12, 1, 5, 0, tzinfo=TzInfo(UTC)) open=255.79 high=263.25 low=252.14 close=260.35 volume=109997043.0 trade_count=1538754.0 vwap=257.880147
            \nsymbol='V' timestamp=datetime.datetime(2024, 1, 1, 5, 0, tzinfo=TzInfo(UTC)) open=259.61 high=279.99 low=256.86 close=273.26 volume=120405195.0 trade_count=1949345.0 vwap=267.371172
            \nsymbol='V' timestamp=datetime.datetime(2024, 2, 1, 5, 0, tzinfo=TzInfo(UTC)) open=273.39 high=286.13 low=272.763 close=282.64 volume=101437525.0 trade_count=1720506.0 vwap=278.676958
            \nsymbol='V' timestamp=datetime.datetime(2024, 3, 1, 5, 0, tzinfo=TzInfo(UTC)) open=283.2 high=290.96 low=276.16 close=279.08 volume=122857507.0 trade_count=1750655.0 vwap=282.751579
            \nsymbol='V' timestamp=datetime.datetime(2024, 4, 1, 4, 0, tzinfo=TzInfo(UTC)) open=280.36 high=283.0 low=268.29 close=268.61 volume=147982218.0 trade_count=1920070.0 vwap=274.393547
            \nsymbol='V' timestamp=datetime.datetime(2024, 5, 1, 4, 0, tzinfo=TzInfo(UTC)) open=268.15 high=282.38 low=266.5 close=272.46 volume=171405032.0 trade_count=1957238.0 vwap=276.088618
            \nsymbol='V' timestamp=datetime.datetime(2024, 6, 1, 4, 0, tzinfo=TzInfo(UTC)) open=273.09 high=280.39 low=261.25 close=262.47 volume=180271175.0 trade_count=1877548.0 vwap=272.901139
            \nsymbol='V' timestamp=datetime.datetime(2024, 7, 1, 4, 0, tzinfo=TzInfo(UTC)) open=263.79 high=273.62 low=252.7 close=265.67 volume=163927316.0 trade_count=2480591.0 vwap=264.201215
            \nsymbol='V' timestamp=datetime.datetime(2024, 8, 1, 4, 0, tzinfo=TzInfo(UTC)) open=266.33 high=276.99 low=254.51 close=276.37 volume=190347114.0 trade_count=2053174.0 vwap=263.493405
            \nsymbol='V' timestamp=datetime.datetime(2024, 9, 1, 4, 0, tzinfo=TzInfo(UTC)) open=276.37 high=293.07 low=268.23 close=274.95 volume=166278367.0 trade_count=2210964.0 vwap=281.182786
            \nsymbol='V' timestamp=datetime.datetime(2024, 10, 1, 4, 0, tzinfo=TzInfo(UTC)) open=276.97 high=296.34 low=273.24 close=289.85 volume=128711760.0 trade_count=2038782.0 vwap=283.187313
            \nsymbol='V' timestamp=datetime.datetime(2024, 11, 1, 4, 0, tzinfo=TzInfo(UTC)) open=288.49 high=294.78 low=287.19 close=293.29 volume=13504161.0 trade_count=254564.0 vwap=291.769473
            """
        },
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

with open('groq_output.md', 'w') as f:
    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="", file=f)
