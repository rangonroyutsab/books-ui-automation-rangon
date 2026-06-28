from urllib.parse import urljoin


def build_absolute_url(base_url: str, href: str) -> str:
    """ 
    Generates an absolute URL 
    by joining a base URL with a relative href. 
    """

    return urljoin(base_url, href)