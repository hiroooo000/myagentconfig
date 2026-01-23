---
name: design_and_planning
description: A comprehensive guide for conducting design and implementation planning.
---

# Design and Implementation Planning Skill

This skill provides a structured approach to designing and planning changes in the codebase. It ensures high-quality, safe, and verifiable code modifications by mandating a thorough planning phase before any code is written.

## 1. Core Principles

*   **Japanese Output / English Thinking**: strict adherence to user rules. Plan and reason in English for precision, but output all user-facing text (plans, messages) in Japanese.
*   **Safety First**: No code modification without a user-approved plan.
*   **Verification Driven**: Planning must always include verification steps (tests, manual checks).
*   **Documentation Aware**: Planning must consider updates to documentation (README, etc.) AND source code documentation (Javadoc, TypeDoc, etc.).
*   **TDD Friendly**: Plan so that implementation CAN proceed in a Test-Driven manner (Writing tests before implementation).

## 2. Process Workflow

### Phase 1: Requirement Analysis & Research (PLANNING Mode)
**Goal**: Understand WHAT to do and WHERE to do it.

1.  **Analyze User Request**: Identify the core objective.
    *   **Ambiguity Check**: User requests are often incomplete. Actively look for missing details.
    *   **Clarification Loop**: If ambiguous, you MUST ask clarifying questions *before* planning.
    *   **Provide Examples**: When asking, provide multiple concrete examples of what you need (e.g., "Do you want A like [Example] or B like [Example]?").
2.  **Context Research**:
    *   Use `find_by_name`, `grep_search`, `view_file_outline` to find relevant files.
    *   Understand existing patterns and dependencies.
    *   **Crucial**: Check for potential breaking changes.

### Phase 2: Drafting the Implementation Plan (PLANNING Mode)
**Goal**: Document the HOW.

*   **Maintain Structure First**: Start by evaluating if the request can be fulfilled while maintaining the current program structure. Avoid unnecessary refactoring or architectural changes unless explicitly required.
*   **Structural Impact Check**: If the design requires a major structural overhaul:
    *   **Notify**: Explicitly warn the user in the plan (use `notify_user` or the plan's alert section).
    *   **Alternative**: You MUST propose an alternative that minimizes changes by adjusting the requirements, if feasible.

Create or update `implementation_plan.md` in the artifact directory. Use the standard structure:

```markdown
# [Short Title]

## User Review Required
> [!IMPORTANT]
> List any breaking changes, permission requirements, or critical design choices here.

## Design Options (Required for non-trivial tasks)
> **Critical Rule**: For anything other than trivial changes, you MUST propose at least two approaches.
**Option 1: [Name]** ...
**Option 2: [Name]** ...
**Recommendation**: ...

## Proposed Changes (Based on Recommended Option)
### [Component/Directory Name]
> **TDD Tip**: List test files *before* source files to encourage Test-Driven Development.
#### [MODIFY] [filename](file:///path...)
- Description of change.
#### [NEW] [filename](file:///path...)
- Description of new file.
- **Note**: Mention test files here.

## Verification Plan
### Automated Tests
- **Build**: Execute project's build command (Must pass without errors).
- **Lint**: Execute project's lint command (Must pass without errors).
- **Scoped Tests**: Run tests specifically for the modified files/features *first*.
- **Regression Tests**: Execute the full test suite (Run ALL tests only after scoped tests pass).
- **Test Code Maintenance**: Explicitly list test files to be **created** or **updated**.
    *   **Unit Tests**: Required for all logic changes.
    *   **Integration Tests**: Add/update if necessary and possible (e.g., component interaction, end-to-end flows).
### Manual Verification
- Steps to reproduce and verify the fix/feature manually.
```

### Phase 3: Review & Approval (PLANNING Mode via notify_user)
**Goal**: Get user consent.

1.  Use `notify_user` to present the plan.
2.  **Strict Rule**: If the user requests changes, STAY in PLANNING mode, update the plan, and re-request review.
3.  **Only** proceed to EXECUTION after explicit approval.

## 3. Checklist for High-Quality Planning

- [ ] **Clarified?**: Did you confirm requirements? If ambiguous, did you ask with multiple examples?
- [ ] **Maintain Structure?**: Did you prioritize a solution that fits the existing architecture?
- [ ] **Structural Impact?**: If huge changes are needed, did you propose a simpler alternative?
- [ ] **Staged Verification?**: Did you plan for Scoped Tests FIRST, then Regression Tests (including build/lint)?
- [ ] **Test Coverage?**: Did you explicitly plan for Unit Tests and Integration Tests (if needed)?
- [ ] **TDD Considered?**: Are test files listed BEFORE implementation files?
- [ ] **Multiple Options?**: Did you propose at least 2 design/implementation options (unless trivial)?
- [ ] **Docs Updated?**: Did you check requirements for `README` AND source code docs (Javadoc/TypeDoc)?
- [ ] **Impact Analysis?**: Did you consider how this change affects other parts of the system?
- [ ] **Dependencies?**: Are new dependencies really necessary? Can existing ones be used?
- [ ] **Japanese Translation?**: Is the output `implementation_plan.md` in natural, professional Japanese?
