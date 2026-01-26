#!/bin/bash
set -e

# Base directory for symlinks
TARGET_BASE="$HOME/.gemini/antigravity"
TARGET_GEMINI_MD="$HOME/.gemini/GEMINI.md"

# Source directories (relative to this script)
# Script is in /home/node/myagentconfig/antigravity/
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC_WORKFLOWS="$SCRIPT_DIR/workflows"
SRC_SKILLS="$SCRIPT_DIR/skills"
SRC_GEMINI_MD="$SCRIPT_DIR/GEMINI.md"

echo "Using source directory: $SCRIPT_DIR"

# Ensure target directories exist (parent for workflows/skills)
mkdir -p "$TARGET_BASE"
mkdir -p "$HOME/.gemini"

# Function to update symlink
update_symlink() {
    local src="$1"
    local target="$2"

    if [ -e "$target" ] || [ -L "$target" ]; then
        echo "Removing existing $target"
        rm -rf "$target"
    fi
    
    echo "Creating symlink: $target -> $src"
    ln -s "$src" "$target"
}

# Update symlinks
# Target: ~/.gemini/antigravity/global_workflows -> Source: workflows
update_symlink "$SRC_WORKFLOWS" "$TARGET_BASE/global_workflows"

# Target: ~/.gemini/antigravity/skills -> Source: skills
update_symlink "$SRC_SKILLS" "$TARGET_BASE/skills"

# Target: ~/.gemini/GEMINI.md -> Source: GEMINI.md
update_symlink "$SRC_GEMINI_MD" "$TARGET_GEMINI_MD"

echo "Symlinks updated successfully."
ls -l "$TARGET_BASE/global_workflows"
ls -l "$TARGET_BASE/skills"
ls -l "$TARGET_GEMINI_MD"
