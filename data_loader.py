import pandas as pd
import streamlit as st
def load_trade_data(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file, sheet_name="交易记录")
        df = df[df["日期"].notna() & df["代码"].notna()]
        df["日期"] = pd.to_datetime(df["日期"])
        return df
    except Exception as e:
        st.error(f"❌ 读取文件失败: {e}")
        return None