import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from scipy import stats

# Page configuration
st.set_page_config(
    page_title="CyberRisk Quantum | Advanced Risk Analytics",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "Advanced Cyber Risk Quantification Platform"
    }
)

# Enhanced Custom CSS with Cybersecurity Theme - Comprehensive Text Fix
st.markdown("""
<style>
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f172a 100%);
        color: #e2e8f0 !important;
    }

    /* Text selection */
    ::selection {
        background: rgba(15, 23, 42, 0.85);
        color: #e2e8f0;
    }

    ::-moz-selection {
        background: rgba(15, 23, 42, 0.85);
        color: #e2e8f0;
    }

    mark {
        background: rgba(15, 23, 42, 0.85) !important;
        color: #e2e8f0 !important;
        padding: 0 0.1em;
    }
    
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
        color: #e2e8f0 !important;
    }
    
    /* Comprehensive Text Visibility Overrides */
    *, 
    *::before, 
    *::after,
    .stApp *,
    .stApp *::before,
    .stApp *::after {
        color: #e2e8f0 !important;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6,
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
        color: #00d9ff !important;
    }
    
    /* All text elements */
    p, div, span, li, label, a, button,
    .stApp p, .stApp div, .stApp span, .stApp li, .stApp label, .stApp a {
        color: #e2e8f0 !important;
    }
    
    /* Streamlit specific elements */
    .stMarkdown, .stMarkdown *,
    .stText, .stText *,
    .css-1v0mbdj, .css-1v0mbdj *,
    .css-16idsys, .css-16idsys *,
    .css-1544g2n, .css-1544g2n *,
    [data-testid="stMarkdownContainer"],
    [data-testid="stMarkdownContainer"] * {
        color: #e2e8f0 !important;
    }
    
    /* Sidebar specific styles */
    .css-1d391kg,
    .css-1d391kg *,
    .stSidebar,
    .stSidebar *,
    [data-testid="stSidebar"],
    [data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
        background-color: transparent !important;
    }
    
    /* Input and form elements in sidebar */
    .stSidebar .stNumberInput label,
    .stSidebar .stSlider label,
    .stSidebar .stRadio label,
    .stSidebar .stSelectbox label {
        color: #e2e8f0 !important;
    }
    
    /* Typography - Simplified */
    .main-header {
        color: #00d9ff !important;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        text-align: center;
        text-shadow: 0 0 10px rgba(0, 217, 255, 0.3);
    }
    
    .sub-header {
        color: #64748b !important;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Cyber Metrics Cards - Simplified */
    .cyber-metric {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%) !important;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        color: #e2e8f0 !important;
    }
    
    .cyber-metric * {
        color: #e2e8f0 !important;
    }
    
    /* Risk Level Styling - Simplified */
    .risk-low { 
        color: #00ff88 !important; 
        font-weight: 700;
        font-size: 1.5rem;
    }
    .risk-medium { 
        color: #fbbf24 !important; 
        font-weight: 700;
        font-size: 1.5rem;
    }
    .risk-high { 
        color: #f59e0b !important; 
        font-weight: 700;
        font-size: 1.5rem;
    }
    .risk-critical { 
        color: #ef4444 !important; 
        font-weight: 700;
        font-size: 1.5rem;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #0f172a 0%, #0b1224 100%) !important;
        border-right: 1px solid #334155 !important;
        box-shadow: 8px 0 24px rgba(2, 6, 23, 0.6) !important;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #0b1224 100%) !important;
        border-right: 1px solid #334155 !important;
        box-shadow: 8px 0 24px rgba(2, 6, 23, 0.6) !important;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding: 1.25rem 1rem 2rem 1rem !important;
    }
    
    /* Sidebar Text Visibility - All Elements */
    .css-1d391kg, .css-1d391kg * {
        color: #e2e8f0 !important;
    }
    
    .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3, .css-1d391kg h4 {
        color: #00d9ff !important;
    }
    
    .css-1d391kg p, .css-1d391kg span, .css-1d391kg div {
        color: #e2e8f0 !important;
    }
    
    /* Sidebar Input Elements */
    .css-1d391kg .stNumberInput label {
        color: #e2e8f0 !important;
    }
    
    .css-1d391kg .stSlider label {
        color: #e2e8f0 !important;
    }
    
    .css-1d391kg .stSelectbox label {
        color: #e2e8f0 !important;
    }
    
    .css-1d391kg .stRadio label {
        color: #e2e8f0 !important;
    }
    
    /* Sidebar Input Values */
    .css-1d391kg input {
        background: #1e293b !important;
        border: 1px solid #334155 !important;
        color: #e2e8f0 !important;
    }
    
    /* Sidebar Radio and Select Option Text */
    .css-1d391kg .stRadio > div {
        color: #e2e8f0 !important;
    }
    
    .css-1d391kg .stRadio > div > label {
        color: #e2e8f0 !important;
    }
    
    .css-1d391kg .stRadio > div > label > span {
        color: #e2e8f0 !important;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #00d9ff 0%, #0099cc 100%);
        color: #0a0e27 !important;
        border: none;
        border-radius: 12px;
        font-weight: 700;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        background: linear-gradient(135deg, #0099cc 0%, #00d9ff 100%);
    }

    /* Download button styling */
    [data-testid="stDownloadButton"] > button {
        background: linear-gradient(135deg, #00d9ff 0%, #0099cc 100%) !important;
        color: #0a0e27 !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        box-shadow: 0 6px 16px rgba(0, 217, 255, 0.2) !important;
    }

    [data-testid="stDownloadButton"] > button:hover {
        transform: translateY(-1px);
        background: linear-gradient(135deg, #0099cc 0%, #00d9ff 100%) !important;
    }
    
    /* Sidebar Button Override */
    .css-1d391kg .stButton > button {
        background: linear-gradient(135deg, #00d9ff 0%, #0099cc 100%);
        color: #0a0e27 !important;
        border: none;
        border-radius: 12px;
        font-weight: 700;
        width: 100%;
    }
    
    /* Streamlit Element Overrides */
    .stMarkdown {
        color: #e2e8f0 !important;
    }
    
    .stMarkdown * {
        color: #e2e8f0 !important;
    }
    
    /* Tab Content */
    .stTabs [data-baseweb="tab-panel"] {
        background: transparent;
        color: #e2e8f0 !important;
    }
    
    /* Metric containers */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 0.75rem 1rem;
        box-shadow: 0 8px 20px rgba(2, 6, 23, 0.35);
        transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
        color: #e2e8f0 !important;
    }

    [data-testid="metric-container"]:hover {
        transform: translateY(-2px);
        border-color: #00d9ff;
        box-shadow: 0 12px 28px rgba(0, 217, 255, 0.15);
    }

    /* Dashboard main cards - hover accent by position */
    .dashboard-metrics [data-testid="column"]:nth-of-type(1) [data-testid="metric-container"]:hover {
        border-color: #00ff88;
        box-shadow: 0 12px 28px rgba(0, 255, 136, 0.18);
    }

    .dashboard-metrics [data-testid="column"]:nth-of-type(2) [data-testid="metric-container"]:hover {
        border-color: #fbbf24;
        box-shadow: 0 12px 28px rgba(251, 191, 36, 0.18);
    }

    .dashboard-metrics [data-testid="column"]:nth-of-type(3) [data-testid="metric-container"]:hover {
        border-color: #ef4444;
        box-shadow: 0 12px 28px rgba(239, 68, 68, 0.2);
    }

    .dashboard-metrics [data-testid="column"]:nth-of-type(4) [data-testid="metric-container"]:hover {
        border-color: #00d9ff;
        box-shadow: 0 12px 28px rgba(0, 217, 255, 0.2);
    }
    
    [data-testid="metric-container"] * {
        color: #e2e8f0 !important;
    }

    /* KPI cards */
    .kpi-card {
        position: relative;
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 1.2rem 1.1rem;
        box-shadow: 0 8px 20px rgba(2, 6, 23, 0.35);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        min-height: 108px;
        margin-bottom: 0.75rem;
    }

    .kpi-card--compact {
        padding: 0.95rem 1rem;
        min-height: 96px;
    }

    .kpi-card--compact .kpi-label {
        font-size: 0.8rem;
    }

    .kpi-card--compact .kpi-value {
        font-size: 1.45rem;
    }

    .kpi-card::before {
        content: "";
        position: absolute;
        inset: 0;
        padding: 1px;
        border-radius: inherit;
        background: linear-gradient(135deg, #00d9ff 0%, #00ff88 45%, #fbbf24 75%, #ef4444 100%);
        -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        opacity: 0;
        transition: opacity 0.2s ease;
        pointer-events: none;
    }

    .kpi-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 28px rgba(0, 217, 255, 0.18);
    }

    .kpi-card:hover::before {
        opacity: 1;
    }

    .kpi-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 0.5rem;
        margin-bottom: 0.5rem;
        min-height: 22px;
    }

    .kpi-label {
        font-size: 0.85rem;
        font-weight: 600;
        color: #cbd5f5 !important;
    }

    .kpi-value {
        font-size: 1.7rem;
        font-weight: 700;
        color: #e2e8f0 !important;
        line-height: 1.1;
        letter-spacing: 0.2px;
    }

    .kpi-help {
        position: relative;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        border: 1px solid #334155;
        font-size: 0.75rem;
        color: #94a3b8 !important;
        cursor: default;
        background: rgba(15, 23, 42, 0.8);
    }

    .kpi-help::after {
        content: attr(data-tooltip);
        position: absolute;
        right: 0;
        top: -0.2rem;
        transform: translateY(-100%);
        background: #0f172a;
        color: #e2e8f0;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 0.35rem 0.55rem;
        font-size: 0.75rem;
        white-space: nowrap;
        opacity: 0;
        pointer-events: none;
        box-shadow: 0 8px 18px rgba(2, 6, 23, 0.4);
    }

    .kpi-help:hover::after {
        opacity: 1;
    }

    .intel-summary {
        color: #e2e8f0 !important;
        line-height: 1.6;
        font-size: 0.95rem;
    }

    .intel-value {
        background: transparent;
        color: #e2e8f0 !important;
        border: none;
        padding: 0;
        white-space: nowrap;
    }

    /* Tooltip theming for Streamlit help */
    [data-baseweb="tooltip"] {
        background: #0f172a !important;
        color: #e2e8f0 !important;
        border: 1px solid #334155 !important;
        box-shadow: 0 8px 18px rgba(2, 6, 23, 0.4) !important;
    }

    [data-baseweb="tooltip"] * {
        color: #e2e8f0 !important;
        background: transparent !important;
    }

    .stSlider [data-baseweb="tooltip"],
    .stSlider [role="tooltip"] {
        background: #0f172a !important;
        color: #e2e8f0 !important;
        border: 1px solid #334155 !important;
        box-shadow: 0 8px 18px rgba(2, 6, 23, 0.4) !important;
    }

    .stSlider [role="tooltip"] * {
        color: #e2e8f0 !important;
        background: transparent !important;
    }

    /* Slider info icon to match KPI help */
    .stSlider [data-testid="stWidgetInfo"],
    .stSlider button[aria-label="Open widget info"] {
        width: 18px !important;
        height: 18px !important;
        border-radius: 50% !important;
        border: 1px solid #334155 !important;
        background: rgba(15, 23, 42, 0.8) !important;
        color: #94a3b8 !important;
        padding: 0 !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        opacity: 1 !important;
        visibility: visible !important;
    }

    .stSlider [data-testid="stWidgetInfo"] svg,
    .stSlider button[aria-label="Open widget info"] svg {
        color: #94a3b8 !important;
        fill: #94a3b8 !important;
        width: 12px !important;
        height: 12px !important;
        opacity: 1 !important;
    }

    /* Widget info popover */
    [data-baseweb="popover"] {
        background: #0f172a !important;
        color: #e2e8f0 !important;
        border: 1px solid #334155 !important;
        box-shadow: 0 8px 18px rgba(2, 6, 23, 0.4) !important;
    }

    [data-baseweb="popover"] * {
        color: #e2e8f0 !important;
        background: transparent !important;
    }

    [data-testid="stTooltip"],
    [data-testid="stTooltip"] * {
        background: #0f172a !important;
        color: #e2e8f0 !important;
        border: 1px solid #334155 !important;
    }

    /* Alert styling - align with dark theme */
    [data-testid="stAlert"],
    .stAlert {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(30, 41, 59, 0.9) 100%) !important;
        border: 1px solid #334155 !important;
        border-left: 4px solid #00d9ff !important;
        box-shadow: 0 8px 18px rgba(2, 6, 23, 0.35) !important;
        color: #e2e8f0 !important;
    }

    [data-testid="stAlert"] > div,
    .stAlert > div {
        background: transparent !important;
    }

    [data-testid="stAlert"] [data-testid="stMarkdownContainer"],
    [data-testid="stAlert"] [data-testid="stMarkdownContainer"] * {
        color: #e2e8f0 !important;
    }

    [data-testid="stAlert"].stAlertSuccess,
    [data-testid="stAlert"].stAlert--success,
    .stAlert.stAlertSuccess,
    .stAlert.stAlert--success {
        border-left-color: #00ff88 !important;
    }

    [data-testid="stAlert"].stAlertWarning,
    [data-testid="stAlert"].stAlert--warning,
    .stAlert.stAlertWarning,
    .stAlert.stAlert--warning {
        border-left-color: #fbbf24 !important;
    }

    [data-testid="stAlert"].stAlertError,
    [data-testid="stAlert"].stAlert--error,
    .stAlert.stAlertError,
    .stAlert.stAlert--error {
        border-left-color: #ef4444 !important;
    }

    [data-testid="stAlert"].stAlertInfo,
    [data-testid="stAlert"].stAlert--info,
    .stAlert.stAlertInfo,
    .stAlert.stAlert--info {
        border-left-color: #38bdf8 !important;
    }
    
    /* Sidebar Markdown Override */
    .css-1d391kg .stMarkdown {
        color: #e2e8f0 !important;
    }
    
    .css-1d391kg .stMarkdown * {
        color: #e2e8f0 !important;
    }
    
    .css-1d391kg .stMarkdown h1, 
    .css-1d391kg .stMarkdown h2, 
    .css-1d391kg .stMarkdown h3, 
    .css-1d391kg .stMarkdown h4 {
        color: #00d9ff !important;
    }
    
    /* Additional Sidebar Input Styling */
    .css-1d391kg .stNumberInput > div > label {
        color: #e2e8f0 !important;
        font-weight: 500 !important;
    }
    
    .css-1d391kg .stSlider > label {
        color: #e2e8f0 !important;
        font-weight: 500 !important;
    }
    
    .css-1d391kg .stSlider > label > div {
        color: #e2e8f0 !important;
    }
    
    .css-1d391kg .stSelectbox > div > label {
        color: #e2e8f0 !important;
        font-weight: 500 !important;
    }
    
    .css-1d391kg .stTextInput > div > label {
        color: #e2e8f0 !important;
        font-weight: 500 !important;
    }
    
    .css-1d391kg div[data-testid="metric-container"] {
        color: #e2e8f0 !important;
    }
    
    .css-1d391kg div[data-testid="metric-container"] > div {
        color: #e2e8f0 !important;
    }
    
    /* Sidebar Selectbox Options */
    .css-1d391kg .stSelectbox > div[data-baseweb="select"] > div {
        background: #1e293b !important;
        color: #e2e8f0 !important;
        border: 1px solid #334155 !important;
    }
    
    .css-1d391kg .stSelectbox [role="option"] {
        background: #1e293b !important;
        color: #e2e8f0 !important;
    }
    
    /* Sidebar Slider Styling */
    .css-1d391kg .stSlider > div > div[data-testid="stSlider"] {
        color: #e2e8f0 !important;
    }
    
    .css-1d391kg .stSlider p {
        color: #e2e8f0 !important;
    }
    
    /* Additional typography fixes */
    .cyber-metric {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%) !important;
        border: 1px solid #334155 !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        text-align: center !important;
        color: #e2e8f0 !important;
    }
    
    .cyber-metric * {
        color: #e2e8f0 !important;
    }
    
    .cyber-metric h4 {
        color: #00d9ff !important;
        font-weight: bold !important;
    }
    
    /* Risk Level Colors */
    .risk-low { 
        color: #00ff88 !important; 
        font-weight: 700 !important;
        font-size: 1.5rem !important;
    }
    .risk-medium { 
        color: #fbbf24 !important; 
        font-weight: 700 !important;
        font-size: 1.5rem !important;
    }
    .risk-high { 
        color: #f59e0b !important; 
        font-weight: 700 !important;
        font-size: 1.5rem !important;
    }
    .risk-critical { 
        color: #ef4444 !important; 
        font-weight: 700 !important;
        font-size: 1.5rem !important;
    }
    
    /* Tab content */
    .stTabs [data-baseweb="tab-panel"] {
        background: transparent !important;
        color: #e2e8f0 !important;
    }
    
    .stTabs [data-baseweb="tab-panel"] * {
        color: #e2e8f0 !important;
    }

    /* Analysis tables */
    [data-testid="stDataFrame"] {
        position: relative;
        background: #0b1224 !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        overflow: hidden !important;
        box-shadow: 0 8px 20px rgba(2, 6, 23, 0.35) !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    [data-testid="stDataFrame"]::before {
        content: "";
        position: absolute;
        inset: 0;
        padding: 1px;
        border-radius: inherit;
        background: linear-gradient(135deg, #00d9ff 0%, #00ff88 40%, #fbbf24 70%, #ef4444 100%);
        -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        opacity: 0.4;
        pointer-events: none;
    }

    [data-testid="stDataFrame"]:hover {
        transform: translateY(-1px);
        box-shadow: 0 12px 26px rgba(0, 217, 255, 0.18) !important;
    }

    [data-testid="stDataFrame"] * {
        color: #e2e8f0 !important;
    }

    [data-testid="stDataFrame"] table {
        background: #0b1224 !important;
    }

    [data-testid="stDataFrame"] thead th {
        background: #111827 !important;
        color: #e2e8f0 !important;
        border-bottom: 1px solid #334155 !important;
        font-weight: 700 !important;
    }

    [data-testid="stDataFrame"] tbody td {
        background: #0b1224 !important;
        border-bottom: 1px solid #1f2937 !important;
        color: #e2e8f0 !important;
    }

    [data-testid="stDataFrame"] tbody tr:hover td {
        background: #111a2e !important;
    }

    /* Static tables */
    [data-testid="stTable"] {
        background: #0b1224 !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        overflow: hidden !important;
        box-shadow: 0 8px 20px rgba(2, 6, 23, 0.35) !important;
    }

    [data-testid="stTable"] table {
        background: #0b1224 !important;
        color: #e2e8f0 !important;
    }

    [data-testid="stTable"] thead th {
        background: #111827 !important;
        color: #e2e8f0 !important;
        border-bottom: 1px solid #334155 !important;
        font-weight: 700 !important;
    }

    [data-testid="stTable"] tbody td {
        background: #0b1224 !important;
        color: #e2e8f0 !important;
        border-bottom: 1px solid #1f2937 !important;
    }

    [data-testid="stTable"] tbody tr:hover td {
        background: #111a2e !important;
    }
</style>
""", unsafe_allow_html=True)

