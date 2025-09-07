# FLL Robot Framework

## Quick Setup (macOS, run once)

  1. Clone this repository
  2. Open Terminal and navigate to the project folder
  3. Run the setup script:
    ```bash
    chmod +x setup.sh
    ./setup.sh
    ```
  4. Open VS Code: `code .`

## Daily Usage

  1. Activate your environment:
    ```bash
    source .venv/bin/activate
    ```
  2. Start coding your missions!

  Troubleshooting

  - If you see "Permission denied": Run chmod +x setup.sh first
  - If Homebrew install fails: Follow prompts and run setup again
  - If VS Code doesn't find Python: Restart VS Code after setup

  ## How Students Use This

  **First time setup:**
  ```bash
  git clone your-repo-url
  cd your-repo-name
  chmod +x setup.sh    # Makes script executable
  ./setup.sh           # Runs the setup
  ```

  Daily workflow:
  ```bash
  source .venv/bin/activate   # Activate Python environment
  code .                      # Open VS Code
  # Code your missions...
  ```


