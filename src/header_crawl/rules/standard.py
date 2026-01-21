from .base import HeaderRule

class ServerHeaderRule(HeaderRule):
    @property
    def rule_name(self) -> str:
        return "Server Header Check"

    def evaluate(self, headers: dict) -> str | None:
        server_header = "Server"
        if server_header not in headers:
            return "Missing Server header"
        return f"Webserver: {headers[server_header]}"

class ContentEncodingRule(HeaderRule):
    @property
    def rule_name(self) -> str:
        return "Content-Encoding Check"

    def evaluate(self, headers: dict) -> str | None:
        encoding_header = "Content-Encoding"
        if encoding_header not in headers:
            return "Missing Content-Encoding header. Effect: Larger file sizes and slower load times (no compression)."
        return f"Content-Encoding: {headers[encoding_header]}"
