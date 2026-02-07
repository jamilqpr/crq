# 🔐 Cyber Risk Quantification (CRQ) Web App

A professional-grade web application for quantifying cyber security risk using the **PyFair (Factor Analysis of Information Risk)** methodology.

## 🎯 Overview

This tool enables security analysts to quantify cyber risk in financial terms using Monte Carlo simulations and the industry-standard FAIR framework.

## ✨ Features

- **PyFair Implementation**: Full implementation of FAIR risk model
- **Monte Carlo Simulation**: Up to 100,000 simulations for statistical accuracy
- **Multiple Input Methods**: PERT, Beta, and Normal distributions
- **Interactive Dashboards**: Real-time visualization of risk metrics
- **Value at Risk (VaR)**: Calculate risk at configurable confidence levels
- **Loss Exceedance Curves**: Understand probability of exceeding loss thresholds
- **Export Capabilities**: Download simulation data and reports
- **Risk Classification**: Automatic risk level assessment (Low/Medium/High/Critical)

## 📊 PyFair Model Components

```
Risk = Loss Event Frequency (LEF) × Loss Magnitude (LM)

Where:
- LEF = Threat Event Frequency (TEF) × Vulnerability (Vuln)
- LM = Primary Loss Magnitude (PLM) + Secondary Loss Magnitude (SLM)
- ALE = Annual Loss Exposure (expected annual financial loss)
```

## 🚀 Installation

### Step 1: Install Dependencies

```bash
pip install -r requirements_crq.txt
```

### Step 2: Run the Application

```bash
streamlit run crq_app.py
```

The app will open automatically in your default browser at `http://localhost:8501`

## 📖 Usage Guide

### 1. Input Parameters

**Threat Event Frequency (TEF)**
- How many times per year does a threat actor attempt this attack?
- Input as range (min/likely/max) or mean/std dev

**Vulnerability (Vuln)**
- What's the probability that an attack attempt succeeds?
- Express as percentage or range (0-100%)

**Primary Loss Magnitude (PLM)**
- Direct financial impact per loss event
- Examples: incident response, system recovery, data restoration

**Secondary Loss Factor (SLM)**
- Indirect costs multiplier (reputation damage, legal, regulatory)
- Typically 0.5x to 3x of primary losses

### 2. Run Simulation

- Set number of simulations (1,000 - 100,000)
- Choose confidence level (80% - 99%)
- Click "Run Risk Analysis"

### 3. Review Results

**Main Metrics:**
- Mean ALE: Average expected annual loss
- Median ALE: Middle value of loss distribution
- VaR: Value at Risk at chosen confidence level
- Risk Level: Automatic classification

**Visualizations:**
- Risk Distribution: Histogram of ALE values
- Loss Components: Breakdown of TEF, Vuln, LEF, LM
- Exceedance Curve: Probability of exceeding loss thresholds
- Detailed Report: Comprehensive risk assessment

## 💡 Example Scenarios

### Scenario 1: Ransomware Attack

```
TEF: 10-50-200 attempts/year
Vulnerability: 20-30-50%
Primary Loss: $50k - $500k - $2M
Secondary Factor: 1.5x
```

### Scenario 2: Data Breach

```
TEF: 5-20-100 attempts/year
Vulnerability: 10-15-40%
Primary Loss: $100k - $1M - $10M
Secondary Factor: 2.0x
```

### Scenario 3: Insider Threat

```
TEF: 1-5-20 attempts/year
Vulnerability: 30-50-80%
Primary Loss: $20k - $200k - $1M
Secondary Factor: 1.0x
```

## 📈 Interpreting Results

### Risk Levels

- **Low**: ALE < $100k - Acceptable risk, standard controls
- **Medium**: $100k - $500k - Enhanced monitoring required
- **High**: $500k - $2M - Priority remediation needed
- **Critical**: > $2M - Immediate action required

### Value at Risk (VaR)

VaR at 95% confidence = $500k means:
- 95% chance annual losses will be ≤ $500k
- 5% chance they could exceed $500k

## 🛡️ Use Cases

1. **Risk Assessment**: Quantify specific cyber threats
2. **Budget Justification**: Support security investment decisions
3. **Cyber Insurance**: Determine appropriate coverage levels
4. **Board Reporting**: Communicate risk in financial terms
5. **Cost-Benefit Analysis**: Evaluate control effectiveness
6. **Compliance**: Support regulatory risk reporting requirements

## 📊 Output Files

The tool generates:
- **Interactive Dashboards**: View in browser
- **CSV Exports**: Full simulation data
- **Risk Reports**: Comprehensive assessment documents

## 🔧 Customization

### Adjust Risk Thresholds

Edit the `get_risk_level()` function in `crq_app.py`:

```python
def get_risk_level(ale):
    if ale < 100000:
        return "Low", "risk-low"
    elif ale < 500000:
        return "Medium", "risk-medium"
    # ... customize thresholds
```

### Add New Distributions

Extend the input methods in the sidebar to support additional statistical distributions.

## ⚠️ Important Notes

- **Results are estimates**: Based on input assumptions and subject to uncertainty
- **Validate assumptions**: Review inputs with subject matter experts
- **Regular updates**: Reassess risk as threat landscape evolves
- **Professional judgment**: Use results as decision support, not absolute truth

## 🌐 Deployment Options

### Local Deployment
```bash
streamlit run crq_app.py
```

### Cloud Deployment (Streamlit Cloud)
1. Push to GitHub repository
2. Connect to Streamlit Cloud
3. Deploy with one click

### Docker Deployment
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements_crq.txt .
RUN pip install -r requirements_crq.txt
COPY crq_app.py .
EXPOSE 8501
CMD ["streamlit", "run", "crq_app.py"]
```

## 📚 References

- **FAIR Framework**: [The Open Group FAIR](https://www.fairinstitute.org/)
- **PyFair**: Python implementation of FAIR standard
- **NIST Cybersecurity Framework**: Risk assessment guidance

## 🤝 Support

For questions or issues:
- Review the in-app documentation
- Check example scenarios
- Validate inputs with security team
- Consult FAIR methodology guidelines

## 📄 License

For professional and educational use by security professionals.

---

**Built for Security Analysts** | **Powered by PyFair** | **Version 1.0**
