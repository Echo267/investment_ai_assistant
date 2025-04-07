def generate_prompt(df, summary):
    total_invested = df["本金投入"].sum()
    total_gain = df["累计收益"].sum()
    text_summary = summary[["基金/股票-自动名称", "本金投入", "累计收益", "综合收益率"]].to_string(index=False)
    prompt = f"""
我总共投入资金 {total_invested:.2f} 元，目前累计收益约 {total_gain:.2f} 元，以下是我的交易摘要：

{text_summary}

请你作为我的 AI 投资顾问，帮我分析整体策略是否合理，并提出优化建议。
"""
    return prompt