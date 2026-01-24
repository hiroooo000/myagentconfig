---
name: implementation_and_verification
description: strict guide for implementing changes and verifying them based on an approved plan.
---

# Implementation and Verification Skill

This skill ensures that the implementation follows the approved plan strictly, adhering to TDD principles and rigorous verification standards.

## 1. Core Principles

*   **Japanese Output / English Thinking**: strict adherence to user rules. Plan and reason in English for precision, but output all user-facing text (plans, messages) in Japanese.
*   **Plan Driven**: Do NOT deviate from `implementation_plan.md` without user approval.
*   **TDD First**: Always write or update tests BEFORE modifying the implementation code.
*   **Staged Verification**: Verify locally (scoped) before verifying globally (regression).
*   **Clean Finish**: Ensure all checks (lint, build, test) pass before asking for final review.

## 2. Process Workflow

### Phase 1: Preparation (EXECUTION Mode)
1.  **Read Plan**: Review `implementation_plan.md` to identify the current component to work on.
2.  **Order of Operations**: Confirm test files are listed first. If not, re-order your mental queue to tackle tests first.

### Phase 2: TDD Cycle (EXECUTION Mode)
**Goal**: Implement safely.

1.  **RED (Test)**:
    *   Create new test files or update existing ones as per plan.
    *   Run the test to confirm it fails (or at least that the new test case exists and fails).
    *   *Note*: If the full test suite takes too long, run only the relevant test file.
2.  **GREEN (Implement)**:
    *   Modify source code to satisfy the test.
    *   Run the **Scoped Test** to confirm it passes.
3.  **Refactor (Optional)**:
    *   Clean up code while keeping tests passing.

### Phase 3: Verification (VERIFICATION Mode)
**Goal**: Ensure quality and no regressions.

1.  **Scoped Verification**:
    *   Run tests for the specific file/feature.
    *   Fix any immediate issues.
2.  **Full Verification**:
    *   **Lint**: Run project lint command.
    *   **Build**: Run project build command.
    *   **Regression**: Run the FULL test suite.
3.  **Documentation Update**:
    *   Update `README.md` if features changed.
    *   Update source code documentation (Javadoc/TypeDoc) for changed classes/methods.

### Phase 4: Final Review (VERIFICATION Mode via notify_user)
1.  Create `walkthrough.md` (optional but recommended for complex tasks) to summarize results.
2.  Call `notify_user` with the results of your checks.
    *   "Build/Lint/Test passed."
    *   "Documentation updated."

## 3. Checklist for Implementation

- [ ] **TDD Followed?**: Did you see the test fail before making it pass?
- [ ] **Scoped Passed?**: Did the specific feature tests pass?
- [ ] **Regression Passed?**: Did ALL tests pass?
- [ ] **Clean Code?**: Did Lint pass?
- [ ] **Docs Updated?**: Are README and Code Docs updated?
