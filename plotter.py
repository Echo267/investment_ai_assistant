import matplotlib.pyplot as plt

def plot_gain_chart(summary):
    fig, ax = plt.subplots(figsize=(10, 4))
    sorted_df = summary.sort_values("综合收益率", ascending=False)
    ax.bar(sorted_df["基金/股票-自动名称"], sorted_df["综合收益率"])
    ax.set_ylabel("综合收益率")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig