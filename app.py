import streamlit as st
import pandas as pd
import time

# Ensure this import matches your local file structure
from loan_model import LoanApprovalApp

# 1. Page Configuration - Sets browser tab title, icon, and expands layout
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cache the model loading to prevent reloading on every interaction
@st.cache_resource
def load_model():
    return LoanApprovalApp()

try:
    model = load_model()
except Exception as e:
    st.error(f"Error loading model: {e}. Please ensure 'loan_model.py' is in the same directory.")

# Header Section
st.title("🏦 Loan Approval Prediction Portal")
st.markdown("""
Welcome to the intelligent Loan Eligibility Checker. Please fill out the applicant's profile, 
asset declarations, and loan requirements below to instantly evaluate their application.
""")
st.divider()

# 2. Form Setup - Prevents app refresh on every keystroke
with st.form("loan_application_form"):
    
    # Create 3 columns for better screen real estate usage
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.subheader("👤 Applicant Profile")
        
        cibil_score = st.number_input(
            "CIBIL Score",
            min_value=300, max_value=900, value=300, step=1,
            help="Credit score typically ranges from 300 to 900."
        )
        
        income_annum = st.number_input(
            "Annual Income ($)",
            min_value=0.0, value=0.0, step=1000.0, format="%.2f"
        )
        
        education = st.selectbox(
            "Education Level",
            ["Graduate", "Not Graduate"]
        )
        
        self_employed = st.selectbox(
            "Self Employed",
            ["Yes", "No"]
        )
        
        no_of_dependents = st.number_input(
            "Number of Dependents",
            min_value=0, max_value=20, value=0, step=1
        )

    with col2:
        st.subheader("💎 Assets Information")
        
        residential_assets_value = st.number_input(
            "Residential Assets Value ($)",
            min_value=0.0, value=0.0, step=5000.0, format="%.2f"
        )
        
        commercial_assets_value = st.number_input(
            "Commercial Assets Value ($)",
            min_value=0.0, value=0.0, step=5000.0, format="%.2f"
        )
        
        luxury_assets_value = st.number_input(
            "Luxury Assets Value ($)",
            min_value=0.0, value=0.0, step=1000.0, format="%.2f"
        )
        
        bank_asset_value = st.number_input(
            "Bank Asset Value ($)",
            min_value=0.0, value=0.0, step=1000.0, format="%.2f"
        )

    with col3:
        st.subheader("📝 Loan Details")
        
        loan_amount = st.number_input(
            "Loan Amount Requested ($)",
            min_value=0.0, value=0.0, step=1000.0, format="%.2f"
        )
        
        loan_term = st.number_input(
            "Loan Term (Months/Years)",
            min_value=1, value=1, step=1,
            help="Duration over which the loan will be repaid."
        )
        
        # Add some empty space to push the button down nicely
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        
        # The submit button for the form
        submit_button = st.form_submit_button(
            "Evaluate Loan Application 🚀", 
            use_container_width=True
        )

# 3. Processing and Results
if submit_button:
    
    # Prepare the dictionary with exact keys expected by the backend
    data = {
        "no_of_dependents": no_of_dependents,
        "education": education,
        "self_employed": self_employed,
        "income_annum": income_annum,
        "loan_amount": loan_amount,
        "loan_term": loan_term,
        "cibil_score": cibil_score,
        "residential_assets_value": residential_assets_value,
        "commercial_assets_value": commercial_assets_value,
        "luxury_assets_value": luxury_assets_value,
        "bank_asset_value": bank_asset_value
    }

    applicant_df = pd.DataFrame([data])
    
    # Visual feedback while model calculates
    with st.spinner("Analyzing applicant profile and running risk assessment models..."):
        # Optional: slight delay to make the spinner noticeable if inference is instantaneous
        time.sleep(0.75) 
        
        try:
            result = model.two_stage_predict(applicant_df)
            
            st.divider()
            st.subheader("📊 Assessment Results")
            
            # 4. Display Results Beautifully
            if result["approve"] == 1:
                st.balloons()
                
                success_col1, success_col2 = st.columns([1, 2])
                
                with success_col1:
                    st.success("✅ Application Approved!")
                    
                with success_col2:
                    # Using metric for a clean, dashboard-like look
                    st.metric(
                        label="Maximum Recommended Loan Amount",
                        value=f"${result['regression_prediction']:,.2f}",
                        delta="Eligible"
                    )
            else:
                st.error("❌ Application Rejected")
                st.info(
                    "The applicant's current profile does not meet the risk thresholds for approval. "
                    "Consider reviewing the CIBIL score, income-to-loan ratio, or asset declarations."
                )
                
        except Exception as e:
            st.error(f"An error occurred during prediction: {str(e)}")