import streamlit as st
import pandas as pd
import numpy as np
import time

# ============================================
# ページ設定
# ============================================
st.set_page_config(
    page_title="AIモデル評価ダッシュボード",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# カスタムCSSでカード風デザインを実装
# ============================================
st.markdown("""
<style>
    .card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .metric-title {
        font-weight: bold;
        color: #2c3e50;
    }
    .metric-value {
        font-size: 1.5rem;
        color: #3498db;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# タイトル
# ============================================
st.title("AIモデル評価ダッシュボード")
st.markdown("""
本アプリは、機械学習モデルの性能を評価・比較するためのダッシュボードです。
サンプルデータを用いた評価結果や、インタラクティブな可視化が可能です。
""")

# ============================================
# サイドバー - モデルと評価指標選択
# ============================================
st.sidebar.header("設定")
model_name = st.sidebar.selectbox("モデルを選択", ["ランダムフォレスト", "ロジスティック回帰", "SVM"])
eval_metric = st.sidebar.multiselect("評価指標", ["Accuracy", "Precision", "Recall", "F1-score"])

# ============================================
# ダミーデータで評価結果表示
# ============================================
st.header("モデル評価結果")
dummy_scores = {
    "ランダムフォレスト": [0.91, 0.89, 0.87, 0.88],
    "ロジスティック回帰": [0.85, 0.83, 0.81, 0.82],
    "SVM": [0.88, 0.86, 0.84, 0.85]
}

metrics = ["Accuracy", "Precision", "Recall", "F1-score"]
data = pd.DataFrame(
    [dummy_scores[model_name]],
    columns=metrics,
    index=[model_name]
)

# カード風レイアウトでメトリクス表示
st.markdown("### 評価メトリクス (カードUI)")
col1, col2, col3, col4 = st.columns(4)
for i, col in enumerate([col1, col2, col3, col4]):
    with col:
        st.markdown(f"""
        <div class='card'>
            <div class='metric-title'>{metrics[i]}</div>
            <div class='metric-value'>{data[metrics[i]].values[0]*100:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

# ============================================
# チャートで可視化
# ============================================
st.subheader("チャートによる比較")
st.bar_chart(data.T)

# ============================================
# ファイルアップロードと表示
# ============================================
st.header("データのアップロードと確認")
uploaded_file = st.file_uploader("CSVファイルをアップロード", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("アップロードされたデータ:")
    st.dataframe(df.head())

# ============================================
# 評価シミュレーション
# ============================================
st.header("評価シミュレーション")
st.markdown("ボタンを押すと評価をシミュレートします。")
if st.button("シミュレート開始"):
    with st.spinner("評価中..."):
        time.sleep(2)
        st.success("評価完了！")
        st.balloons()

# ============================================
# フッター
# ============================================
st.markdown("""
---
**公開要件：** このアプリは講義用に作成されたもので、GitHub上で公開することを前提としています。
""")
