"""Simple text-analysis feature."""


def analyze_text(text: str) -> dict[str, int]:
	"""Return basic character, word, and line counts for *text*."""
	return {
		"characters": len(text),
		"words": len(text.split()),
		"lines": len(text.splitlines()),
	}
