from datetime import datetime
import kong_pdk.pdk.kong as kong

Schema = [
    {"HEADER_NAME": {"type": "string"}},
]
version = "0.1.0"
priority = 1000

class Plugin:
    def __init__(self, config):
        self.config = config

    def access(self, kong: kong.kong):
        header_name = self.config["HEADER_NAME"]
        header_value = kong.request.get_header(header_name)

        if header_value is None:
            return kong.response.error(400, f"Missing header: {header_name}")
        else:
            kong.service.request.set_header("now", str(datetime.utcnow()))
