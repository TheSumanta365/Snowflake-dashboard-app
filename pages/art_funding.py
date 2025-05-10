import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="🎨 State-wise Art Funding Dashboard", layout="wide")
st.title("🎭 Government Financial Support for Art - India")

uploaded_file = st.file_uploader("📁 Upload CSV file (state-wise funding data)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    df.rename(columns={"State/UT": "State"}, inplace=True)

    amount_cols = [col for col in df.columns if "Amount" in col]

    long_df = pd.melt(
        df,
        id_vars=["State"],
        value_vars=amount_cols,
        var_name="Year",
        value_name="Amount"
    )

    long_df["Year"] = long_df["Year"].str.extract(r"(\d{4}-\d{4})")

    long_df.dropna(subset=["Amount"], inplace=True)

    st.subheader("📊 Processed Dataset Preview")
    st.dataframe(long_df)

    states = long_df["State"].dropna().unique()
    selected_state = st.selectbox("Select a State", sorted(states))

    filtered_df = long_df[long_df["State"] == selected_state]

    try:
        filtered_df["Amount"] = (
            filtered_df["Amount"]
            .replace("[^0-9]", "", regex=True)
            .astype(float)
        )
    except:
        st.warning("⚠️ Could not convert amount column to numbers properly.")

    fig, ax = plt.subplots()
    filtered_df.sort_values("Year", inplace=True)
    ax.plot(filtered_df["Year"], filtered_df["Amount"], marker="o", color="green")
    ax.set_title(f"Funding Amount Over Years in {selected_state}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Amount (₹)")
    ax.grid(True)
    st.pyplot(fig)

else:
    st.info("⬆️ Please upload your dataset to begin.")
