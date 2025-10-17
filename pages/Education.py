import streamlit as st

st.set_page_config(page_title="ความรู้หุ้น • Investing Basics", page_icon="📚", layout="wide")

st.markdown("## 📚 ความรู้หุ้น — Investing Basics")
st.caption("Short bilingual notes • Thai + English")

st.markdown("""
### 1) คำศัพท์สำคัญ (Key Terms)
- **Price / ราคา** — ราคาซื้อขายล่าสุดของหุ้น  
- **Volume / ปริมาณ** — จำนวนหุ้นที่ถูกซื้อขายในช่วงเวลา  
- **Market Cap / มูลค่าตลาด** — ราคาหุ้น × จำนวนหุ้นทั้งหมด  
- **P/E Ratio** — ราคาเทียบกำไรต่อหุ้น (ประเมินความแพง/ถูก)  
- **Dividend / เงินปันผล** — ผลตอบแทนที่บริษัทจ่ายคืนผู้ถือหุ้น  

### 2) วิธีอ่านกราฟแท่งเทียน (How to read Candlesticks)
- **Body** — ช่วงเปิด–ปิด (Open–Close)  
- **Wick/Shadow** — หางเทียน (High/Low)  
- **Bullish (เขียว)** — ปิดสูงกว่าเปิด → แรงซื้อเด่น  
- **Bearish (แดง)** — ปิดต่ำกว่าเปิด → แรงขายเด่น  

### 3) ความเสี่ยงและพอร์ต (Risk & Portfolio)
- **Diversification** — กระจายการลงทุนเพื่อลดความเสี่ยงเฉพาะตัว  
- **Time Horizon** — ระยะเวลาการลงทุนสัมพันธ์กับความผันผวน  
- **Risk Tolerance** — ความสามารถในการรับความเสี่ยงต่างกัน  
- **Rebalancing** — ปรับสัดส่วนพอร์ตกลับสู่เป้าหมาย  
- **Cost & Tax** — ต้นทุนและภาษีมีผลต่อผลตอบแทนสุทธิ  

> ⚠️ **Disclaimer**: ข้อมูลเพื่อการศึกษา ไม่ใช่คำแนะนำการลงทุน (Educational use only)
""")
