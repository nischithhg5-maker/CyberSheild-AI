import streamlit as st

st.set_page_config(
    page_title="CyberShield AI",
    page_icon="🛡️"
)

st.title("🛡️ CyberShield AI")
st.subheader("AI-Powered Scam and Phishing Detector")

st.write(
    "Check suspicious messages before clicking links "
    "or sharing personal information."
)

st.info("Demo version: risk scoring uses simple rules.")

message = st.text_area("Paste a suspicious message here:")

if st.button("Analyze Message"):
    if not message.strip():
        st.warning("Please enter a message first.")
    else:
        suspicious_words = [
            "urgent",
            "verify your account",
            "password",
            "click here",
            "prize",
            "bank details",
            "otp",
            "won",
            "claim now",
            "limited time"
        ]

        text = message.lower()

        found = [
            word for word in suspicious_words
            if word in text
        ]

        # Calculate the risk score
        risk_score = min(len(found) * 20,100)

        # Urgency and threat detection
if any(word in text for word in ["immediately", "today", "urgent", "within 24 hours"]):
    risk_score += 20

# Bank account threats
if any(word in text for word in ["account will be blocked", "account suspended", "verify your details"]):
    risk_score += 40

# OTP requests
if "otp" in text or "one-time password" in text:
    risk_score += 40

if "share your otp" in text or "send your otp" in text:
    risk_score += 30

# Suspicious links
if "http://" in text or "https://" in text or "click this link" in text:
    risk_score += 20

# Keep the score between 0 and 100
risk_score = min(risk_score, 100)
        
st.divider()
st.subheader("📊 Security Analysis")

st.metric("Risk Score", f"{risk_score}/100")
st.progress(risk_score / 100)

if risk_score >= 60:
    st.error("🔴 HIGH RISK - Be extremely cautious.")
elif risk_score >= 30:
    st.warning("🟠 MEDIUM RISK - Check carefully.")
else:
    st.success("🟢 LOW RISK - Few warning signs detected.")

if found:
    st.write("Warning signs detected:")
    st.write(", ".join(found))
else:
    st.write("No listed warning words detected.")

if risk_score >= 30:
    st.info(
        "Do not click suspicious links or share "
        "passwords, bank details, or OTPs. "
        "Verify the sender through an official channel."
    )
else:
    st.caption(
        "A low score does not guarantee the message is safe."
    )
