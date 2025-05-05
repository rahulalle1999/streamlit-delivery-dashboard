# 🚚 EZ Street Deliveries – Streamlit Dashboard
🔗 **Live App:** [Click here to view](https://app-delivery-dashboard-map2mj8vkbc5uhzixum5nj.streamlit.app/)

A simple, elegant web-based delivery dashboard built using **Streamlit**, **Pandas**, and **Plotly**. It lets you visualize your delivery company’s performance with real-time insights based on uploaded CSV files.

---

## 📊 Features

- Upload your own delivery CSV
- View:
  - Total Orders
  - Average Delivery Time
  - Cancelled Orders
- Visuals:
  - Bar chart showing deliveries per driver
  - Pie chart for delivery status (Delivered / Cancelled)
- Fully interactive – just drag & drop your file

---

## 🧰 Built With

- `streamlit` – interactive UI
- `pandas` – data handling
- `plotly` – beautiful graphs

---

## 🖥 How to Run

1. Clone this repo or download the files
2. Make sure you have Python installed
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
streamlit run delivery_dashboard.py
```

5. Open your browser and go to:
```
http://localhost:8501/
```

Upload any CSV file that matches this format:

| OrderID | Date | Pickup | Drop | Driver | Status | Time_taken_min | Cost |
|---------|------|--------|------|--------|--------|----------------|------|

---

## 📁 Files in This Repo

| File | Description |
|------|-------------|
| `delivery_dashboard.py` | Main Streamlit dashboard code |
| `sample_delivery_data.csv` | Example file to test the app |
| `requirements.txt` | Python libraries required |

---

## 👤 About Me

Hi, I’m **Rahul Alle**, a data engineer in the making. This project showcases how I can use Python and Streamlit to create dashboards from real data. 

📫 [Connect on LinkedIn](https://www.linkedin.com/in/rahul-alle)

---

## 🚀 Live Demo (Optional)
Want to run this online? [See Deployment Guide](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app)

Or DM me for a hosted version!
