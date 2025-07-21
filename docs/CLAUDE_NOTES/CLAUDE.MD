## 🚦 Claude Code Operating Rules (v1.1)

1 Think first – draft plan in tasks/todo.md  
2 Plan review – wait for “Approved”  
3 Iterate small – one TODO at a time  
4 Security audit – run prompt before /commit  
5 Learning recap – run prompt after /commit  
6 Undoable – no big‑bang refactors without ticket  
7 Wrap‑up – append Review section to todo.md  

### 🔒 Security‑Audit Prompt  
  > “Please audit the code you just wrote against security best-practices.
  > - Remove leaked secrets
  > - Validate inputs / sanitise outputs
  > - Check for insecure file-handling or injection vectors
  > Return ‘OK’ or list any issues found.”


### 🧑‍🏫 Learning Prompt  
  > “Explain in detail what you built, why you made those design choices, and how the new code works.
  > Assume I’m a junior developer you’re mentoring.” :contentReference[oaicite:4]{index=4}
  How to use it


### 📚 Snippet Registry – when Claude should `/open` extra prompts

| Snippet file | Auto‑trigger | Manual |
|--------------|-------------|--------|
| CodeFarm_v9.md | Backlog task > 150 LOC **or** > 2 files | `/open docs/prompt_snippets/CodeFarm_v9.md` |
| Dev_Companion.md | You ask to *Review / Explain / Test* existing code | `/open docs/prompt_snippets/Dev_Companion.md` |
| Code_Translator.md | You say “translate this language A → B” | `/open docs/prompt_snippets/Code_Translator.md` |

*(Claude: remember to `/forget` a snippet when finished.)*