# Enhanced Header with Cyber Theme - Text Visibility Fixed
st.markdown("""
<div style="text-align: center; padding: 2rem 0; color: #e2e8f0;">
    <h1 style="color: #00d9ff !important; font-size: 3rem; font-weight: 700; margin: 0.5rem 0; text-shadow: 0 0 10px rgba(0, 217, 255, 0.3);">
        🛡️ CyberRisk Quantum
    </h1>
    <p style="color: #64748b !important; font-size: 1.1rem; margin: 0.5rem 0; letter-spacing: 0.05em;">
        ADVANCED CYBER RISK QUANTIFICATION PLATFORM
    </p>
    <div style="display: flex; justify-content: center; align-items: center; gap: 1rem; margin-top: 1rem;">
        <span style="color: #00d9ff !important; font-size: 0.9rem;">━━━</span>
        <span style="color: #64748b !important; font-size: 0.9rem; letter-spacing: 0.1em;">PYFAIR QUANTUM ENGINE</span>
        <span style="color: #00d9ff !important; font-size: 0.9rem;">━━━</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Status Bar - Text Visibility Fixed
st.markdown("""
<div style="background: linear-gradient(90deg, #1e293b 0%, #0f172a 100%); 
            padding: 0.5rem 1rem; 
            border-radius: 8px; 
            border: 1px solid #334155; 
            margin-bottom: 2rem;
            font-size: 0.85rem;
            display: flex;
            justify-content: space-between;
            align-items: center;">
    <span style="color: #00ff88 !important;">🟢 SYSTEM ONLINE</span>
    <span style="color: #64748b !important;">QUANTUM RISK ANALYTICS v2.0</span>
    <span style="color: #00d9ff !important;">🔒 SECURED</span>
</div>
""", unsafe_allow_html=True)

# Enhanced Sidebar with Cyber Theme - Text Visibility Fixed
st.sidebar.markdown("""
<div style="text-align: center; padding: 1.5rem 0; border-bottom: 1px solid #334155; margin-bottom: 1.5rem;">
    <h2 style="color: #00d9ff !important; font-size: 1.3rem; font-weight: 700; margin: 0;">
        ⚙️ THREAT MODELING CONSOLE
    </h2>
    <p style="color: #64748b !important; font-size: 0.8rem; margin: 0.5rem 0 0 0;">
        Configure Risk Parameters
    </p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); 
            padding: 1rem; 
            border-radius: 8px; 
            border: 1px solid #334155; 
            margin-bottom: 1rem;">
    <h4 style="color: #00d9ff !important; margin: 0 0 0.5rem 0; font-weight: bold;">🎯 Threat Event Frequency (TEF)</h4>
    <p style="color: #94a3b8 !important; font-size: 0.85rem; margin: 0; font-style: italic;">Attack attempt frequency per annum</p>
