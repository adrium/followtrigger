# FollowTrigger

This script endlessly reads the output of a process and triggers a command on a match.

It is intended as a mini fail2ban alternative.

## Configuration

```json
{
	"follow": ["tail", "-F", "/path/to/file-to-follow" ],
	"trigger": "/path/to/command to execute for matched {subject} (with regex {name})",
	"watches": {
		"name-of-regex1": { "search": "auth failed", "subject": "([0-9.]{7,15})" },
		"name-of-regex2": { "search": "invalid command", "subject": "([0-9.]{7,15})" },
		"...": {}
	}
}
```
