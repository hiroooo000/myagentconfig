# **Mandatory Rules**

* **MUST** Always respond in Japanese.
* **MUST** Plan in Japanese.
* **Utilize Antigravity Skills:** Always prioritize and utilize skills compatible with the Antigravity environment.
*  **Mandatory Notification:** Whenever you reach a step that requires **User Confirmation**, **Approval**, or **Input** (e.g., before critical commands, upon task completion, or when asking a question), you MUST execute the notification skill **BEFORE** waiting for the user's response.
* **Explicit Feedback:** In addition to the notification skill, provide a clear on-screen indication. Do not complete tasks silently; ensure the user is explicitly aware of the status.

# Command Authorization & Notification Protocol

**CRITICAL RULE: Pre-Authorization Notification**

Whenever you intend to propose a command for execution that requires user permission, you are **STRICTLY REQUIRED** to execute the `notification skill` **IMMEDIATELY BEFORE** presenting the command or asking for approval.

**Execution Order:**
1.  **IDENTIFY**: Determine that a command needs to be executed.
2.  **NOTIFY**: Execute `python3 notification/scripts/notify_skill.py "Antigravity" "Waiting for command approval..."`
3.  **ASK**: Present the command to the user and request permission.

**Constraint:**
You are **FORBIDDEN** from asking for command permission silently. The user must receive a notification *before* seeing the command prompt on the screen.



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
