# 🏞️ Place Recommender System  

A **Streamlit web app** that recommends places similar to the one you search or select. It uses precomputed similarity scores to suggest the top 5 related places.  

---

## 🚀 Features  
- 🔍 Search for a place by name  
- 📋 Select from a dropdown list of available places  
- 🤝 Get **top 5 recommended places** instantly  
- 🖥️ Simple and interactive UI built with **Streamlit**  

---

## 🛠️ Tech Stack  
- **Python**  
- **Streamlit** (for web app)  
- **Pickle** (for loading models & data)  
- **Pandas / Numpy** (for handling data, assumed in pkl files)  

---

## 📂 Project Structure  
```
.
├── Place.py              # Main Streamlit app
├── place_list.pkl        # Pickled list of places
├── similarity.pkl        # Pickled similarity matrix
└── README.md             # Project documentation
```

---

## ⚙️ Installation & Setup  

1. **Clone this repository**  
```bash
git clone https://github.com/your-username/place-recommender.git
cd place-recommender
```

2. **Create a virtual environment (optional but recommended)**  
```bash
python -m venv venv
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. **Install dependencies**  
```bash
pip install streamlit requests pickle5
```

4. **Run the app**  
```bash
streamlit run Place.py
```

---

## 🎯 How It Works  
1. User searches or selects a place.  
2. The app finds the corresponding index in the dataset.  
3. Uses similarity scores to rank other places.  
4. Displays **top 5 recommended places** in a clean UI.  
