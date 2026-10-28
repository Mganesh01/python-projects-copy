
import streamlit as st


# Create a Node for each website
class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


# Browser history using Doubly Linked List
class BrowserHistory:
    def __init__(self, homepage):
        self.head = Node(homepage)
        self.current = self.head

    def visit(self, url):
        new_node = Node(url)

        # Remove forward history after a new visit
        self.current.next = None

        # Connect current page to the new page
        new_node.prev = self.current
        self.current.next = new_node

        # Move to the new page
        self.current = new_node

    def back(self):
        if self.current.prev:
            self.current = self.current.prev

    def forward(self):
        if self.current.next:
            self.current = self.current.next

    def get_history(self):
        # Traverse from the first page
        pages = []
        node = self.head

        while node:
            pages.append(node.url)
            node = node.next

        return pages


# Streamlit UI
st.set_page_config(
    page_title="Browser History",
    page_icon="🌐"
)

st.title("🌐 Browser History")
st.caption("Python + Doubly Linked List")

# Initialize browser history once per session
if "browser" not in st.session_state:
    st.session_state.browser = BrowserHistory(
        "https://google.com"
    )

browser = st.session_state.browser

# Display current website
st.subheader("Current Website")
st.info(browser.current.url)

# Visit a new website
url = st.text_input(
    "Enter website URL",
    placeholder="https://youtube.com"
)

if st.button("🌐 Visit"):
    if url.strip():
        website = url.strip()

        if not website.startswith(("http://", "https://")):
            website = "https://" + website

        browser.visit(website)
        st.rerun()

# Back and Forward buttons
col1, col2 = st.columns(2)

with col1:
    if st.button(
        "⬅️ Back",
        disabled=browser.current.prev is None,
        use_container_width=True
    ):
        browser.back()
        st.rerun()

with col2:
    if st.button(
        "Forward ➡️",
        disabled=browser.current.next is None,
        use_container_width=True
    ):
        browser.forward()
        st.rerun()

# Display navigation history
st.subheader("📜 Browser History")

for page in browser.get_history():
    if page == browser.current.url:
        st.markdown(f"👉 **{page} — Current Page**")
    else:
        st.write(f"🔗 {page}")
