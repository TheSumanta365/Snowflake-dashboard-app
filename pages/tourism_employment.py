import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="🧳 State-wise Tourism Employment", layout="wide")
st.title("🌏 Tourism Employment Across Indian States")

uploaded_file = st.file_uploader("📁 Upload CSV file (state-wise tourism data)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    df.rename(columns={"States/UTs": "State"}, inplace=True)

    st.subheader("📊 Processed Dataset Preview")
    st.dataframe(df)

    states = df["State"].dropna().unique()
    selected_state = st.selectbox("Select a State", sorted(states))

    filtered_df = df[df["State"] == selected_state]

    fig, ax = plt.subplots()
    ax.bar(filtered_df["State"], filtered_df["Estimated employment due to Tourism in States/UTs (Number in lakhs)"], color="blue")
    ax.set_title(f"Tourism Employment in {selected_state}")
    ax.set_xlabel("State")
    ax.set_ylabel("Estimated Employment (lakhs)")
    ax.grid(True)
    st.pyplot(fig)

else:
    st.info("⬆️ Please upload your dataset to begin.")
