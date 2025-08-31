Paste this short content and save:

# Apply Hygiene (once)

1) Append these ignore rules to the end of .gitignore (UTF-8 now):

--- project hygiene ---

data/outputs/**
artifacts/**
reports/**
**/*.cache


2) Create/overwrite file:


artifacts.gitignore

with:


!.gitignore


3) Stage only the hygiene files and commit:


git add .gitignore artifacts.gitignore
git commit -m "hygiene: convert .gitignore to UTF-8, add safe ignores, keep artifacts/"
git push


4) Stop and wait.

D) What to do in Codex right now

You’re seeing Codex wanting to run xxd … | sed. That’s because it thought the file was UTF-16. We’ve fixed the file manually, so:

In Codex, choose No (deny) for that xxd … | sed command.

Then send this short message:

Read briefings\hygiene_apply.md and execute it exactly:
- append the ignores to .gitignore
- create artifacts\.gitignore as shown
- show /diff and wait for approval
- then run the git add/commit/push exactly as written


Approve the /diff Codex shows, then approve the git add/commit/push.

After that, git status will be quiet and we’re done with hygiene.

Quick reassurance

The “dirty repo” wasn’t a cloning issue — it’s just unignored generated files.

Converting .gitignore to UTF-8 is one-time; future sessions won’t hit that warning.

Using briefings\*.md to feed Codex instructions avoids all the paste headaches going forward.