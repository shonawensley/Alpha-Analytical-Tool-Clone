# AAT9 ▸ Git Commit Instructions for v0.3-checkpoint

Use these commands to commit the V-TRAC enhancement and documentation updates. This creates a dedicated feature branch, commits the relevant files, and tags the release.

```bash
# 1. Create a new feature branch
git checkout -b feat/vtrac-logging

# 2. Add the modified and new files to staging
git add scripts/streamlit_app_with_analyzer.py \
        utils/bundler.py \
        docs/modules/AAT9_Module_VTRAC_Enhancement.md \
        docs/AAT9_CHANGELOG.md \
        docs/AAT9_Minor_Fixes_Checkpoint_v0.3.md \
        docs/guides/AAT9_Git_Commit_v0.3.md

# 3. Commit the changes with a descriptive message
git commit -m "feat: V-TRAC 3-prediction logging + bundle JSON + docs"

# 4. Tag the commit as a checkpoint
git tag v0.3-checkpoint

# 5. Push the branch and tags to the remote repository
git push --set-upstream origin feat/vtrac-logging --tags
```

**Note:** The file `tools/long_string_reducer_part3.py` should be left unstaged as it is parked for a future release.
