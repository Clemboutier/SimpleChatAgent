# GitHub Setup Instructions

## Steps to connect this repository to GitHub

### 1. Create a new GitHub repository

1. Go to https://github.com/new
2. Repository name: `PocketChatbot`
3. Description: "A chatbot built with PocketFlow framework"
4. Keep it Public or Private (your choice)
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

### 2. Connect your local repository to GitHub

After creating the repository, run these commands:

```bash
cd /Users/clementboutier/Desktop/Explore/Code/PocketChatbot

# Add the remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/PocketChatbot.git

# Or if you prefer SSH:
# git remote add origin git@github.com:YOUR_USERNAME/PocketChatbot.git

# Push your code
git branch -M main
git push -u origin main
```

### 3. Verify the connection

```bash
git remote -v
```

You should see:
```
origin  https://github.com/YOUR_USERNAME/PocketChatbot.git (fetch)
origin  https://github.com/YOUR_USERNAME/PocketChatbot.git (push)
```

### Quick Command (replace YOUR_USERNAME)

```bash
git remote add origin https://github.com/YOUR_USERNAME/PocketChatbot.git && git push -u origin main
```
