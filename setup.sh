 #!/bin/bash
  # FLL Robot Framework Setup Script
  # Run with `source setup.sh`
  # Run this once after cloning the repo

    # Set your student identifier for local git commits in THIS repo only.
    # Change this to your unique ID (no spaces).
    STUDENT_GIT_NAME="team_member_name"

  echo "🤖 Setting up FLL Robot Framework..."

  # Check if Homebrew is installed
  if ! command -v brew &> /dev/null; then
      echo "📦 Installing Homebrew..."
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

      # Add Homebrew to PATH for this session
      echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
      eval "$(/opt/homebrew/bin/brew shellenv)"
  fi

  # Check for git (from Xcode or system)
  if command -v git &> /dev/null; then
      echo "✅ Git already installed ($(git --version))"
  else
      echo "📦 Installing Git via Homebrew..."
      brew install git
  fi

  # Configure local git user.name for this repository
  if [ -d .git ]; then
      echo "🛠️  Setting local git user.name to: $STUDENT_GIT_NAME"
      git config --local user.name "$STUDENT_GIT_NAME"
      git config --local user.email "$STUDENT_GIT_NAME@example.com"
  else
      echo "⚠️  Not a git repository (no .git directory). Skipping git config."
  fi

  # Install Python 3.13
  echo "🐍 Ensuring Python 3.13 is installed..."
  brew install python@3.13

# Check if the virtual environment exists, if not, create it
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
echo "Activating the virtual environment..."
source .venv/bin/activate

# Install dependencies
# Refresh requirements.txt with `pip freeze > requirements.txt`
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found!"
fi

echo "Setup complete. Virtual environment activated."