</div>
""", unsafe_allow_html=True)

tef_method = st.sidebar.radio("Input Method:", ["Range (PERT)", "Mean & Std Dev"], key="tef_method")

if tef_method == "Range (PERT)":
    tef_min = st.sidebar.number_input("TEF Min (per year)", min_value=0, value=10, help="Minimum threat attempts per year")
    tef_likely = st.sidebar.number_input("TEF Most Likely", min_value=0, value=50, help="Most likely number of attempts")
    tef_max = st.sidebar.number_input("TEF Max (per year)", min_value=0, value=200, help="Maximum threat attempts")
else:
    tef_mean = st.sidebar.number_input("TEF Mean (per year)", min_value=0.0, value=50.0)
    tef_std = st.sidebar.number_input("TEF Std Dev", min_value=0.1, value=20.0)

st.sidebar.markdown("""
<div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); 
            padding: 1rem; 
            border-radius: 8px; 
            border: 1px solid #334155; 
            margin-bottom: 1rem;">
    <h4 style="color: #fbbf24 !important; margin: 0 0 0.5rem 0; font-weight: bold;">🛡️ Vulnerability Surface (Vuln)</h4>
    <p style="color: #94a3b8 !important; font-size: 0.85rem; margin: 0; font-style: italic;">Success probability of threat exploitation</p>
