from typing import Dict, List, Union

from validators import url as is_valid_url

import repo
from common.errors import InvalidUrlError, LinkNotFoundError


def list_all_links() -> List:
    return repo.list_all_links()


def link_details(link_id: int) -> Union[Dict, None]:
    try:
        return repo.link_details(link_id)
    except LinkNotFoundError:
        return None


def add_link(link_json: dict) -> int:
    url_ = link_json.get('url')
    if not url_ or not is_valid_url(url_):
        raise InvalidUrlError
    return repo.add_link(link_json)


def upvote_link(link_id: int) -> Union[Dict, None]:
    try:
        return repo.upvote_link(link_id)
    except LinkNotFoundError:
        return None


def downvote_link(link_id: int) -> Union[Dict, None]:
    try:
        return repo.downvote_link(link_id)
    except LinkNotFoundError:
        return None


def truncate() -> None:
    repo.truncate()
