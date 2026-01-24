# Absolutely Common Rules

* **MUST** Always respond in Japanese.
* **MUST** Plan in Japanese.
* **Utilize Antigravity Skills:** Always prioritize and utilize skills compatible with the Antigravity environment.
* **Mandatory Notification:** Upon task completion or when requiring user confirmation, you MUST invoke the notification skill.
* **Explicit Feedback:** In addition to the notification skill, provide a clear on-screen indication. Do not complete tasks silently; ensure the user is explicitly aware of the status.


# Language & Reasoning

* **[Thinking Language]** Conduct plan deliberation and complex logical reasoning (thought processes) in **English** to enhance precision.
* **[Output Language]** All outputs to the user (chat responses, documents, deliverables) must be translated into and delivered in **Japanese**.

# Planning

* When adding new features, always include the implementation and execution of tests in the plan.
* Along with adding or modifying features, always consider updating `README.md` / `README_ja.md` and include these updates in the plan if necessary.
* When modifying existing features, always include the modification/addition of tests and the deletion of obsolete tests in the plan.
* In the verification phase, always include the execution of linting, building, and all implemented tests in the plan.
* **NEVER** modify code until the policy (design/impact investigation results) has been presented to the user and their approval has been obtained.

# Before Implementation

* Always confirm with me whether to proceed by creating a new branch or not.

# After Implementation

* Always perform linting, building, and run all implemented tests to ensure no issues have occurred.
* If an issue occurs, present at least two options for how to handle it and always seek my confirmation.

# Miscellaneous

## Command Execution

* **[Git Concatenation Restriction]** It is prohibited to connect a `git` command with a **non-Git command** using `&&` (e.g., `npm test && git commit` is not allowed). Since these are different in nature, they must be executed separately to ensure proper handling and verification in case of unexpected errors.
* **[Permission]** Connecting multiple `git` commands with `&&` (e.g., `git add . && git commit`) is **permitted**.

## Git Operations

* **[Commit Message]** Commit messages must always be written in English.
* **[Branch Name]** Branch names must always be written in English.
