import pandas as pd
import numpy as np
import streamlit as st
from recomend import new_recommendation
from recomend import movie_name
st.header("Movie Recommendation System")
option = st.selectbox(
    'Which movies have u watched ?',
    movie_name())
st.write(option)
count=st.slider("Recommend Movies", min_value=1, max_value=20, step=1)
l=pd.DataFrame({
    "Sr.no":np.arange(1,count+1),
    "movie":new_recommendation(option,count)
}, index=range(1,count+1))
st.table(l)