</div>
""", unsafe_allow_html=True)

vuln_method = st.sidebar.radio("Input Method:", ["Range (Beta)", "Percentage"], key="vuln_method")

if vuln_method == "Range (Beta)":
    vuln_min = st.sidebar.slider("Vuln Min (%)", 0, 100, 10, help="Minimum vulnerability percentage") / 100
    vuln_likely = st.sidebar.slider("Vuln Most Likely (%)", 0, 100, 30, help="Most likely vulnerability percentage") / 100
    vuln_max = st.sidebar.slider("Vuln Max (%)", 0, 100, 60, help="Maximum vulnerability percentage") / 100
else:
    vuln_pct = st.sidebar.slider("Vulnerability (%)", 0, 100, 30, help="Single-point vulnerability estimate") / 100

st.sidebar.markdown("""
<div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); 
            padding: 1rem; 
            border-radius: 8px; 
            border: 1px solid #334155; 
            margin-bottom: 1rem;">
    <h4 style="color: #ef4444 !important; margin: 0 0 0.5rem 0; font-weight: bold;">💰 Primary Loss Magnitude</h4>
    <p style="color: #94a3b8 !important; font-size: 0.85rem; margin: 0; font-style: italic;">Direct financial impact per breach event</p>
</div>
""", unsafe_allow_html=True)

plm_method = st.sidebar.radio("Input Method:", ["Range (PERT)", "Mean & Std Dev"], key="plm_method")

if plm_method == "Range (PERT)":
    plm_min = st.sidebar.number_input("Min Loss ($)", min_value=0, value=10000, step=1000)
    plm_likely = st.sidebar.number_input("Most Likely Loss ($)", min_value=0, value=100000, step=5000)
    plm_max = st.sidebar.number_input("Max Loss ($)", min_value=0, value=1000000, step=10000)
else:
    plm_mean = st.sidebar.number_input("Mean Loss ($)", min_value=0, value=100000, step=5000)
    plm_std = st.sidebar.number_input("Loss Std Dev ($)", min_value=0, value=50000, step=1000)

st.sidebar.markdown("""
<div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); 
            padding: 1rem; 
            border-radius: 8px; 
            border: 1px solid #334155; 
            margin-bottom: 1rem;">
    <h4 style="color: #8b5cf6 !important; margin: 0 0 0.5rem 0; font-weight: bold;">📈 Secondary Loss Multiplier</h4>
    <p style="color: #94a3b8 !important; font-size: 0.85rem; margin: 0; font-style: italic;">Cascading impact amplification factor</p>
</div>
""", unsafe_allow_html=True)

slm_factor = st.sidebar.slider(
    "Secondary Loss Factor",
    0.0,
    3.0,
    0.5,
    0.1,
    help="Multiplier for indirect costs (reputation, legal, regulatory)"
)

# Enhanced Simulation Parameters
st.sidebar.markdown("""
<div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); 
            padding: 1rem; 
            border-radius: 8px; 
            border: 1px solid #334155; 
            margin-bottom: 1rem;">
    <h4 style="color: #00ff88 !important; margin: 0 0 0.5rem 0; font-weight: bold;">⚡ Quantum Simulation Engine</h4>
    <p style="color: #94a3b8 !important; font-size: 0.85rem; margin: 0; font-style: italic;">Monte Carlo computation parameters</p>
