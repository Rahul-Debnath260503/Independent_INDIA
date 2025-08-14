import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta
import random

# Flag URL (PNG for better rendering)
FLAG_URL = "https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/1920px-Flag_of_India.svg.png"

# Extended 50+ Motivational Patriotic Messages
messages = [
    "🇮🇳 Be the change you wish to see in Bharat.",
    "🇮🇳 Our freedom was not gifted, it was earned — cherish it.",
    "🇮🇳 Serve your country in every little act you do.",
    # ... rest of your 50+ messages
]

def leap_years_count(start_year, end_year):
    return sum(1 for y in range(start_year, end_year + 1)
               if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0))

st.set_page_config(page_title="Independent Bharat", page_icon="🇮🇳", layout="centered")

# Show big flag
st.image(FLAG_URL, width=300)

st.title("Happy Independence Day 🎉")
now = datetime.now()

birth_date = st.date_input("Enter your birthdate", min_value=datetime(1900, 1, 1).date())
birth_datetime = datetime.combine(birth_date, datetime.min.time())

independence_day = datetime(1947, 8, 15)

# Independence years
independence_years = now.year - 1947
if (now.month, now.day) < (8, 15):
    independence_years -= 1

# Life stats
years_completed = now.year - birth_datetime.year
if (now.month, now.day) < (birth_datetime.month, birth_datetime.day):
    years_completed -= 1

months_completed = years_completed * 12 + (now.month - birth_datetime.month)
if now.day < birth_datetime.day:
    months_completed -= 1

days_since_birth = (now - birth_datetime).days
decades = years_completed // 10
extra_years_in_decade = years_completed % 10
leap_years = leap_years_count(birth_datetime.year, now.year)
seconds_since = int((now - birth_datetime).total_seconds())
minutes_since = seconds_since // 60
hours_since = minutes_since // 60

days_after_independence = (birth_datetime - independence_day).days
independent_days_lived = max(0, (now - max(birth_datetime, independence_day)).days)

if days_after_independence >= 0:
    before_birth_diff = relativedelta(birth_datetime, independence_day)
else:
    before_birth_diff = relativedelta(independence_day, birth_datetime)

independent_life_diff = relativedelta(now, max(birth_datetime, independence_day))

# HEADER
st.subheader(f"🎊 Celebrating {independence_years}th Independence of Motherland INDIA 🇮🇳")

# Section 4 - Message
st.markdown("### MESSAGE FROM THE MOTHERLAND")
st.markdown(f"<h2>{random.choice(messages)}</h2>", unsafe_allow_html=True)

# Section 2 - Before Birth
st.markdown("### DAYS PASSED BEFORE YOUR BIRTH")
if days_after_independence >= 0:
    st.markdown(f"<h2>India was independent for {before_birth_diff.years} years, "
                f"{before_birth_diff.months} months, and {before_birth_diff.days} days before you were born.</h2>",
                unsafe_allow_html=True)
else:
    st.markdown(f"<h2>You were born {-days_after_independence} days before India’s Independence "
                f"({before_birth_diff.years} years, {before_birth_diff.months} months, {before_birth_diff.days} days).</h2>",
                unsafe_allow_html=True)

# Section 3 - Days lived in Independent Bharat
st.markdown("### DAYS YOU HAVE LIVED IN INDEPENDENT BHARAT")
st.markdown(f"<h2>You have spent {independent_days_lived} days "
            f"({independent_life_diff.years} years, {independent_life_diff.months} months, {independent_life_diff.days} days) "
            f"in Independent Bharat 🇮🇳</h2>", unsafe_allow_html=True)

# Section 1 - Birth Information
st.markdown("### YOUR BIRTH INFORMATION")
st.markdown(f"<h2>Years Completed: {years_completed} years</h2>", unsafe_allow_html=True)
st.markdown(f"<h2>Decades: {decades} decades and {extra_years_in_decade} years</h2>", unsafe_allow_html=True)
st.markdown(f"<h2>Months Completed: {months_completed}</h2>", unsafe_allow_html=True)
st.markdown(f"<h2>Days Since Birth: {days_since_birth}</h2>", unsafe_allow_html=True)
st.markdown(f"<h2>Leap Years Passed: {leap_years}</h2>", unsafe_allow_html=True)
st.markdown(f"<h2>Hours Since Birth: {hours_since:,}</h2>", unsafe_allow_html=True)
st.markdown(f"<h2>Minutes Since Birth: {minutes_since:,}</h2>", unsafe_allow_html=True)
st.markdown(f"<h2>Seconds Since Birth: {seconds_since:,}</h2>", unsafe_allow_html=True)
