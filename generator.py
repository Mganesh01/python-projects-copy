# Copyright © LearnBuildShare
# Mini Movie Ticket Booking App
# Python Generator + Streamlit

import streamlit as st
import time
import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )

st.set_page_config(
    page_title="Movie Ticket Booking",
    page_icon="🎬",
    layout="wide"
)

# ---------------------------------------------------------
# Movie Data
# ---------------------------------------------------------

MOVIE = "RRR"
THEATER = "LearnBuild Cinemas"
SHOW_TIME = "7:30 PM"

# ---------------------------------------------------------
# Generator - Creates ticket only when requested
# ---------------------------------------------------------

def ticket_generator(total_tickets):
    for ticket_id in range(1, total_tickets + 1):
        yield {
            "ticket_id": f"LB-{ticket_id:06d}",
            "movie": MOVIE,
            "theater": THEATER,
            "show_time": SHOW_TIME,
            "seat": f"{chr(65 + ((ticket_id - 1) // 20) % 26)}{((ticket_id - 1) % 20) + 1}"
        }


# ---------------------------------------------------------
# Session State
# ---------------------------------------------------------

if "generator" not in st.session_state:
    st.session_state.generator = None

if "booked_tickets" not in st.session_state:
    st.session_state.booked_tickets = []

if "total_tickets" not in st.session_state:
    st.session_state.total_tickets = 0