</div>
""", unsafe_allow_html=True)

n_simulations = st.sidebar.slider(
    "🔢 Simulation Iterations",
    1000,
    100000,
    10000,
    step=1000,
    help="Number of Monte Carlo iterations"
)
confidence_level = st.sidebar.slider(
    "📊 Confidence Interval (%)",
    80,
    99,
    95,
    help="Confidence level used for Value at Risk"
)

# Enhanced Run Button
st.sidebar.markdown("""
<div style="margin-top: 2rem; padding: 1rem; background: linear-gradient(135deg, rgba(0, 217, 255, 0.1) 0%, rgba(0, 153, 204, 0.1) 100%); 
            border: 1px solid #00d9ff; border-radius: 12px; text-align: center;">
    <p style="color: #00d9ff; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; margin: 0 0 0.5rem 0;">
        INITIATE QUANTUM ANALYSIS
    </p>
</div>
""", unsafe_allow_html=True)

run_simulation = st.sidebar.button("🚀 EXECUTE RISK SCAN", type="primary", use_container_width=True)

# Sidebar Footer
st.sidebar.markdown("""
<div style="position: fixed; bottom: 1rem; left: 1rem; right: 1rem; 
            background: rgba(30, 41, 59, 0.9); 
            padding: 0.5rem; 
            border-radius: 6px; 
            border: 1px solid #334155;
            text-align: center;
            backdrop-filter: blur(10px);">
    <p style="color: #64748b; font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; margin: 0;">
        🔒 SECURED BY QUANTUM ENCRYPTION
    </p>
