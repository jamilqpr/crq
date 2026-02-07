# Deployment Guide: Cyber Risk Quantification App

## ✅ Successfully Pushed to GitHub!

Your CRQ app is now available at: **https://github.com/jamilqpr/crq**

---

## 🚀 Deploy to Streamlit Cloud (FREE)

### Step 1: Go to Streamlit Cloud
Visit: **https://share.streamlit.io/**

### Step 2: Sign In
- Click "Sign in" with your GitHub account
- Authorize Streamlit to access your repositories

### Step 3: Deploy New App
1. Click **"New app"**
2. Select your repository: `jamilqpr/crq`
3. Select branch: `main`
4. Main file path: `crq_app.py`
5. Click **"Deploy!"**

### Step 4: Wait for Deployment
- Streamlit will install dependencies from `requirements.txt`
- Deployment takes 2-5 minutes
- Your app will be live at: `https://[your-app-name].streamlit.app`

---

## 🌐 Alternative Deployment Options

### Option 1: Heroku
```bash
# Install Heroku CLI
# Create Procfile
echo "web: streamlit run crq_app.py --server.port=$PORT" > Procfile

# Deploy
heroku create your-crq-app
git push heroku main
```

### Option 2: Docker (Any Cloud Provider)
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements_crq.txt .
RUN pip install --no-cache-dir -r requirements_crq.txt

COPY crq_app.py .
COPY .streamlit .streamlit

EXPOSE 8501

CMD ["streamlit", "run", "crq_app.py", "--server.address", "0.0.0.0"]
```

Build and run:
```bash
docker build -t crq-app .
docker run -p 8501:8501 crq-app
```

### Option 3: AWS EC2
```bash
# SSH into EC2 instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Install dependencies
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements_crq.txt

# Run app
streamlit run crq_app.py --server.port 80
```

### Option 4: Azure Web Apps
```bash
# Install Azure CLI
az webapp up --name crq-app --resource-group your-rg --runtime "PYTHON:3.11"
```

---

## 📋 Files Pushed to GitHub

✅ `crq_app.py` - Main application (600+ lines)  
✅ `requirements.txt` - Python dependencies  
✅ `README_CRQ.md` - Complete documentation  
✅ `.gitignore` - Git ignore rules  
✅ `.streamlit/config.toml` - Streamlit configuration  

---

## 🔧 Configure Streamlit Cloud Secrets (Optional)

If you want to add authentication or API keys:

1. Go to your app settings on Streamlit Cloud
2. Click "Secrets"
3. Add TOML format secrets:

```toml
# .streamlit/secrets.toml
[passwords]
admin = "your_secure_password"

[api]
key = "your_api_key"
```

---

## 🎯 Quick Start for Team Members

Share this with your security analysts:

```bash
# Clone the repository
git clone https://github.com/jamilqpr/crq.git
cd crq

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run crq_app.py
```

---

## 📱 Share Your Deployed App

Once deployed on Streamlit Cloud, you'll get a URL like:
- `https://crq-jamilqpr.streamlit.app`

Share this URL with:
- ✅ Security team members
- ✅ Clients for risk assessments
- ✅ Management for demos
- ✅ Compliance auditors

---

## 🔒 Security Considerations

For production deployment:

1. **Authentication**: Add Streamlit auth or integrate with SSO
2. **HTTPS**: Ensure SSL/TLS is enabled (Streamlit Cloud does this automatically)
3. **Rate Limiting**: Configure to prevent abuse
4. **Data Privacy**: Don't log sensitive risk data
5. **Access Control**: Use GitHub Teams to control who can deploy

---

## 📊 Monitor Your App

Streamlit Cloud provides:
- ✅ Real-time logs
- ✅ Usage analytics
- ✅ Performance metrics
- ✅ Error tracking

---

## 🆘 Troubleshooting

**App won't deploy?**
- Check `requirements.txt` format
- Verify Python version compatibility
- Check Streamlit Cloud logs

**Slow performance?**
- Reduce number of simulations for public demo
- Add caching with `@st.cache_data`
- Optimize Monte Carlo code

**Need help?**
- Streamlit Community Forum: https://discuss.streamlit.io/
- GitHub Issues: https://github.com/jamilqpr/crq/issues

---

## ✨ Next Steps

1. **Deploy to Streamlit Cloud** (5 minutes - FREE)
2. **Customize branding** (add your company logo)
3. **Add authentication** (if needed for production)
4. **Share with team** (send them the URL)
5. **Gather feedback** (improve based on user input)

---

**Your CRQ app is ready for the cloud! 🚀**
