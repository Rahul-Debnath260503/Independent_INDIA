import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta
import random

# Flag URL (PNG for better rendering)
FLAG_URL = "https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/1920px-Flag_of_India.svg.png"

# Tricolor colors
SAFFRON = "#FF9933"
WHITE = "#FFFFFF"
GREEN = "#138808"

# Patriotic messages
messages = [
    "🇮🇳 Our tricolor waves not just in the sky, but in the heart of every proud Indian.",
    "🇮🇳 India’s freedom is our inheritance; let’s enrich it with unity and action.",
    "🇮🇳 A billion dreams, one heartbeat — that’s the power of Bharat.",
    "🇮🇳 Every sunrise in India is a call to rise for our motherland.",
    "🇮🇳 The courage of our martyrs flows in our veins — live worthy of it.",
    "🇮🇳 In serving India, you serve generations yet to be born.",
    "🇮🇳 Let our love for Bharat be louder than our words.",
    "🇮🇳 India’s glory is built on the unity of its people — be that strength.",
    "🇮🇳 Freedom is a duty, not just a right — protect it every day.",
    "🇮🇳 Bharat Mata calls not for sacrifice alone, but for our excellence.",
    "🇮🇳 Our ancestors gave blood for this soil — give your best for it.",
    "🇮🇳 The tricolor is not cloth; it’s the soul of our nation.",
    "🇮🇳 In every grain of this land lies a story of courage.",
    "🇮🇳 Serve Bharat, and Bharat will serve you for eternity.",
    "🇮🇳 Unity is our strength, diversity is our pride.",
    "🇮🇳 India lives in the smile of its people — keep it alive.",
    "🇮🇳 Let your work be a tribute to those who fought for freedom.",
    "🇮🇳 The soil beneath your feet is more valuable than gold.",
    "🇮🇳 Patriotism is not a feeling for one day, it’s a way of life.",
    "🇮🇳 Our flag flies high because of the wind of sacrifice.",
    "🇮🇳 The heartbeat of Bharat echoes in every Indian soul.",
    "🇮🇳 Let no hand harm the land that gave you your name.",
    "🇮🇳 Be the citizen that Bharat Mata is proud of.",
    "🇮🇳 History gave us freedom; we must give the future hope.",
    "🇮🇳 Every Indian carries the responsibility of 1.4 billion dreams.",
    "🇮🇳 Our heritage is our crown, wear it with pride.",
    "🇮🇳 The more we unite, the stronger Bharat becomes.",
    "🇮🇳 From the Himalayas to Kanyakumari — one heart, one nation.",
    "🇮🇳 India’s greatness lies in her people, not just her borders.",
    "🇮🇳 You are the future that our freedom fighters dreamed of.",
    "🇮🇳 Our past is our inspiration; our future is our responsibility.",
    "🇮🇳 Every Indian’s duty is to make Bharat shine brighter.",
    "🇮🇳 Freedom is the result of sacrifice; never take it for granted.",
    "🇮🇳 Work not for personal glory, but for the glory of the nation.",
    "🇮🇳 Our culture is our strength — protect it.",
    "🇮🇳 A strong Bharat begins with a strong citizen.",
    "🇮🇳 Let your life be a song of devotion to Bharat Mata.",
    "🇮🇳 Every field, every street is blessed with sacrifice.",
    "🇮🇳 Our duty to India is bigger than our duty to ourselves.",
    "🇮🇳 Do not ask what India can give you — ask what you can give India.",
    "🇮🇳 The tricolor demands respect, not just celebration.",
    "🇮🇳 India’s progress is your progress — walk together.",
    "🇮🇳 Let your dreams lift the nation higher.",
    "🇮🇳 The love of the land is the purest love.",
    "🇮🇳 In every Indian’s chest beats a soldier’s heart.",
    "🇮🇳 A nation is built by those who care beyond themselves.",
    "🇮🇳 Every citizen is a pillar of Bharat’s strength.",
    "🇮🇳 To serve Bharat is the greatest honor.",
    "🇮🇳 Respect the freedom you have — many died without seeing it.",
    "🇮🇳 Bharat Mata is proud when her children are united.",
    "🇮🇳 Our duty is to turn freedom into prosperity for all.",
    "🇮🇳 The land that raised you deserves your best work.",
    "🇮🇳 True patriotism is in everyday honesty and hard work.",
    "🇮🇳 Let every action you take strengthen Bharat.",
    "🇮🇳 When Bharat shines, every Indian shines with her."
]


def leap_years_count(start_year, end_year):
    return sum(1 for y in range(start_year, end_year + 1)
               if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0))

