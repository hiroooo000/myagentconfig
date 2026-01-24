---
name: notification
description: A skill to notify a message to Discord with the current project name.
---

# Discord Notification Skill

This skill provides the capability to send notifications to Discord, clearly identifying the source Project Name.

## Capability

- **Notify Project Status**: Sends a formatted message `[Project Name] Message` to the configured Discord channel.
- **Error Reporting**: Supports error notifications with `@everyone` mention for urgent attention.

## Usage

This skill requires two arguments: the **Project Name** and the **Message content**.

```bash
python3 scripts/notify_skill.py <Project Name> <Message>
```

### Example

```bash
python3 scripts/notify_skill.py "Antigravity" "Build process completed successfully."
```

## File Structure

```
notification/
├── SKILL.md                    # This file (Skill Definition)
├── README.md                   # Detailed setup guide
├── .env                        # Environment variables (Git ignored)
├── .env.example                # Environment variable template
├── .gitignore                  # Git ignore settings
└── scripts/
    └── notify_skill.py         # Notification script
```

## Troubleshooting

### Error: Arguments required

```
Usage: python notify_skill.py <project_name> <message>
```

**Solution**:
Ensure you provide both the Project Name and the Message as arguments.

### Error: Environment variable not found

```
[Error] 環境変数 NOTIFY_ANTIGRAVITY_TO_DISCORD_WEBHOOK_URL が見つかりません
```

**Solution**:
Check if `.env` exists and contains the valid Webhook URL.

## Setup

See `README.md` for detailed setup instructions.
