#!/bin/bash
# git-rollback-operations.sh - Git-based rollback operations with repository management
# Part of rollback-manager.sh L2-MODULAR extraction
# Authority: @context/architecture/patterns/l2-modular-extraction-patterns.md

set -euo pipefail

# Git-based rollback operations
git_rollback_operation() {
    local rollback_type="$1"  # commit, branch, stash
    local target="$2"         # commit hash, branch name, stash index
    local scope="${3:-all}"   # all, context, specific_files
    
    echo -e "${BLUE}🔄 Git rollback operation: $rollback_type to $target${NC}"
    
    # Verify we're in a git repository
    if ! git -C "$PROJECT_ROOT" rev-parse --git-dir >/dev/null 2>&1; then
        echo -e "${RED}❌ Not a git repository: $PROJECT_ROOT${NC}"
        return 1
    fi
    
    # Save current state
    local current_commit=$(git -C "$PROJECT_ROOT" rev-parse HEAD)
    local current_branch=$(git -C "$PROJECT_ROOT" branch --show-current)
    
    echo "Current state: $current_branch ($current_commit)"
    
    case "$rollback_type" in
        "commit")
            echo "Rolling back to commit: $target"
            
            # Verify commit exists
            if ! git -C "$PROJECT_ROOT" cat-file -e "$target" 2>/dev/null; then
                echo -e "${RED}❌ Commit not found: $target${NC}"
                return 1
            fi
            
            if [[ "$scope" == "context" ]]; then
                # Rollback only context directory
                echo "Selective rollback: context/ directory only"
                if git -C "$PROJECT_ROOT" checkout "$target" -- context/; then
                    echo -e "${GREEN}✅ Context directory rolled back to $target${NC}"
                else
                    echo -e "${RED}❌ Context rollback failed${NC}"
                    return 1
                fi
            else
                # Full repository rollback
                echo "Full repository rollback to: $target"
                if git -C "$PROJECT_ROOT" reset --hard "$target"; then
                    echo -e "${GREEN}✅ Repository rolled back to $target${NC}"
                else
                    echo -e "${RED}❌ Repository rollback failed${NC}"
                    return 1
                fi
            fi
            ;;
            
        "branch")
            echo "Switching to branch: $target"
            
            # Check if branch exists
            if ! git -C "$PROJECT_ROOT" show-ref --verify --quiet "refs/heads/$target"; then
                echo -e "${RED}❌ Branch not found: $target${NC}"
                return 1
            fi
            
            if git -C "$PROJECT_ROOT" checkout "$target"; then
                echo -e "${GREEN}✅ Switched to branch: $target${NC}"
            else
                echo -e "${RED}❌ Branch switch failed${NC}"
                return 1
            fi
            ;;
            
        "stash")
            echo "Applying stash: $target"
            
            if git -C "$PROJECT_ROOT" stash apply "$target"; then
                echo -e "${GREEN}✅ Stash applied: $target${NC}"
            else
                echo -e "${RED}❌ Stash apply failed${NC}"
                return 1
            fi
            ;;
            
        *)
            echo -e "${RED}❌ Unknown git rollback type: $rollback_type${NC}"
            return 1
            ;;
    esac
    
    # Log git operation
    {
        echo "GIT_ROLLBACK: $(date)"
        echo "  Type: $rollback_type"
        echo "  Target: $target"
        echo "  Scope: $scope"
        echo "  Previous state: $current_branch ($current_commit)"
        echo "  Status: SUCCESS"
        echo "  ---"
    } >> "$LOG_FILE"
    
    return 0
}