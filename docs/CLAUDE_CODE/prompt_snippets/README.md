# Prompt Snippets

This directory contains "heavy" or specialized prompts that should not be loaded into the AI's context on every request. They are loaded on-demand based on the rules in the `Snippet Registry` found in the root `CLAUDE.md` file.

-   **`CodeFarm_v9.md`**: A multi-persona prompt for building large or complex features.
-   **`Dev_Companion.md`**: A prompt that instructs the AI to act as a senior developer for tasks like code reviews, refactoring, or documentation.
-   **`Code_Translator.md`**: A specialized prompt for translating code from one language to another. 