if "booking_started" not in st.session_state:
    st.session_state.booking_started = False


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        text-align:center;
        font-size:45px;
        font-weight:800;
        margin-bottom:5px;
    }

    .subtitle {
        text-align:center;
        color:#777;
        font-size:18px;
        margin-bottom:30px;
    }

    .movie-card {
        padding:25px;
        border-radius:20px;
        background:linear-gradient(135deg,#111,#292929);
        color:white;
        text-align:center;
        box-shadow:0 8px 30px rgba(0,0,0,.25);
    }

    .ticket {
        padding:20px;
        margin:10px 0;
        border-radius:15px;
        background:#f7f7f7;
        border-left:6px solid #111;
    }

    .ticket-id {
        font-size:20px;
        font-weight:bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">🎬 Movie Ticket Booking</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">⚡ Powered by Python Generator</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# Movie Information
# ---------------------------------------------------------

st.markdown(
    f"""
    <div class="movie-card">
        <h1>🎬 {MOVIE}</h1>
        <h3>🏢 {THEATER}</h3>
        <p>🕢 {SHOW_TIME}</p>
        <p>🎟️ Book your tickets instantly</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")


# ---------------------------------------------------------
# Booking Configuration
# ---------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    total_tickets = st.number_input(
        "🎟️ Total Tickets Available",
        min_value=10,
        max_value=1_000_000,
        value=100,
        step=10,
        key="total_tickets_input"
    )

with col2:
    tickets_to_book = st.number_input(
        "🎫 Tickets to Book",
        min_value=1,
        max_value=20,
        value=1,
        step=1,
        key="tickets_to_book"
    )

with col3:
    ticket_price = st.number_input(
        "💰 Ticket Price",
        min_value=100,
        max_value=5000,
        value=250,
        step=50,
        key="ticket_price_input"
    )

selected_tickets = int(tickets_to_book)
selected_cost = selected_tickets * int(ticket_price)

st.metric(
    "🎫 Selected ticket cost",
    f"₹{selected_cost:,}",
    f"{selected_tickets} ticket(s) × ₹{int(ticket_price):,}"
)


# ---------------------------------------------------------
# Start Booking
# ---------------------------------------------------------

if st.button(
    "🚀 START BOOKING",
    use_container_width=True
):

    st.session_state.total_tickets = total_tickets

    st.session_state.generator = ticket_generator(
        total_tickets
    )

    st.session_state.booked_tickets = []

    st.session_state.booking_started = True

    st.success(
        f"🎬 Booking system started with "
        f"{total_tickets:,} available tickets!"
    )


# ---------------------------------------------------------
# Booking
# ---------------------------------------------------------

if st.session_state.booking_started:

    st.divider()

    st.subheader("🎟️ Book Tickets")

    available = (
        st.session_state.total_tickets
        - len(st.session_state.booked_tickets)
    )

    st.write("")

    if st.button(
        f"🎫 BOOK {selected_tickets} TICKET(S)",
        use_container_width=True
    ):

        if available < selected_tickets:

            st.error(
                "❌ Not enough tickets available!"
            )

        else:

            start = time.perf_counter()

            new_tickets = []

            for _ in range(selected_tickets):

                ticket = next(
                    st.session_state.generator
                )

                ticket["price"] = int(ticket_price)

                new_tickets.append(ticket)

                st.session_state.booked_tickets.append(
                    ticket
                )

            end = time.perf_counter()

            st.success(
                f"🎉 {selected_tickets} ticket(s) booked successfully!"
            )

            st.caption(
                f"⚡ Tickets generated only when required "
                f"| Processing time: {(end - start) * 1000:.3f} ms"
            )

    available = (
        st.session_state.total_tickets
        - len(st.session_state.booked_tickets)
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎟️ Total Seats",
            f"{st.session_state.total_tickets:,}"
        )

    with col2:
        st.metric(
            "✅ Booked",
            f"{len(st.session_state.booked_tickets):,}"
        )

    with col3:
        st.metric(
            "🟢 Available",
            f"{available:,}"
        )


# ---------------------------------------------------------
# Booked Tickets
# ---------------------------------------------------------

if st.session_state.booked_tickets:

    st.divider()

    st.subheader("🎟️ Your Booked Tickets")

    for ticket in st.session_state.booked_tickets:
        ticket.setdefault("price", int(ticket_price))

    for ticket in reversed(
        st.session_state.booked_tickets
    ):

        st.markdown(
            f"""
            <div class="ticket">

                <div class="ticket-id">
                    🎫 {ticket["ticket_id"]}
                </div>

                <hr>

                🎬 <b>Movie:</b> {ticket["movie"]}<br>
                🏢 <b>Theater:</b> {ticket["theater"]}<br>
                🕢 <b>Show:</b> {ticket["show_time"]}<br>
                💺 <b>Seat:</b> {ticket["seat"]}<br>
                💰 <b>Price:</b> ₹{ticket["price"]}

            </div>
            """,
            unsafe_allow_html=True
        )

    st.success(
        f"💰 Total Amount: "
        f"₹{sum(ticket['price'] for ticket in st.session_state.booked_tickets):,}"
    )


# ---------------------------------------------------------
# Generator Explanation
# ---------------------------------------------------------

st.divider()

st.subheader("⚡ Generator in Action")

st.code(
    """
def ticket_generator(total_tickets):

    for ticket_id in range(1, total_tickets + 1):

        yield {
            "ticket_id": ticket_id,
            "movie": "RRR",
            "seat": ticket_id
        }
""",
    language="python"
)

st.info(
    "💡 Even if the cinema has 10 lakh tickets, "
    "the application generates a ticket only when "
    "the customer actually books one."
)

# Copyright © LearnBuildShare


def get_ticket():
    return "Movie Ticket"

ticket = get_ticket()

print(ticket)


def ticket_generator():
    for ticket in range(1, 6):
        yield f"Ticket-{ticket}"


tickets = ticket_generator()

print(next(tickets))
print(next(tickets))
print(next(tickets))


# Generator creates only the value we need
def ticket_generator():
    for ticket in range(1, 1_000_001):
        yield ticket
tickets = ticket_generator()
# Only one ticket is generated at a time
print(next(tickets))  # 🎟️ Ticket 1
print(next(tickets))  # 🎟️ Ticket 2
print(next(tickets))  # 🎟️ Ticket 3


# ❌ Don't do this for a huge 10GB file

with open("app.log", "r") as file:
    data = file.read()  # Entire file is loaded into memory 😅

    for line in data.splitlines():
        if "ERROR" in line:
            print(line)

with open("app.log", "r") as file:
    for line in file:
        print("Processing:", line.strip())

        

for line in file:
    if "ERROR" in line:
        print("🚨 Error found:", line.strip())

with open("app.log", "r") as file:
    iterator = iter(file)

    #Internally how for loop works
    line = next(iterator)
    print(line)

    line = next(iterator)
    print(line)

    line = next(iterator)
    print(line)


with open("app.log", "r") as file:
    for line in file:
        print("Processing:", line.strip())

        if "ERROR" in line:
            print("🚨 Error found!")



with open("app.log", "r") as file:

    iterator = iter(file)  # File object ni iterator ga use chestunnam

    print(next(iterator))  # First line
    print(next(iterator))  # Next line
    print(next(iterator))  # Next line

# 👉 Iterator = next() use chesi values ni one by one provide chese object



