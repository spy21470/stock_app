import streamlit as st
import yfinance as yf

st.set_page_config(page_title="ตลาดหุ้น • Market Overview", page_icon="💹", layout="wide")

# --- Header ---
st.title("💹 ตลาดหุ้น | Market Overview")
st.caption("Dark • Luxury • Thai + English • Real data via Yahoo Finance")

st.subheader("ภาพรวมดัชนีหลัก (Major Indices)")

# ดัชนีที่จะแสดง
indices = {
    "S&P 500 (^GSPC)": "^GSPC",
    "NASDAQ (^IXIC)": "^IXIC",
    "Dow Jones (^DJI)": "^DJI",
    "SET Thailand (^SET)": "^SET"
}

cols = st.columns(len(indices))

def fetch_quote(ticker: str):
    """
    คืนค่า (last_close, prev_close) จาก Yahoo Finance
    ใช้ history(2d) เพื่อกัน fast_info ว่างในบางสภาพแวดล้อม
    """
    try:
        t = yf.Ticker(ticker)
        hist = t.history(period="2d")  # เอา 2 วันเพื่อหา prev close ได้ชัวร์
        if hist.empty:
            return None, None
        last_close = float(hist["Close"].iloc[-1])
        prev_close = float(hist["Close"].iloc[-2]) if len(hist) >= 2 else None
        return last_close, prev_close
    except Exception:
        return None, None

for (label, ticker), c in zip(indices.items(), cols):
    with c:
        last, prev = fetch_quote(ticker)
        if last is not None and prev is not None and prev != 0:
            delta = last - prev
            pct = (delta / prev) * 100
            st.metric(label=label, value=f"{last:,.2f}", delta=f"{delta:+.2f} ({pct:+.2f}%)")
        elif last is not None:
            st.metric(label=label, value=f"{last:,.2f}", delta="—")
        else:
            st.metric(label=label, value="—", delta="—")

st.markdown("---")
st.subheader("เกี่ยวกับเว็บ • About")
st.write(
    "- เว็บไซต์สรุปภาพรวมตลาดหุ้น, ดูราคาหุ้นรายตัว และเนื้อหาความรู้พื้นฐานการลงทุน\n"
    "- **Bilingual**: ไทย + English • **Theme**: Dark & Luxury • **Data**: Yahoo Finance (`yfinance`)\n"
    "- ใช้ Sidebar ทางซ้ายเพื่อสลับหน้า: **Home / Education / Stock Data**"
)
