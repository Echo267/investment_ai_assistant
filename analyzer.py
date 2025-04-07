def analyze_summary(df):
    summary = df.groupby("基金/股票-自动名称").agg({
        "本金投入": "max",
        "持仓市值": "max",
        "累计收益": "max",
        "综合收益率": "max"
    }).reset_index()

    def suggest(row):
        rate = row["综合收益率"]
        if rate > 0.1:
            return "👍 表现优秀，考虑继续持有或止盈"
        elif rate < -0.05:
            return "⚠️ 收益较低，请评估是否止损"
        else:
            return "🟡 表现中性，继续观察"

    summary["AI建议"] = summary.apply(suggest, axis=1)
    return summary