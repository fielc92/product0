import re


STALE_V02_SIBLING_SKILLS = {
    "product0-orienting-context",
    "product0-shaping-direction",
    "product0-challenging-direction",
    "product0-writing-brief",
    "product0-reviewing-brief",
}

POSITIVE_INVOCATION_RE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?"
    r"(?:invoke|load|use|dispatch|call|run|route\s+to)\s+"
    r"`?(?P<name>product0-(?:orienting-context|shaping-direction|"
    r"challenging-direction|writing-brief|reviewing-brief))`?\b"
)
