# 🐳 Docker Setup Guide for Student ID Validation App

## Prerequisites
✅ Docker Desktop installed and running on your system

---

## 📁 Project Structure
```
cc/
├── docker-compose.yml          # Docker Compose configuration
├── student-id-validation/
│   ├── Dockerfile              # Docker build instructions
│   ├── .dockerignore          # Files to exclude from Docker build
│   ├── app.py                 # Flask application
│   ├── index.html             # Frontend interface
│   └── requirements.txt       # Python dependencies
└── DOCKER_SETUP_GUIDE.md      # This file
```

---

## 🚀 Step-by-Step Guide to Run with Docker Desktop

### Method 1: Using Docker Compose (Recommended - Easiest!)

#### Step 1: Open Docker Desktop
- Launch Docker Desktop on your computer
- Wait for it to fully start (the whale icon should be steady, not animated)

#### Step 2: Open Terminal/Command Prompt
- **Windows**: Press `Win + R`, type `cmd`, and press Enter
- **Mac**: Press `Cmd + Space`, type `terminal`, and press Enter
- **Linux**: Press `Ctrl + Alt + T`

#### Step 3: Navigate to the Project Directory
```bash
cd /workspace/cc
```

Or navigate to wherever your `cc` folder is located:
```bash
# Windows example:
cd C:\Users\YourName\Projects\workspace\cc

# Mac/Linux example:
cd ~/Projects/workspace/cc
```

#### Step 4: Build and Start the Container
```bash
docker-compose up --build
```

**What this does:**
- 📦 Builds the Docker image with all dependencies
- 🚀 Starts the container
- 📊 Shows logs in real-time

#### Step 5: Access Your Application
- Open your web browser
- Go to: **http://localhost:5000**
- You should see the Student ID Validation interface!

#### Step 6: Test the Application
1. Enter a student ID in the input field
2. Click "Check" to validate
3. Click the "Get Recommendations" button to test the new recommendations feature

#### Step 7: Stop the Application
- Press `Ctrl + C` in the terminal
- Or run: `docker-compose down`

---

### Method 2: Using Docker Desktop GUI

#### Step 1: Open Docker Desktop

#### Step 2: Click on "Images" in the left sidebar

#### Step 3: Build the Image via Terminal First
```bash
cd /workspace/cc/student-id-validation
docker build -t student-validation-app .
```

#### Step 4: In Docker Desktop
1. Go to "Images" tab
2. Find `student-validation-app`
3. Click the ▶️ "Run" button
4. Click "Optional Settings"
5. Set:
   - **Container name**: `student-app`
   - **Ports**: Host Port `5000` → Container Port `5000`
6. Click "Run"

#### Step 5: Access the Application
- Go to **http://localhost:5000** in your browser

#### Step 6: Stop the Container
1. Go to "Containers" tab in Docker Desktop
2. Find your container
3. Click the ⏹️ Stop button

---

### Method 3: Pure Docker Commands (Advanced)

#### Build the Image
```bash
cd /workspace/cc/student-id-validation
docker build -t student-validation-app .
```

#### Run the Container
```bash
docker run -d -p 5000:5000 --name student-app student-validation-app
```

#### View Logs
```bash
docker logs student-app
```

#### Stop the Container
```bash
docker stop student-app
```

#### Remove the Container
```bash
docker rm student-app
```

---

## 🧪 Testing the API Endpoints

### 1. Test Student Validation
```bash
curl -X POST http://localhost:5000/validate \
  -H "Content-Type: application/json" \
  -d '{"student_id": "12345"}'
```

### 2. Test Recommendations Endpoint
```bash
curl -X POST http://localhost:5000/recommendations \
  -H "Content-Type: application/json" \
  -d '{"student_id": "12345"}'
```

---

## 🔧 Useful Docker Commands

### View Running Containers
```bash
docker ps
```

### View All Containers (including stopped)
```bash
docker ps -a
```

### View Container Logs
```bash
docker logs student-validation-app
```

### Access Container Shell (for debugging)
```bash
docker exec -it student-validation-app /bin/bash
```

### Rebuild After Code Changes
```bash
docker-compose up --build
```

### Remove All Stopped Containers
```bash
docker container prune
```

### Remove Unused Images
```bash
docker image prune
```

---

## 🐛 Troubleshooting

### Issue: "Port 5000 is already in use"
**Solution:**
```bash
# Stop the conflicting container
docker-compose down

# Or use a different port by editing docker-compose.yml
# Change "5000:5000" to "5001:5000"
```

### Issue: "Cannot connect to database"
**Solution:**
- Ensure your Azure SQL database is accessible
- Check firewall settings to allow your IP
- Verify credentials in `app.py`

### Issue: Changes not reflecting
**Solution:**
```bash
# Rebuild the container
docker-compose up --build --force-recreate
```

### Issue: Container keeps restarting
**Solution:**
```bash
# Check logs
docker logs student-validation-app

# Common causes:
# - Database connection issues
# - Missing dependencies
# - Syntax errors in Python code
```

---

## 📊 Monitoring in Docker Desktop

1. Open Docker Desktop
2. Click "Containers" in the left sidebar
3. Click on your running container
4. You can see:
   - 📈 CPU and Memory usage
   - 📝 Real-time logs
   - 🔍 Inspect container details
   - 🖥️ Access terminal inside container

---

## 🎯 Quick Reference

| Action | Command |
|--------|---------|
| Start app | `docker-compose up` |
| Start in background | `docker-compose up -d` |
| Stop app | `docker-compose down` |
| View logs | `docker-compose logs -f` |
| Rebuild | `docker-compose up --build` |
| Access shell | `docker exec -it student-validation-app /bin/bash` |

---

## 🌟 Best Practices

1. **Always check Docker Desktop is running** before executing commands
2. **Use `docker-compose`** for easier management
3. **Check logs** if something doesn't work: `docker-compose logs`
4. **Rebuild after changes** to `requirements.txt` or `Dockerfile`
5. **Use `.dockerignore`** to keep images small and secure

---

## 📞 Need Help?

If you encounter issues:
1. Check the logs: `docker-compose logs`
2. Ensure Docker Desktop is running
3. Verify port 5000 is not in use
4. Try rebuilding: `docker-compose up --build`

---

**Happy Dockerizing! 🐳✨**
