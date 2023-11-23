import streamlit as st

long_markdown_1 = """
<h1 style='color: green; font-size: 24px;'>
    OPEC+ is set to consider whether
    to make additional oil supply cuts when the group meets later this month

    Oil has slid to around $79 a barrel for Brent crude from a 2023 high in
    September near $98. Concern about demand and a possible surplus next year
    has pressured prices, despite support from the OPEC+ cuts and conflict in the
    Middle East.

  Source: Reuters <a href ='https://www.reuters.com/business/energy/opec-consider-whether-more-oil-cuts-needed-sources-2023-11-17/' target = '_blank'>Read more</a>
</h1>
"""

st.markdown(long_markdown_1, unsafe_allow_html=True)


long_markdown_2 = """
<h1 style='color: green; font-size: 24px;'>
    OPEC+ is set to consider whether
    to make additional oil supply cuts when the group meets later this month

    Oil has slid to around $79 a barrel for Brent crude from a 2023 high in
    September near $98. Concern about demand and a possible surplus next year
    has pressured prices, despite support from the OPEC+ cuts and conflict in the
    Middle East.

  Source: Reuters <a href ='https://www.reuters.com/business/energy/opec-consider-whether-more-oil-cuts-needed-sources-2023-11-17/' target = '_blank'>Read more</a>
</h1>
"""

st.markdown(long_markdown_2, unsafe_allow_html=True)