# Page config
st.set_page_config(page_title="Independent Bharat Life Timer 🎉", layout="centered")

# Big flag at the top
st.image(FLAG_URL, width=300)

# Title
st.markdown(f"<h1 style='text-align:center; color:{SAFFRON};'>Independent Bharat Life Timer 🎉</h1>", unsafe_allow_html=True)

# Date input
birth_date_input = st.date_input(
    "Select your Birth Date:",
    min_value=datetime(1900, 1, 1),
    max_value=datetime.now(),
    value=datetime(2000, 1, 1)
)

birth_date = datetime(birth_date_input.year, birth_date_input.month, birth_date_input.day)
now = datetime.now()
independence_day = datetime(1947, 8, 15)

# Independence years
independence_years = now.year - 1947 + 2  # +1 because 1947 is counted as Year 1
if (now.month, now.day) < (8, 15):
    independence_years -= 1


# Life stats
years_completed = now.year - birth_date.year
if (now.month, now.day) < (birth_date.month, birth_date.day):
    years_completed -= 1

months_completed = years_completed * 12 + (now.month - birth_date.month)
if now.day < birth_date.day:
    months_completed -= 1

days_since_birth = (now - birth_date).days
decades = years_completed // 10
extra_years_in_decade = years_completed % 10
leap_years = leap_years_count(birth_date.year, now.year)
seconds_since = int((now - birth_date).total_seconds())
minutes_since = seconds_since // 60
hours_since = minutes_since // 60

# Independence relation
days_after_independence = (birth_date - independence_day).days
independent_days_lived = max(0, (now - max(birth_date, independence_day)).days)

if days_after_independence >= 0:
    before_birth_diff = relativedelta(birth_date, independence_day)
else:
    before_birth_diff = relativedelta(independence_day, birth_date)

independent_life_diff = relativedelta(now, max(birth_date, independence_day))

# HEADER
st.markdown(f"<p style='color:{SAFFRON}; font-size:20px; text-align:center;'>Happy Independence Day 🎉</p>", unsafe_allow_html=True)
st.markdown(f"<p style='color:{SAFFRON}; font-size:28px; font-weight:bold; text-align:center;'>Celebrating {independence_years}th Independence of Motherland INDIA 🇮🇳</p>", unsafe_allow_html=True)

# SECTION 4
st.markdown(f"<p style='color:{SAFFRON}; font-size:18px;'>MESSAGE FROM THE MOTHERLAND</p>", unsafe_allow_html=True)
st.markdown(f"<p style='color:{SAFFRON}; font-size:26px; font-weight:bold;'>{random.choice(messages)}</p>", unsafe_allow_html=True)

# SECTION 2
st.markdown(f"<p style='color:{SAFFRON}; font-size:18px;'>DAYS PASSED BEFORE YOUR BIRTH</p>", unsafe_allow_html=True)
if days_after_independence >= 0:
    st.markdown(f"<p style='color:{SAFFRON}; font-size:26px; font-weight:bold;'>India was independent for {before_birth_diff.years} years, {before_birth_diff.months} months, and {before_birth_diff.days} days before you were born.</p>", unsafe_allow_html=True)
else:
    st.markdown(f"<p style='color:{SAFFRON}; font-size:26px; font-weight:bold;'>You were born {-days_after_independence} days before India’s Independence ({before_birth_diff.years} years, {before_birth_diff.months} months, {before_birth_diff.days} days).</p>", unsafe_allow_html=True)

# SECTION 3
st.markdown(f"<p style='color:{WHITE}; font-size:18px;'>DAYS YOU HAVE LIVED IN INDEPENDENT BHARAT</p>", unsafe_allow_html=True)
st.markdown(f"<p style='color:{WHITE}; font-size:26px; font-weight:bold;'>You have spent {independent_days_lived} days ({independent_life_diff.years} years, {independent_life_diff.months} months, {independent_life_diff.days} days) in Independent Bharat 🇮🇳</p>", unsafe_allow_html=True)

# SECTION 1
st.markdown(f"<p style='color:{GREEN}; font-size:18px;'>YOUR BIRTH INFORMATION</p>", unsafe_allow_html=True)
st.markdown(f"<p style='color:{GREEN}; font-size:26px; font-weight:bold;'>Years Completed: {years_completed} years<br>Decades: {decades} decades and {extra_years_in_decade} years<br>Months Completed: {months_completed}<br>Days Since Birth: {days_since_birth}<br>Leap Years Passed: {leap_years}<br>Hours Since Birth: {hours_since:,}<br>Minutes Since Birth: {minutes_since:,}<br>Seconds Since Birth: {seconds_since:,}</p>", unsafe_allow_html=True)
