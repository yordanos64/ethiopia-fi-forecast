import streamlit as st

# Set up page configurations
st.set_page_config(page_title="Ethiopia Financial Inclusion Dashboard", layout="wide")

st.title("🇪🇹 Ethiopia Financial Inclusion Forecasting System")
st.markdown("### Tracking Digital Financial Transformation (2025 - 2027)")
st.write("---")

# Metrics Sidebar Layout
st.sidebar.header("Dashboard Controls")
st.sidebar.write("Project Milestone: Week 11 Challenge")
st.sidebar.info("Status: Final Submission Ready")

# Create two columns for visual layout metrics
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Access: Account Ownership Rate Trend")
    st.markdown("**Historical Benchmarks (Global Findex):**")
    st.write("🔹 2011: **14.0%**")
    st.write("🔹 2014: **22.0%**")
    st.write("🔹 2017: **35.0%**")
    st.write("🔹 2021: **46.0%**")
    st.write("🔹 2024: **49.0%**")
    
    st.write("---")
    st.markdown("**Predicted Access Targets:**")
    st.info("🔮 2025: **52.12%**  |  2026: **55.25%**  |  2027: **58.38%**")

with col2:
    st.subheader("💳 Usage: Digital Payment Adoption Rate")
    st.markdown("**Historical Baseline Reference (2024 Context):**")
    st.write("🔹 Mobile Money Ownership: **9.45%**")
    st.write("🔹 Made/Received Digital Payments: **35.0%**")
    st.write("🔹 Used Account for Wages: **15.0%**")
    
    st.write("---")
    st.markdown("**Predicted Usage Targets (Telebirr & M-Pesa Acceleration):**")
    st.success("🔮 2025: **39.50%**  |  2026: **44.00%**  |  2027: **48.50%**")

st.write("---")
st.markdown("### 🎯 Policy Targets & Market Nuances")
st.warning("💡 **Market Context:** Interoperable P2P digital transfers have officially surpassed ATM cash withdrawals in Ethiopia. Fayda National ID expansion acts as a core enabler for rapid future account onboarding.")