</div>
""", unsafe_allow_html=True)

# Main content area
if run_simulation:
    with st.spinner("⚡ Executing Quantum Monte Carlo Analysis..."):
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
        
    # Analysis Results Header
    st.success(f"⚡ **QUANTUM ANALYSIS COMPLETE** - Monte Carlo simulation executed with {n_simulations:,} iterations")
    
    # Key Metrics Header
    st.markdown("### 📊 CYBER RISK METRICS DASHBOARD")
    st.markdown("<div class=\"dashboard-metrics\">", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(
            f"""
            <div class=\"kpi-card\">
                <div class=\"kpi-header\">
                    <div class=\"kpi-label\">💰 Mean ALE</div>
                    <div class=\"kpi-help\" data-tooltip=\"Expected annual loss\">i</div>
                </div>
                <div class=\"kpi-value\">${ale_mean:,.0f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            f"""
            <div class=\"kpi-card\">
                <div class=\"kpi-header\">
                    <div class=\"kpi-label\">📈 Median ALE</div>
                    <div class=\"kpi-help\" data-tooltip=\"50th percentile\">i</div>
                </div>
                <div class=\"kpi-value\">${ale_median:,.0f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown(
            f"""
            <div class=\"kpi-card\">
                <div class=\"kpi-header\">
                    <div class=\"kpi-label\">⚠️ VaR ({confidence_level}%)</div>
                    <div class=\"kpi-help\" data-tooltip=\"Value at risk\">i</div>
                </div>
                <div class=\"kpi-value\">${ale_var_value:,.0f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col4:
        st.markdown(
            f"""
            <div class=\"kpi-card\">
                <div class=\"kpi-header\">
                    <div class=\"kpi-label\">🎯 Threat Level</div>
                    <div class=\"kpi-help\" data-tooltip=\"Risk classification\">i</div>
                </div>
                <div class=\"kpi-value {risk_class}\">{risk_level}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.divider()
    
    # Analytics Dashboard
    st.markdown("### 🗺️ QUANTUM RISK ANALYTICS DASHBOARD")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 RISK DISTRIBUTION", 
        "🎯 ATTACK VECTORS", 
        "📈 THREAT CURVES", 
        "📄 INTEL REPORT"
    ])
    
    with tab1:
        st.markdown("#### 📊 Annual Loss Exposure Distribution")
        st.caption("Quantum Monte Carlo risk simulation analysis")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Enhanced ALE Distribution with Cybersecurity Theme
            fig_ale = go.Figure()
            fig_ale.add_trace(go.Histogram(
                x=ale_samples,
                nbinsx=100,
                name="ALE Distribution",
                marker=dict(
                    color='rgba(0, 217, 255, 0.7)',
                    line=dict(color='#00d9ff', width=1)
                ),
                hovertemplate='<b>Annual Loss</b>: $%{x:,.0f}<br><b>Frequency</b>: %{y}<extra></extra>'
            ))
            
            # Enhanced reference lines
            fig_ale.add_vline(
                x=ale_mean, 
                line_dash="dash", 
                line_color="#00ff88", 
                line_width=3,
                annotation_text=f"MEAN: ${ale_mean:,.0f}",
                annotation_position="top",
                annotation_font_color="#00ff88",
                annotation_font_size=12
            )
            fig_ale.add_vline(
                x=ale_var_value, 
                line_dash="dot", 
                line_color="#ef4444",
                line_width=3,
                annotation_text=f"VaR {confidence_level}%: ${ale_var_value:,.0f}",
                annotation_position="top",
                annotation_font_color="#ef4444",
                annotation_font_size=12
            )
            
            fig_ale.update_layout(
                title={
                    'text': "<b>Risk Distribution Analysis</b>",
                    'font': {'color': '#e2e8f0', 'size': 16}
                },
                xaxis={
                    'title': {'text': "Annual Loss Exposure ($)", 'font': {'color': '#94a3b8'}},
                    'color': '#94a3b8',
                    'gridcolor': '#334155',
                    'tickformat': '$,.0f'
                },
                yaxis={
                    'title': {'text': "Simulation Frequency", 'font': {'color': '#94a3b8'}},
                    'color': '#94a3b8',
                    'gridcolor': '#334155'
                },
                plot_bgcolor='rgba(15, 23, 42, 0.8)',
                paper_bgcolor='rgba(15, 23, 42, 0.8)',
                font=dict(color='#e2e8f0'),
                height=500,
                margin=dict(t=50, b=50, l=60, r=60)
            )
            st.plotly_chart(fig_ale, use_container_width=True)
        
        with col2:
            # Risk Metrics Summary
            st.markdown("##### 🎯 Risk Metrics Summary")
            
            stats_metrics = [
                ("Mean", f"${ale_mean:,.0f}", "#00ff88"),
                ("Median", f"${ale_median:,.0f}", "#fbbf24"),
                ("Std Dev", f"${ale_std:,.0f}", "#8b5cf6"),
                ("Minimum", f"${ale_min:,.0f}", "#64748b"),
                ("Maximum", f"${ale_max:,.0f}", "#ef4444"),
                ("Range", f"${ale_max - ale_min:,.0f}", "#94a3b8")
            ]
            
            stats_df = pd.DataFrame({
                "Metric": [m for m, _, _ in stats_metrics],
                "Value": [v for _, v, _ in stats_metrics]
            })
            st.dataframe(stats_df, use_container_width=True, hide_index=True)

            st.markdown("##### 🎯 Percentiles")
            percentiles = [50, 75, 90, 95, 99]
            percentile_rows = []
            for p in percentiles:
                val = np.percentile(ale_samples, p)
                percentile_rows.append({
                    "Percentile": f"{p}th",
                    "Value": f"${val:,.0f}"
                })
            percentiles_df = pd.DataFrame(percentile_rows)
            st.dataframe(percentiles_df, use_container_width=True, hide_index=True)
    
    with tab2:
        st.markdown("#### 🎯 Attack Vector Component Analysis")
        st.caption("Detailed breakdown of threat surface components")
        
        # Enhanced component visualization with cyber theme
        fig_components = make_subplots(
            rows=2, cols=2,
            subplot_titles=("Loss Event Frequency", "Threat Event Frequency", 
                          "Vulnerability Surface", "Loss Magnitude"),
            specs=[[{'type': 'histogram'}, {'type': 'histogram'}],
                   [{'type': 'histogram'}, {'type': 'histogram'}]]
        )
        
        # Enhanced color scheme for cyber theme
        colors = ['#00d9ff', '#00ff88', '#fbbf24', '#ef4444']
        
        fig_components.add_trace(
            go.Histogram(
                x=lef_samples, 
                name="LEF", 
                marker=dict(color=colors[0], opacity=0.7, line=dict(color=colors[0], width=1)), 
                nbinsx=50,
                hovertemplate='<b>Events/Year</b>: %{x:.2f}<br><b>Count</b>: %{y}<extra></extra>'
            ),
            row=1, col=1
        )
        fig_components.add_trace(
            go.Histogram(
                x=tef_samples, 
                name="TEF", 
                marker=dict(color=colors[1], opacity=0.7, line=dict(color=colors[1], width=1)), 
                nbinsx=50,
                hovertemplate='<b>Attempts/Year</b>: %{x:.0f}<br><b>Count</b>: %{y}<extra></extra>'
            ),
            row=1, col=2
        )
        fig_components.add_trace(
            go.Histogram(
                x=vuln_samples, 
                name="Vuln", 
                marker=dict(color=colors[2], opacity=0.7, line=dict(color=colors[2], width=1)), 
                nbinsx=50,
                hovertemplate='<b>Probability</b>: %{x:.2%}<br><b>Count</b>: %{y}<extra></extra>'
            ),
            row=2, col=1
        )
        fig_components.add_trace(
            go.Histogram(
                x=lm_samples, 
                name="LM", 
                marker=dict(color=colors[3], opacity=0.7, line=dict(color=colors[3], width=1)), 
                nbinsx=50,
                hovertemplate='<b>Loss</b>: $%{x:,.0f}<br><b>Count</b>: %{y}<extra></extra>'
            ),
            row=2, col=2
        )
        
        fig_components.update_layout(
            height=700, 
            showlegend=False,
            plot_bgcolor='rgba(15, 23, 42, 0.8)',
            paper_bgcolor='rgba(15, 23, 42, 0.8)',
            font=dict(color='#e2e8f0'),
            margin=dict(t=80, b=60, l=60, r=60)
        )
        
        # Update subplot titles with cyber theme
        for i, annotation in enumerate(fig_components['layout']['annotations']):
            annotation['font']['color'] = '#00d9ff'
            annotation['font']['size'] = 14
        
        # Update axes
        fig_components.update_xaxes(title_text="Events/Year", row=1, col=1, color='#94a3b8', gridcolor='#334155')
        fig_components.update_xaxes(title_text="Attempts/Year", row=1, col=2, color='#94a3b8', gridcolor='#334155')
        fig_components.update_xaxes(title_text="Success Probability", row=2, col=1, color='#94a3b8', gridcolor='#334155')
        fig_components.update_xaxes(title_text="Financial Impact ($)", row=2, col=2, color='#94a3b8', gridcolor='#334155')
        fig_components.update_yaxes(color='#94a3b8', gridcolor='#334155')
        
        st.plotly_chart(fig_components, use_container_width=True)
        
        # Enhanced summary with cyber theme
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### 📻 Frequency Metrics")
            st.markdown(
                f"""
                <div class=\"kpi-card kpi-card--compact\">
                    <div class=\"kpi-header\">
                        <div class=\"kpi-label\">TEF Mean</div>
                        <div class=\"kpi-help\" data-tooltip=\"Average threat attempts per year\">i</div>
                    </div>
                    <div class=\"kpi-value\">{np.mean(tef_samples):.2f} attempts/year</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                f"""
                <div class=\"kpi-card kpi-card--compact\">
                    <div class=\"kpi-header\">
                        <div class=\"kpi-label\">Vulnerability Rate</div>
                        <div class=\"kpi-help\" data-tooltip=\"Average probability of success\">i</div>
                    </div>
                    <div class=\"kpi-value\">{np.mean(vuln_samples)*100:.2f}%</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                f"""
                <div class=\"kpi-card kpi-card--compact\">
                    <div class=\"kpi-header\">
                        <div class=\"kpi-label\">LEF Mean</div>
                        <div class=\"kpi-help\" data-tooltip=\"Expected loss events per year\">i</div>
                    </div>
                    <div class=\"kpi-value\">{np.mean(lef_samples):.2f} events/year</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        with col2:
            st.markdown("##### 💰 Loss Magnitude")
            st.markdown(
                f"""
                <div class=\"kpi-card kpi-card--compact\">
                    <div class=\"kpi-header\">
                        <div class=\"kpi-label\">Primary Loss</div>
                        <div class=\"kpi-help\" data-tooltip=\"Direct financial impact per event\">i</div>
                    </div>
                    <div class=\"kpi-value\">${np.mean(plm_samples):,.0f}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                f"""
                <div class=\"kpi-card kpi-card--compact\">
                    <div class=\"kpi-header\">
                        <div class=\"kpi-label\">Secondary Loss</div>
                        <div class=\"kpi-help\" data-tooltip=\"Indirect costs per event\">i</div>
                    </div>
                    <div class=\"kpi-value\">${np.mean(slm_samples):,.0f}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                f"""
                <div class=\"kpi-card kpi-card--compact\">
                    <div class=\"kpi-header\">
                        <div class=\"kpi-label\">Total Loss/Event</div>
                        <div class=\"kpi-help\" data-tooltip=\"Primary + secondary loss per event\">i</div>
                    </div>
                    <div class=\"kpi-value\">${np.mean(lm_samples):,.0f}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
    
    with tab3:
        st.markdown("#### 📈 Threat Probability Exceedance Curves")
        st.caption("Advanced probability analysis for loss threshold assessment")
        
        # Calculate exceedance probabilities
        sorted_ale = np.sort(ale_samples)
        exceedance_prob = np.arange(len(sorted_ale), 0, -1) / len(sorted_ale) * 100
        
        # Enhanced exceedance curve with cyber theme
        fig_exceed = go.Figure()
        
        # Main curve with gradient fill
        fig_exceed.add_trace(go.Scatter(
            x=sorted_ale,
            y=exceedance_prob,
            mode='lines',
            name='Exceedance Probability',
            line=dict(color='#00d9ff', width=4),
            fill='tozeroy',
            fillcolor='rgba(0, 217, 255, 0.2)',
            hovertemplate='<b>Loss Threshold</b>: $%{x:,.0f}<br><b>Exceedance Probability</b>: %{y:.2f}%<extra></extra>'
        ))
        
        # Enhanced reference lines with labels
        reference_probs = [1, 5, 10, 50]
        reference_colors = ['#ef4444', '#f59e0b', '#fbbf24', '#00ff88']
        
        for i, prob in enumerate(reference_probs):
            loss_val = np.percentile(ale_samples, 100 - prob)
            
            # Horizontal line
            fig_exceed.add_hline(
                y=prob, 
                line_dash="dot", 
                line_color=reference_colors[i], 
                line_width=2,
                opacity=0.7,
                annotation_text=f"{prob}% Risk",
                annotation_position="right",
                annotation_font_color=reference_colors[i]
            )
            
            # Vertical line
            fig_exceed.add_vline(
                x=loss_val, 
                line_dash="dot", 
                line_color=reference_colors[i], 
                line_width=2,
                opacity=0.7,
                annotation_text=f"${loss_val:,.0f}",
                annotation_position="top",
                annotation_font_color=reference_colors[i]
            )
        
        fig_exceed.update_layout(
            title={
                'text': "<b>Loss Exceedance Probability Analysis</b>",
                'font': {'color': '#e2e8f0', 'size': 16}
            },
            xaxis={
                'title': {'text': "Annual Loss Threshold ($)", 'font': {'color': '#94a3b8'}},
                'type': "log",
                'color': '#94a3b8',
                'gridcolor': '#334155',
                'tickformat': '$,.0f'
            },
            yaxis={
                'title': {'text': "Probability of Exceedance (%)", 'font': {'color': '#94a3b8'}},
                'color': '#94a3b8',
                'gridcolor': '#334155',
                'range': [0, 100]
            },
            plot_bgcolor='rgba(15, 23, 42, 0.8)',
            paper_bgcolor='rgba(15, 23, 42, 0.8)',
            font=dict(color='#e2e8f0'),
            height=500,
            margin=dict(t=50, b=50, l=60, r=60),
            showlegend=False
        )
        
        st.plotly_chart(fig_exceed, use_container_width=True)
        
        # Critical risk thresholds
        st.markdown("#### 🎯 Critical Risk Thresholds")
        
        col1, col2, col3 = st.columns(3)
        
        thresholds = [
            ("1% CRITICAL", 99, "#ef4444", "🔴"),
            ("5% HIGH RISK", 95, "#f59e0b", "🟠"),
            ("10% MODERATE", 90, "#fbbf24", "🟡")
        ]
        
        for i, (label, percentile, color, emoji) in enumerate(thresholds):
            value = np.percentile(ale_samples, percentile)
            with [col1, col2, col3][i]:
                st.markdown(
                    f"""
                    <div class=\"kpi-card kpi-card--compact\">
                        <div class=\"kpi-header\">
                            <div class=\"kpi-label\">{emoji} {label}</div>
                            <div class=\"kpi-help\" data-tooltip=\"{100-percentile}% chance of exceeding\">i</div>
                        </div>
                        <div class=\"kpi-value\">${value:,.0f}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    
    with tab4:
        st.markdown("#### 📄 Cybersecurity Risk Intelligence Report")
        st.caption("Comprehensive threat assessment and risk analysis documentation")
        
        # Executive summary
        summary_html = (
            f"<div class=\"intel-summary\">"
            f"Based on {n_simulations:,} Monte Carlo simulations using the PyFair methodology, "
            f"the estimated Annual Loss Exposure (ALE) is "
            f"<span class=\"intel-value\">${ale_mean:,.0f} (mean)</span> with a "
            f"<span class=\"intel-value\">{confidence_level}%</span> Value at Risk (VaR) of "
            f"<span class=\"intel-value\">${ale_var_value:,.0f}</span>. "
            f"There is a <span class=\"intel-value\">{confidence_level}%</span> probability that annual losses will not exceed "
            f"<span class=\"intel-value\">${ale_var_value:,.0f}</span>, and a "
            f"<span class=\"intel-value\">{100-confidence_level}%</span> chance they could be higher."
            f"</div>"
        )

        if risk_level in {"High", "Critical"}:
            st.warning(f"**Threat Classification:** {risk_level.upper()}")
        elif risk_level == "Medium":
            st.info(f"**Threat Classification:** {risk_level.upper()}")
        else:
            st.success(f"**Threat Classification:** {risk_level.upper()}")

        st.markdown(summary_html, unsafe_allow_html=True)
        
        # Input summary
        st.markdown("#### ⚙️ Threat Model Configuration")
        
        # Enhanced input parameters table
        input_data = {
            "Parameter": ["Threat Event Frequency", "Vulnerability Surface", "Primary Loss Impact", "Secondary Loss Amplifier", "Simulation Iterations"],
            "Value": [
                f"{np.mean(tef_samples):.1f} attempts/year",
                f"{np.mean(vuln_samples)*100:.1f}%",
                f"${np.mean(plm_samples):,.0f}",
                f"{slm_factor}x multiplier",
                f"{n_simulations:,} iterations"
            ],
            "Description": [
                "Annual frequency of threat actor attempts",
                "Probability of successful exploitation",
                "Direct financial impact per incident",
                "Indirect cost multiplication factor",
                "Monte Carlo simulation sample size"
            ]
        }
        
        input_df = pd.DataFrame(input_data)
        
        st.dataframe(input_df, use_container_width=True, hide_index=True)
        
        # Results summary
        st.markdown("#### 📊 Quantum Risk Simulation Results")
        
        results_data = {
            "Risk Metric": ["Mean ALE", "Median ALE", "Standard Deviation", "Minimum Loss", "Maximum Loss", 
                      f"VaR ({confidence_level}%)", "50th Percentile", "75th Percentile", 
                      "90th Percentile", "95th Percentile", "99th Percentile"],
            "Financial Impact": [
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
            ],
            "Risk Level": [
                "🟢 Expected", "🟡 Median", "🔵 Volatility", "🟢 Best Case", "🔴 Worst Case",
                "🔴 High Risk", "🟡 Moderate", "🟠 Elevated", "🟠 High", "🔴 Critical", "🔴 Extreme"
            ]
        }
        
        results_df = pd.DataFrame(results_data)
        st.dataframe(results_df, use_container_width=True, hide_index=True)
        
        # Export section
        st.markdown("#### 📡 Data Export & Forensics")
        
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
        
        col1, col2 = st.columns(2)
        with col1:
            st.caption("Simulation data export")
            st.download_button(
                label="📊 Download Full Dataset",
                data=csv,
                file_name=f"crq_quantum_analysis_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        with col2:
            # Export summary stats
            summary_data = {
                'Metric': ['Mean_ALE', 'VaR_95', 'Risk_Level', 'Simulation_Count'],
                'Value': [ale_mean, ale_var_value, risk_level, n_simulations]
            }
            summary_csv = pd.DataFrame(summary_data).to_csv(index=False)
            
            st.caption("Executive summary export")
            
            st.download_button(
                label="📈 Download Summary Report",
                data=summary_csv,
                file_name=f"crq_executive_summary_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        # Risk management recommendations
        st.markdown("#### 🛡️ Cybersecurity Response Matrix")

        if risk_level == "Critical":
            st.error("🚨 **Critical Threat Alert** — Immediate action required")
            st.markdown(
                "- ⚡ Deploy emergency incident response team immediately\n"
                "- 🛡️ Implement maximum security controls and monitoring\n"
                "- 💰 Secure comprehensive cyber insurance coverage\n"
                "- 🎯 Execute complete vulnerability remediation program\n"
                "- 📄 Prepare board-level risk briefing documentation"
            )
        elif risk_level == "High":
            st.warning("⚠️ **High Priority Actions** — Enhanced security measures required")
            st.markdown(
                "- 🔄 Review and enhance existing security control framework\n"
                "- 💰 Evaluate comprehensive cyber insurance options\n"
                "- 🎯 Conduct targeted security awareness training\n"
                "- 📈 Implement enhanced threat monitoring systems\n"
                "- 📅 Schedule quarterly risk assessment reviews"
            )
        elif risk_level == "Medium":
            st.info("🟡 **Moderate Risk Management** — Standard security protocols")
            st.markdown(
                "- 🛡️ Maintain current security posture and controls\n"
                "- 📈 Conduct regular security assessment cycles\n"
                "- 🔍 Monitor evolving threat landscape intelligence\n"
                "- 📅 Review security controls on a quarterly basis\n"
                "- 📊 Maintain risk monitoring dashboard"
            )
        else:
            st.success("🟢 **Acceptable Risk Level** — Baseline security status")
            st.markdown(
                "- ✅ Risk within acceptable organizational tolerance\n"
                "- 📈 Continue standard security monitoring protocols\n"
                "- 🛡️ Maintain established security baseline controls\n"
                "- 📅 Schedule annual comprehensive risk assessment\n"
                "- 📊 Monitor threat intelligence for emerging risks"
            )

else:
    # Landing page
    st.markdown("## 🔮 Quantum Cyber Risk Intelligence")
    st.caption("Advanced PyFair Threat Quantification Platform")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 🎯 Mission Objective")
        st.write(
            "This platform implements the Factor Analysis of Information Risk (PyFair) methodology "
            "to help cybersecurity professionals quantify cyber threat exposure in precise financial terms."
        )

        st.markdown("### ⚡ Quantum Analysis Engine")
        st.markdown(
            "1. **Threat Profiling** — define attack frequency patterns (TEF).\n"
            "2. **Vulnerability Mapping** — assess exploitation probability (Vuln).\n"
            "3. **Loss Event Modeling** — calculate LEF = TEF × Vulnerability.\n"
            "4. **Financial Impact** — estimate primary + secondary losses.\n"
            "5. **Quantum Simulation** — execute Monte Carlo analysis.\n"
            "6. **Risk Intelligence** — generate ALE = LEF × Loss Magnitude."
        )

        st.markdown("### 📊 PyFair Quantum Components")
        st.markdown(
            "- **TEF**: Threat Event Frequency (attack attempts/year)\n"
            "- **Vuln**: Vulnerability Surface (success probability)\n"
            "- **LEF**: Loss Event Frequency (TEF × Vuln)\n"
            "- **PLM**: Primary Loss Magnitude (direct costs)\n"
            "- **SLM**: Secondary Loss Magnitude (indirect costs)\n"
            "- **ALE**: Annual Loss Exposure (expected annual loss)"
        )

        st.markdown("### ✨ Advanced Capabilities")
        st.markdown(
            "- ⚙️ Monte Carlo simulations (up to 100K)\n"
            "- 📈 Multiple distributions (PERT, Beta, Normal)\n"
            "- 🎯 Configurable Value at Risk (VaR)\n"
            "- 🗺️ Interactive dashboards and real-time visualization\n"
            "- 📉 Exceedance curves and probability analysis\n"
            "- 📄 Export data and executive reports"
        )

    with col2:
        st.markdown("### 🚀 Quantum Protocol")
        st.markdown(
            "1. Configure parameters (threat frequency & vulnerability).\n"
            "2. Define loss magnitude (primary + secondary).\n"
            "3. Execute analysis (run simulation).\n"
            "4. Review intelligence (risk dashboard).\n"
            "5. Export reports (data & findings)."
        )

        st.markdown("### 📊 Intelligence Applications")
        st.markdown(
            "- 🎯 Threat assessment\n"
            "- 💰 Budget justification\n"
            "- 🛡️ Insurance planning\n"
            "- 📄 Compliance reporting\n"
            "- 🏢 Executive briefings"
        )

        st.info(
            "**Security Disclaimer:** Results are quantitative estimates based on input parameters and "
            "subject to uncertainty. Validate assumptions with cybersecurity experts and update assessments "
            "as the threat landscape evolves."
        )

# Simple Footer
st.divider()
st.caption("© 2026 CyberRisk Quantum • Advanced Threat Intelligence Platform")
