## 🚦 Claude Code Operating Rules (v1.1)

*For system architecture, see [docs/aat9_overview.md](./docs/aat9_overview.md).*

1.  **Think first** – scan code & docs; draft a checkbox plan in `tasks/todo.md`.
2.  **Plan review** – wait for my "Approved" before coding.
3.  **Iterate small** – one TODO at a time; summarise each change.
4.  **Security check** – run the *Security-Audit Prompt* **before** `/commit`.
5.  **Learning recap** – run the *Learning Prompt* **once, after** a successful `/commit`.
6.  **Keep it simple & undoable** – no big-bang refactors without a separate ticket.
7.  **Wrap-up** – append a **Review** section to `todo.md`, noting follow-ups.

### 🔒 Security-Audit Prompt (run before `/commit`)

> "Audit the staged diff for leaked secrets, unsafe input handling, or insecure file access.
> Respond **OK** or list concrete issues."

### 🧑‍🏫 Learning Prompt (run after `/commit`, once per commit)

> "Explain what this commit adds, why, and how a junior dev can extend or test it."

---

### 📚 Snippet Registry – _when to /open extra prompts_

| Snippet file                              | Auto-trigger condition                                                  | Manual command                                    |
| ----------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------- |
| `docs/CLAUDE_CODE/prompt_snippets/CodeFarm_v9.md`     | When a `/todo` file lists **>2 files** OR user types **"/open CodeFarm"** | `/open docs/CLAUDE_CODE/prompt_snippets/CodeFarm_v9.md`       |
| `docs/CLAUDE_CODE/prompt_snippets/Dev_Companion.md`   | You ask to *Review / Explain / Refactor / Document / Test* an existing file | `/open docs/CLAUDE_CODE/prompt_snippets/Dev_Companion.md`     |
| `docs/CLAUDE_CODE/prompt_snippets/Code_Translator.md` | You type "translate this <lang A> → <lang B>"                           | `/open docs/CLAUDE_CODE/prompt_snippets/Code_Translator.md`   |

*Claude: load a snippet when its condition matches; `/forget <file>` after the task to free tokens.* 