import streamlit as st
from data_loader import load_trade_data
from analyzer import analyze_summary
from advisor import generate_prompt
from plotter import plot_gain_chart

st.title("📈 个人股票/基金投资 AI 助理")

uploaded_file = st.file_uploader("请上传你的投资交易记录表（Excel 格式）", type=["xlsx"])
if uploaded_file:
    df = load_trade_data(uploaded_file)
    if df is not None:
        st.success("✅ 成功读取交易记录！")

        summary = analyze_summary(df)
        st.subheader("📊 投资概况分析")
        st.dataframe(summary)

        st.subheader("📉 收益率排行榜")
        fig = plot_gain_chart(summary)
        st.pyplot(fig)

        st.subheader("🧠 AI 分析建议 Prompt（可用于 DeepSeek）")
        prompt = generate_prompt(df, summary)
        st.text_area("📋 可复制粘贴使用的 Prompt", prompt, height=300)
    else:
        st.error("❌ 无法读取交易记录，请检查文件格式是否正确。")
else:
    st.info("💡 请上传你的投资交易记录表（Excel 格式），以便进行分析。")
