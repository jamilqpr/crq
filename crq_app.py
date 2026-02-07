import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from scipy import stats

# Page configuration
st.set_page_config(
    page_title="Cyber Risk Quantification (PyFair)",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .risk-low { color: #10B981; font-weight: bold; }
    .risk-medium { color: #F59E0B; font-weight: bold; }
    .risk-high { color: #EF4444; font-weight: bold; }
    .risk-critical { color: #DC2626; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">🔐 Cyber Risk Quantification Model</h1>', unsafe_allow_html=True)
st.markdown("**PyFair-Based Risk Analysis Framework** | Quantify Information Security Risk in Financial Terms")
st.markdown("---")

# Sidebar - Model Inputs
st.sidebar.header("📊 Risk Parameters")
st.sidebar.markdown("### Threat Event Frequency (TEF)")
st.sidebar.markdown("*How often does a threat actor attempt an attack?*")

tef_method = st.sidebar.radio("Input Method:", ["Range (PERT)", "Mean & Std Dev"], key="tef_method")

if tef_method == "Range (PERT)":
    tef_min = st.sidebar.number_input("TEF Min (per year)", min_value=0, value=10, help="Minimum threat attempts per year")
    tef_likely = st.sidebar.number_input("TEF Most Likely", min_value=0, value=50, help="Most likely number of attempts")
    tef_max = st.sidebar.number_input("TEF Max (per year)", min_value=0, value=200, help="Maximum threat attempts")
else:
    tef_mean = st.sidebar.number_input("TEF Mean (per year)", min_value=0.0, value=50.0)
    tef_std = st.sidebar.number_input("TEF Std Dev", min_value=0.1, value=20.0)

st.sidebar.markdown("---")
st.sidebar.markdown("### Vulnerability (Vuln)")
st.sidebar.markdown("*Probability that a threat attempt succeeds*")

vuln_method = st.sidebar.radio("Input Method:", ["Range (Beta)", "Percentage"], key="vuln_method")

if vuln_method == "Range (Beta)":
    vuln_min = st.sidebar.slider("Vuln Min (%)", 0, 100, 10) / 100
    vuln_likely = st.sidebar.slider("Vuln Most Likely (%)", 0, 100, 30) / 100
    vuln_max = st.sidebar.slider("Vuln Max (%)", 0, 100, 60) / 100
else:
    vuln_pct = st.sidebar.slider("Vulnerability (%)", 0, 100, 30) / 100

st.sidebar.markdown("---")
st.sidebar.markdown("### Primary Loss Magnitude")
st.sidebar.markdown("*Direct financial impact per loss event*")

plm_method = st.sidebar.radio("Input Method:", ["Range (PERT)", "Mean & Std Dev"], key="plm_method")

if plm_method == "Range (PERT)":
    plm_min = st.sidebar.number_input("Min Loss ($)", min_value=0, value=10000, step=1000)
    plm_likely = st.sidebar.number_input("Most Likely Loss ($)", min_value=0, value=100000, step=5000)
    plm_max = st.sidebar.number_input("Max Loss ($)", min_value=0, value=1000000, step=10000)
else:
    plm_mean = st.sidebar.number_input("Mean Loss ($)", min_value=0, value=100000, step=5000)
    plm_std = st.sidebar.number_input("Loss Std Dev ($)", min_value=0, value=50000, step=1000)

st.sidebar.markdown("---")
st.sidebar.markdown("### Secondary Loss Multiplier")
slm_factor = st.sidebar.slider("Secondary Loss Factor", 0.0, 3.0, 0.5, 0.1, 
                                help="Multiplier for indirect costs (reputation, legal, etc.)")

# Simulation parameters
st.sidebar.markdown("---")
st.sidebar.markdown("### Simulation Settings")
n_simulations = st.sidebar.slider("Number of Simulations", 1000, 100000, 10000, step=1000)
confidence_level = st.sidebar.slider("Confidence Level (%)", 80, 99, 95)

run_simulation = st.sidebar.button("🚀 Run Risk Analysis", type="primary", use_container_width=True)

# Main content area
if run_simulation:
    with st.spinner("Running Monte Carlo simulation..."):
        # Generate distributions
        np.random.seed(42)
        
        # 1. Threat Event Frequency (TEF)
        if tef_method == "Range (PERT)":
            # PERT distribution (Modified Beta)
            tef_samples = (tef_min + 4*tef_likely + tef_max) / 6 + \
                          np.random.triangular(tef_min - tef_likely, 0, tef_max - tef_likely, n_simulations)
            tef_samples = np.clip(tef_samples, tef_min, tef_max)
        else:
            tef_samples = np.random.normal(tef_mean, tef_std, n_simulations)
            tef_samples = np.clip(tef_samples, 0, None)
        
        # 2. Vulnerability (Vuln)
        if vuln_method == "Range (Beta)":
            # Beta PERT
            vuln_mean = (vuln_min + 4*vuln_likely + vuln_max) / 6
            vuln_std = (vuln_max - vuln_min) / 6
            alpha = vuln_mean * ((vuln_mean * (1 - vuln_mean) / vuln_std**2) - 1)
            beta = (1 - vuln_mean) * ((vuln_mean * (1 - vuln_mean) / vuln_std**2) - 1)
            vuln_samples = np.random.beta(max(alpha, 0.5), max(beta, 0.5), n_simulations)
        else:
            vuln_samples = np.full(n_simulations, vuln_pct)
        
        # 3. Loss Event Frequency (LEF = TEF × Vuln)
        lef_samples = tef_samples * vuln_samples
        
        # 4. Primary Loss Magnitude (PLM)
        if plm_method == "Range (PERT)":
            plm_samples = (plm_min + 4*plm_likely + plm_max) / 6 + \
                          np.random.triangular(plm_min - plm_likely, 0, plm_max - plm_likely, n_simulations)
            plm_samples = np.clip(plm_samples, plm_min, plm_max)
        else:
            plm_samples = np.random.lognormal(np.log(plm_mean), plm_std/plm_mean, n_simulations)
        
        # 5. Secondary Loss Magnitude (SLM)
        slm_samples = plm_samples * slm_factor
        
        # 6. Total Loss Magnitude (LM = PLM + SLM)
        lm_samples = plm_samples + slm_samples
        
        # 7. Annual Loss Exposure (ALE = LEF × LM)
        ale_samples = lef_samples * lm_samples
        
        # Calculate statistics
        ale_mean = np.mean(ale_samples)
        ale_median = np.median(ale_samples)
        ale_std = np.std(ale_samples)
        ale_var = (confidence_level/100)
        ale_var_value = np.percentile(ale_samples, ale_var * 100)
        ale_min = np.min(ale_samples)
        ale_max = np.max(ale_samples)
        
        # Risk rating
        def get_risk_level(ale):
            if ale < 100000:
                return "Low", "risk-low"
            elif ale < 500000:
                return "Medium", "risk-medium"
            elif ale < 2000000:
                return "High", "risk-high"
            else:
                return "Critical", "risk-critical"
        
        risk_level, risk_class = get_risk_level(ale_mean)
        
    # Display Results
    st.success("✅ Simulation Complete!")
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Mean Annual Loss Exposure (ALE)", f"${ale_mean:,.0f}")
    with col2:
        st.metric("Median ALE", f"${ale_median:,.0f}")
    with col3:
        st.metric(f"VaR ({confidence_level}%)", f"${ale_var_value:,.0f}")
    with col4:
        st.markdown(f"**Risk Level**")
        st.markdown(f'<p class="{risk_class}" style="font-size: 1.5rem;">{risk_level}</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Visualizations
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Risk Distribution", "🎯 Loss Components", "📈 Exceedance Curve", "📋 Detailed Report"])
    
    with tab1:
        st.subheader("Annual Loss Exposure Distribution")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # ALE Distribution
            fig_ale = go.Figure()
            fig_ale.add_trace(go.Histogram(
                x=ale_samples,
                nbinsx=100,
                name="ALE Distribution",
                marker=dict(color='#667eea', line=dict(color='#764ba2', width=1))
            ))
            fig_ale.add_vline(x=ale_mean, line_dash="dash", line_color="red", 
                             annotation_text=f"Mean: ${ale_mean:,.0f}")
            fig_ale.add_vline(x=ale_var_value, line_dash="dot", line_color="orange",
                             annotation_text=f"VaR {confidence_level}%: ${ale_var_value:,.0f}")
            
            fig_ale.update_layout(
                title="Distribution of Annual Loss Exposure",
                xaxis_title="Annual Loss ($)",
                yaxis_title="Frequency",
                template="plotly_white",
                height=400
            )
            st.plotly_chart(fig_ale, use_container_width=True)
        
        with col2:
            st.markdown("### 📊 Statistics")
            st.metric("Mean", f"${ale_mean:,.0f}")
            st.metric("Median", f"${ale_median:,.0f}")
            st.metric("Std Dev", f"${ale_std:,.0f}")
            st.metric("Min", f"${ale_min:,.0f}")
            st.metric("Max", f"${ale_max:,.0f}")
            st.metric("Range", f"${ale_max - ale_min:,.0f}")
            
            # Percentiles
            st.markdown("**Percentiles:**")
            for p in [50, 75, 90, 95, 99]:
                val = np.percentile(ale_samples, p)
                st.write(f"{p}th: ${val:,.0f}")
    
    with tab2:
        st.subheader("Loss Components Breakdown")
        
        # Create subplots for components
        fig_components = make_subplots(
            rows=2, cols=2,
            subplot_titles=("Loss Event Frequency", "Threat Event Frequency", 
                          "Vulnerability", "Loss Magnitude"),
            specs=[[{'type': 'histogram'}, {'type': 'histogram'}],
                   [{'type': 'histogram'}, {'type': 'histogram'}]]
        )
        
        fig_components.add_trace(
            go.Histogram(x=lef_samples, name="LEF", marker=dict(color='#FF6B6B'), nbinsx=50),
            row=1, col=1
        )
        fig_components.add_trace(
            go.Histogram(x=tef_samples, name="TEF", marker=dict(color='#4ECDC4'), nbinsx=50),
            row=1, col=2
        )
        fig_components.add_trace(
            go.Histogram(x=vuln_samples, name="Vuln", marker=dict(color='#FFD93D'), nbinsx=50),
            row=2, col=1
        )
        fig_components.add_trace(
            go.Histogram(x=lm_samples, name="LM", marker=dict(color='#6BCB77'), nbinsx=50),
            row=2, col=2
        )
        
        fig_components.update_layout(height=700, showlegend=False, template="plotly_white")
        fig_components.update_xaxes(title_text="Events/Year", row=1, col=1)
        fig_components.update_xaxes(title_text="Attempts/Year", row=1, col=2)
        fig_components.update_xaxes(title_text="Probability", row=2, col=1)
        fig_components.update_xaxes(title_text="Loss ($)", row=2, col=2)
        
        st.plotly_chart(fig_components, use_container_width=True)
        
        # Summary table
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Frequency Metrics")
            st.write(f"**TEF Mean:** {np.mean(tef_samples):.2f} attempts/year")
            st.write(f"**Vulnerability:** {np.mean(vuln_samples)*100:.2f}%")
            st.write(f"**LEF Mean:** {np.mean(lef_samples):.2f} events/year")
        
        with col2:
            st.markdown("### Loss Magnitude")
            st.write(f"**Primary Loss:** ${np.mean(plm_samples):,.0f}")
            st.write(f"**Secondary Loss:** ${np.mean(slm_samples):,.0f}")
            st.write(f"**Total Loss/Event:** ${np.mean(lm_samples):,.0f}")
    
    with tab3:
        st.subheader("Loss Exceedance Curve")
        
        # Calculate exceedance probabilities
        sorted_ale = np.sort(ale_samples)
        exceedance_prob = np.arange(len(sorted_ale), 0, -1) / len(sorted_ale) * 100
        
        fig_exceed = go.Figure()
        fig_exceed.add_trace(go.Scatter(
            x=sorted_ale,
            y=exceedance_prob,
            mode='lines',
            name='Exceedance',
            line=dict(color='#667eea', width=3),
            fill='tozeroy',
            fillcolor='rgba(102, 126, 234, 0.2)'
        ))
        
        # Add reference lines
        for prob in [1, 5, 10, 50]:
            loss_val = np.percentile(ale_samples, 100 - prob)
            fig_exceed.add_hline(y=prob, line_dash="dot", line_color="gray", opacity=0.5)
            fig_exceed.add_vline(x=loss_val, line_dash="dot", line_color="gray", opacity=0.5)
        
        fig_exceed.update_layout(
            title="Probability of Exceeding Loss Threshold",
            xaxis_title="Annual Loss ($)",
            yaxis_title="Probability of Exceedance (%)",
            template="plotly_white",
            height=500,
            xaxis_type="log"
        )
        
        st.plotly_chart(fig_exceed, use_container_width=True)
        
        st.markdown("### 🎯 Key Thresholds")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("1% Exceedance", f"${np.percentile(ale_samples, 99):,.0f}",
                     help="There's a 1% chance losses will exceed this amount")
        with col2:
            st.metric("5% Exceedance", f"${np.percentile(ale_samples, 95):,.0f}",
                     help="There's a 5% chance losses will exceed this amount")
        with col3:
            st.metric("10% Exceedance", f"${np.percentile(ale_samples, 90):,.0f}",
                     help="There's a 10% chance losses will exceed this amount")
    
    with tab4:
        st.subheader("📋 Detailed Risk Assessment Report")
        
        # Executive Summary
        st.markdown("### Executive Summary")
        st.info(f"""
        Based on {n_simulations:,} Monte Carlo simulations using the PyFair methodology, the estimated 
        **Annual Loss Exposure (ALE)** for this cyber risk scenario is **${ale_mean:,.0f}** (mean) with a 
        **{confidence_level}% Value at Risk (VaR)** of **${ale_var_value:,.0f}**.
        
        **Risk Classification: {risk_level}**
        
        This indicates that there is a {confidence_level}% probability that annual losses will not exceed 
        ${ale_var_value:,.0f}, and a {100-confidence_level}% chance they could be higher.
        """)
        
        # Input Summary
        st.markdown("### Input Parameters")
        
        input_df = pd.DataFrame({
            "Parameter": ["Threat Event Frequency", "Vulnerability", "Primary Loss", "Secondary Loss Factor", "Simulations"],
            "Value": [
                f"{np.mean(tef_samples):.1f} attempts/year",
                f"{np.mean(vuln_samples)*100:.1f}%",
                f"${np.mean(plm_samples):,.0f}",
                f"{slm_factor}x",
                f"{n_simulations:,}"
            ]
        })
        st.dataframe(input_df, use_container_width=True, hide_index=True)
        
        # Results Summary
        st.markdown("### Simulation Results")
        
        results_df = pd.DataFrame({
            "Metric": ["Mean ALE", "Median ALE", "Standard Deviation", "Minimum", "Maximum", 
                      f"VaR ({confidence_level}%)", "50th Percentile", "75th Percentile", 
                      "90th Percentile", "95th Percentile", "99th Percentile"],
            "Value ($)": [
                f"${ale_mean:,.0f}",
                f"${ale_median:,.0f}",
                f"${ale_std:,.0f}",
                f"${ale_min:,.0f}",
                f"${ale_max:,.0f}",
                f"${ale_var_value:,.0f}",
                f"${np.percentile(ale_samples, 50):,.0f}",
                f"${np.percentile(ale_samples, 75):,.0f}",
                f"${np.percentile(ale_samples, 90):,.0f}",
                f"${np.percentile(ale_samples, 95):,.0f}",
                f"${np.percentile(ale_samples, 99):,.0f}"
            ]
        })
        st.dataframe(results_df, use_container_width=True, hide_index=True)
        
        # Download results
        st.markdown("### 📥 Export Results")
        
        # Create comprehensive export
        export_data = pd.DataFrame({
            'ALE': ale_samples,
            'LEF': lef_samples,
            'TEF': tef_samples,
            'Vulnerability': vuln_samples,
            'Loss_Magnitude': lm_samples,
            'Primary_Loss': plm_samples,
            'Secondary_Loss': slm_samples
        })
        
        csv = export_data.to_csv(index=False)
        st.download_button(
            label="📊 Download Full Simulation Data (CSV)",
            data=csv,
            file_name=f"crq_simulation_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
        
        # Risk Management Recommendations
        st.markdown("### 🛡️ Risk Management Recommendations")
        
        if risk_level == "Critical":
            st.error("""
            **Immediate Action Required:**
            - Implement additional security controls immediately
            - Consider cyber insurance coverage
            - Conduct incident response planning
            - Execute vulnerability remediation program
            """)
        elif risk_level == "High":
            st.warning("""
            **Priority Actions:**
            - Review and enhance existing security controls
            - Evaluate cyber insurance options
            - Conduct security awareness training
            - Implement enhanced monitoring
            """)
        elif risk_level == "Medium":
            st.info("""
            **Recommended Actions:**
            - Maintain current security posture
            - Regular security assessments
            - Monitor threat landscape
            - Review controls quarterly
            """)
        else:
            st.success("""
            **Current Status:**
            - Risk within acceptable tolerance
            - Continue regular monitoring
            - Maintain security baseline
            - Annual assessment recommended
            """)

else:
    # Landing page
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("## 🎯 About This Tool")
        st.markdown("""
        This **Cyber Risk Quantification** tool implements the **Factor Analysis of Information Risk (PyFair)** 
        standard to help security professionals quantify cyber risk in financial terms.
        
        ### 🔍 How It Works:
        
        1. **Define Threat Landscape**: Estimate how often threat actors attempt attacks (TEF)
        2. **Assess Vulnerability**: Determine the probability an attack succeeds (Vuln)
        3. **Calculate Loss Event Frequency**: LEF = TEF × Vulnerability
        4. **Estimate Loss Magnitude**: Primary + Secondary financial impacts
        5. **Compute Annual Loss Exposure**: ALE = LEF × Loss Magnitude
        
        ### 📊 PyFair Model Components:
        
        - **TEF**: Threat Event Frequency (attempts/year)
        - **Vuln**: Vulnerability (probability of success)
        - **LEF**: Loss Event Frequency (LEF = TEF × Vuln)
        - **PLM**: Primary Loss Magnitude (direct costs)
        - **SLM**: Secondary Loss Magnitude (indirect costs)
        - **ALE**: Annual Loss Exposure (expected annual loss)
        
        ### ✨ Key Features:
        
        - ✅ Monte Carlo simulation (up to 100,000 iterations)
        - ✅ Multiple input methods (PERT, Beta, Normal distributions)
        - ✅ Value at Risk (VaR) calculations
        - ✅ Interactive visualizations
        - ✅ Exceedance probability curves
        - ✅ Exportable results and reports
        - ✅ Risk-based decision support
        """)
    
    with col2:
        st.markdown("## 🚀 Quick Start")
        st.info("""
        1. **Set Parameters** in the sidebar
        2. **Configure** threat frequency
        3. **Adjust** vulnerability estimates
        4. **Define** loss magnitudes
        5. Click **'Run Risk Analysis'**
        """)
        
        st.markdown("## 📚 Use Cases")
        st.success("""
        - **Risk Assessment**: Quantify specific cyber threats
        - **Budget Planning**: Justify security investments
        - **Insurance**: Determine coverage needs
        - **Compliance**: Support risk reporting
        - **Decision Making**: Cost-benefit analysis
        """)
        
        st.markdown("## ⚠️ Disclaimer")
        st.warning("""
        Results are estimates based on input assumptions. 
        Always validate with subject matter experts.
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <p><strong>Cyber Risk Quantification Tool v1.0</strong></p>
    <p>Based on Factor Analysis of Information Risk (FAIR) Standard | Built for Security Professionals</p>
    <p>© 2026 Security Analytics | For Professional Use Only</p>
</div>
""", unsafe_allow_html=True)
