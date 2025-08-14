import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta
import random

# Tricolor hex colors for Streamlit text
SAFFRON = "#FF9933"
WHITE = "#FFFFFF"
GREEN = "#138808"

# Extended 50+ Motivational Patriotic Messages
messages = [
    "🇮🇳 Be the change you wish to see in Bharat.",
    "🇮🇳 Our freedom was not gifted, it was earned — cherish it.",
    "🇮🇳 Serve your country in every little act you do.",
    "🇮🇳 A nation's strength lies in its unity.",
    "🇮🇳 Live for your country, and it will live forever.",
    "🇮🇳 The soil of India is rich with the sweat of its heroes.",
    "🇮🇳 Tricolor is not just a flag, it’s the soul of the nation.",
    "🇮🇳 Small deeds of love create a big impact for Bharat.",
    "🇮🇳 Let your work speak for your love for the nation.",
    "🇮🇳 Our heritage is our pride; protect it.",
    "🇮🇳 True patriotism is action, not just emotion.",
    "🇮🇳 Serve Bharat with integrity and honesty.",
    "🇮🇳 Courage built this nation; courage will sustain it.",
    "🇮🇳 Honor the past, create the future.",
    "🇮🇳 Remember the sacrifice, live the responsibility.",
    "🇮🇳 Every heart that beats for Bharat is a soldier in spirit.",
    "🇮🇳 Respect the land that gave you your identity.",
    "🇮🇳 Our freedom story is written in the ink of sacrifice.",
    "🇮🇳 Bharat Mata’s blessings are with the devoted.",
    "🇮🇳 Let unity be our power and diversity our beauty.",
    "🇮🇳 Protect nature — it’s the soul of our motherland.",
    "🇮🇳 Let’s build a future worthy of our ancestors.",
    "🇮🇳 A true patriot works even when no one is watching.",
    "🇮🇳 Speak the truth, live the truth — that’s patriotism.",
    "🇮🇳 Our flag waves high because of our unity.",
    "🇮🇳 Every sunrise in Bharat is a call to do better.",
    "🇮🇳 Service to the nation is service to God.",
    "🇮🇳 A country’s greatness begins with its people.",
    "🇮🇳 Your character is your gift to the nation.",
    "🇮🇳 Every citizen is a guardian of the nation’s soul.",
    "🇮🇳 Stand tall, for you belong to a land of legends.",
    "🇮🇳 Education is the weapon to defend our freedom.",
    "🇮🇳 Our roots are deep — let our branches be strong.",
    "🇮🇳 Peace is the truest form of patriotism.",
    "🇮🇳 Nation first, always.",
    "🇮🇳 Heroes are not born, they are made by their country.",
    "🇮🇳 Freedom is precious — guard it.",
    "🇮🇳 Every good deed strengthens the nation.",
    "🇮🇳 Together, we rise.",
    "🇮🇳 The future belongs to those who serve it.",
    "🇮🇳 Patriotism is love in action.",
    "🇮🇳 A strong Bharat starts with strong citizens.",
    "🇮🇳 Pride in our land, honor in our hearts.",
    "🇮🇳 The flag is the heart of the nation.",
    "🇮🇳 Sacrifice today for a better tomorrow.",
    "🇮🇳 You are the future of Bharat — build it well.",
    "🇮🇳 Be fearless, be selfless, be patriotic.",
    "🇮🇳 Every step for the nation counts.",
    "🇮🇳 Our diversity is our strength.",
]

def leap_years_count(start_year, end_year):
    return sum(1 for y in range(start_year, end_year + 1)
               if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0))

# Title
st.set_page_config(page_title="Independent Bharat Life Timer 🎉", layout="centered")
st.markdown(f"<h1 style='text-align:center; color:{SAFFRON};'>🇮🇳 Independent Bharat Life Timer 🎉</h1>", unsafe_allow_html=True)

# Date Picker
birth_date_input = st.date_input(
    "Select your Birth Date:",
    min_value=datetime(1900, 1, 1),
    max_value=datetime.now(),
    value=datetime(2000, 1, 1)
)

# Convert to datetime for calculations
birth_date = datetime(birth_date_input.year, birth_date_input.month, birth_date_input.day)
now = datetime.now()
independence_day = datetime(1947, 8, 15)

# Independence years calculation
independence_years = now.year - 1947
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

# Relativedelta
if days_after_independence >= 0:
    before_birth_diff = relativedelta(birth_date, independence_day)
else:
    before_birth_diff = relativedelta(independence_day, birth_date)

independent_life_diff = relativedelta(now, max(birth_date, independence_day))

# HEADER
st.markdown(f"<h2 style='color:{SAFFRON};'>Happy Independence Day 🎉 Celebrating {independence_years}th Independence of Motherland INDIA 🇮🇳</h2>", unsafe_allow_html=True)

# SECTION 4
st.markdown(f"<h3 style='color:{SAFFRON};'>MESSAGE FROM THE MOTHERLAND</h3>", unsafe_allow_html=True)
st.markdown(f"<p style='color:{SAFFRON}; font-size:18px;'>{random.choice(messages)}</p>", unsafe_allow_html=True)

# SECTION 2
st.markdown(f"<h3 style='color:{SAFFRON};'>DAYS PASSED BEFORE YOUR BIRTH</h3>", unsafe_allow_html=True)
if days_after_independence >= 0:
    st.markdown(f"<p style='color:{SAFFRON};'>India was independent for {before_birth_diff.years} years, {before_birth_diff.months} months, and {before_birth_diff.days} days before you were born.</p>", unsafe_allow_html=True)
else:
    st.markdown(f"<p style='color:{SAFFRON};'>You were born {-days_after_independence} days before India’s Independence ({before_birth_diff.years} years, {before_birth_diff.months} months, {before_birth_diff.days} days).</p>", unsafe_allow_html=True)

# SECTION 3
st.markdown(f"<h3 style='color:{WHITE};'>DAYS YOU HAVE LIVED IN INDEPENDENT BHARAT</h3>", unsafe_allow_html=True)
st.markdown(f"<p style='color:{WHITE};'>You have spent {independent_days_lived} days ({independent_life_diff.years} years, {independent_life_diff.months} months, {independent_life_diff.days} days) in Independent Bharat 🇮🇳</p>", unsafe_allow_html=True)

# SECTION 1
st.markdown(f"<h3 style='color:{GREEN};'>YOUR BIRTH INFORMATION</h3>", unsafe_allow_html=True)
st.markdown(f"<p style='color:{GREEN};'>Years Completed: {years_completed} years<br>Decades: {decades} decades and {extra_years_in_decade} years<br>Months Completed: {months_completed}<br>Days Since Birth: {days_since_birth}<br>Leap Years Passed: {leap_years}<br>Hours Since Birth: {hours_since:,}<br>Minutes Since Birth: {minutes_since:,}<br>Seconds Since Birth: {seconds_since:,}</p>", unsafe_allow_html=True)
