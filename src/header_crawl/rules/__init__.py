from .standard import ServerHeaderRule, ContentEncodingRule

# List of all active rules
ACTIVE_RULES = [
    ServerHeaderRule(),
    ContentEncodingRule(),
]
