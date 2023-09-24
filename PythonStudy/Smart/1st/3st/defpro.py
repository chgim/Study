# a = {"name": "chanho"}

# print(a["name"])  # chanho
# print(a["class"])  # error


def load_database(options: dict):
    """
    options: {
    host: ...
    port: ... (optional, default: 5432)
    }
    """
    print(options.get("port", 5432))
    # if "port" not in options:
    #     raise TypeError("options need port value")
    # print(options["port"])


load_database({"host": "localhost"})
