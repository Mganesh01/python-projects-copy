import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get OMDb API Key
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

if not OMDB_API_KEY:
    st.error("❌ OMDB_API_KEY not found in .env file")
    st.stop()

OMDB_BASE_URL = "http://www.omdbapi.com/"

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="LearnBuildShare OTT",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CUSTOM CSS & STYLING
# =========================================================

st.markdown(
    """
    <style>
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f0f1e 0%, #1a1a2e 50%, #16213e 100%);
        color: white;
    }
    
    .header-container {
        background: linear-gradient(90deg, #e50914 0%, #831010 100%);
        padding: 30px 20px;
        border-radius: 10px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(229, 9, 20, 0.3);
    }
    
    .header-title {
        font-size: 48px;
        font-weight: 900;
        margin-bottom: 8px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    .header-subtitle {
        font-size: 16px;
        color: rgba(255, 255, 255, 0.8);
        letter-spacing: 2px;
    }
    
    .search-container {
        background: rgba(255, 255, 255, 0.08);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid rgba(229, 9, 20, 0.3);
        margin-bottom: 30px;
        backdrop-filter: blur(10px);
    }
    
    .movie-poster {
        border-radius: 15px;
        box-shadow: 0 20px 60px rgba(229, 9, 20, 0.4);
        overflow: hidden;
    }
    
    .movie-card {
        background: linear-gradient(145deg, #1a1a2e, #16213e);
        padding: 30px;
        border-radius: 15px;
        border: 1px solid rgba(229, 9, 20, 0.3);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
        margin-top: 20px;
    }
    
    .movie-title {
        font-size: 42px;
        font-weight: 900;
        margin-bottom: 12px;
        color: #e50914;
    }
    
    .movie-meta {
        display: flex;
        gap: 15px;
        margin-bottom: 20px;
        flex-wrap: wrap;
    }
    
    .meta-tag {
        background: rgba(229, 9, 20, 0.2);
        color: #fff;
        padding: 8px 14px;
        border-radius: 20px;
        font-size: 14px;
        border: 1px solid rgba(229, 9, 20, 0.5);
    }
    
    .rating-badge {
        background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
        color: #000;
        padding: 12px 20px;
        border-radius: 10px;
        font-weight: 900;
        font-size: 20px;
        display: inline-block;
    }
    
    .plot-text {
        font-size: 16px;
        line-height: 1.8;
        color: rgba(255, 255, 255, 0.9);
        margin-top: 20px;
        padding: 20px;
        background: rgba(0, 0, 0, 0.3);
        border-left: 4px solid #e50914;
        border-radius: 8px;
    }
    
    .info-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 15px;
        margin-top: 25px;
    }
    
    .info-box {
        background: rgba(229, 9, 20, 0.1);
        padding: 18px;
        border-radius: 10px;
        border: 1px solid rgba(229, 9, 20, 0.3);
        text-align: center;
    }
    
    .info-label {
        color: #aaa;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }
    
    .info-value {
        color: #fff;
        font-size: 16px;
        font-weight: 700;
    }
    
    .no-poster {
        height: 400px;
        background: linear-gradient(145deg, #1a1a2e, #16213e);
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 80px;
        border: 2px dashed rgba(229, 9, 20, 0.3);
    }
    
    .error-box {
        background: rgba(220, 38, 38, 0.1);
        border: 2px solid #dc2626;
        color: #fca5a5;
        padding: 20px;
        border-radius: 10px;
        font-size: 16px;
    }
    
    .success-box {
        background: rgba(34, 197, 94, 0.1);
        border: 2px solid #22c55e;
        color: #86efac;
        padding: 20px;
        border-radius: 10px;
    }
    
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 30px;
        color: #666;
        border-top: 1px solid rgba(229, 9, 20, 0.2);
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="header-container">
        <div class="header-title">🎬 LearnBuildShare OTT</div>
        <div class="header-subtitle">DISCOVER MOVIES • EXPLORE DETAILS • FIND YOUR NEXT FAVORITE</div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SEARCH SECTION
# =========================================================

st.markdown(
    """
    <div class="search-container">
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([4, 1])

with col1:
    movie_name = st.text_input(
        "🔍 Search for a movie...",
        placeholder="e.g. Inception, The Matrix, Interstellar",
        label_visibility="collapsed"
    )

with col2:
    search_button = st.button("🔎 SEARCH", use_container_width=True)

# =========================================================
# API FUNCTION
# =========================================================

def fetch_movie_data(title: str) -> dict:
    """Fetch movie data from OMDb API"""
    try:
        params = {
            "apikey": OMDB_API_KEY,
            "t": title,
            "type": "movie"
        }
        response = requests.get(OMDB_BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("Response") == "True":
            return data
        else:
            return {"error": data.get("Error", "Movie not found")}
    
    except requests.exceptions.Timeout:
        return {"error": "Request timed out. Please try again."}
    except requests.exceptions.ConnectionError:
        return {"error": "Connection error. Check your internet."}
    except Exception as e:
        return {"error": f"Error: {str(e)}"}

# =========================================================
# SEARCH ACTION
# =========================================================

if search_button:
    if not movie_name.strip():
        st.warning("⚠️ Please enter a movie name to search")
    else:
        with st.spinner("🤖 Searching OMDb database..."):
            movie_data = fetch_movie_data(movie_name.strip())
        
        if "error" in movie_data:
            st.markdown(
                f"""
                <div class="error-box">
                    ❌ {movie_data['error']}
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            # Display success message
            st.markdown(
                """
                <div class="success-box">
                    ✅ Movie found! Here are the details:
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Movie Display Section
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            
            col_poster, col_details = st.columns([1.2, 2.5], gap="large")
            
            # Poster Section
            with col_poster:
                if movie_data.get("Poster") and movie_data["Poster"] != "N/A":
                    st.image(movie_data["Poster"], use_container_width=True)
                else:
                    st.markdown(
                        '<div class="no-poster">🎬</div>',
                        unsafe_allow_html=True
                    )
            
            # Details Section
            with col_details:
                title = movie_data.get("Title", "N/A")
                year = movie_data.get("Year", "N/A")
                runtime = movie_data.get("Runtime", "N/A")
                genre = movie_data.get("Genre", "N/A")
                rating = movie_data.get("imdbRating", "N/A")
                director = movie_data.get("Director", "N/A")
                actors = movie_data.get("Actors", "N/A")
                plot = movie_data.get("Plot", "N/A")
                
                st.markdown(f'<div class="movie-title">{title}</div>', unsafe_allow_html=True)
                
                st.markdown(
                    f"""
                    <div class="movie-meta">
                        <span class="meta-tag">📅 {year}</span>
                        <span class="meta-tag">⏱️ {runtime}</span>
                        <span class="meta-tag">🎭 {genre}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                if rating != "N/A":
                    st.markdown(
                        f'<div style="margin: 15px 0;"><span class="rating-badge">⭐ {rating}/10</span></div>',
                        unsafe_allow_html=True
                    )
                
                st.markdown(f'<div class="plot-text">{plot}</div>', unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Movie Information Grid
            st.markdown("### 📊 Movie Information")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(
                    f"""
                    <div class="info-box">
                        <div class="info-label">Director</div>
                        <div class="info-value">{director}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                st.markdown(
                    f"""
                    <div class="info-box">
                        <div class="info-label">Released</div>
                        <div class="info-value">{movie_data.get('Released', 'N/A')}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            with col2:
                st.markdown(
                    f"""
                    <div class="info-box">
                        <div class="info-label">Cast</div>
                        <div class="info-value">{actors}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                st.markdown(
                    f"""
                    <div class="info-box">
                        <div class="info-label">IMDb ID</div>
                        <div class="info-value">{movie_data.get('imdbID', 'N/A')}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            # Additional Info
            st.markdown("### 📝 Additional Details")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Type", movie_data.get("Type", "N/A").upper())
            
            with col2:
                st.metric("Language", movie_data.get("Language", "N/A"))
            
            with col3:
                st.metric("Country", movie_data.get("Country", "N/A"))

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        <h3>🎬 LearnBuildShare OTT Movie Search</h3>
        <p style="color: #999; margin-top: 15px;">Powered by Learn Build Share</p>
    </div>
    """,
    unsafe_allow_html=True
)
