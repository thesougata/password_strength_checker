import streamlit as st

st.title("💻 Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if password:
    uppercase=False
    lowercase=False
    digit=False
    special_char=False

    for ch in password:
        if ch.isupper():
            uppercase=True
        elif ch.islower():
            lowercase=True
        elif ch.isdigit():
            digit=True
        elif not ch.isspace():
            special_char=True

    issues=[]
    if not uppercase:
        issues.append("uppercase letter")
    if not lowercase:
        issues.append("lowercase letter")
    if not digit:
        issues.append("minimum one digit")
    if not special_char:
        issues.append("minimum one special character")
    if len(password)<8:
        issues.append("minimum length must be 8")

    score = 5 - len(issues)
    st.write("Score:", score, "/5")

    if score == 5:
        st.success("💪 Strong Password")
    elif score >= 3:
        st.warning("😐 Medium Password")
    else:
        st.error("❌ Weak Password")

    if issues:
        st.info("Missing: " + ", ".join(issues))
