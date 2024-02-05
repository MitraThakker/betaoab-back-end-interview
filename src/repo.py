import datetime
from typing import Dict, List

from common.errors import LinkNotFoundError
from src.common.db_ import SQLiteDBConnection


def list_all_links() -> List[Dict]:
    with SQLiteDBConnection() as conn:
        result = conn.execute('''SELECT *, (upvotes - downvotes) as score
                                 FROM links''')
        links = result.fetchall()
    return links


def link_details(link_id: int) -> Dict:
    with SQLiteDBConnection() as conn:
        result = conn.execute(f'''SELECT *, (upvotes - downvotes) as score
                                  FROM links WHERE id={link_id}''')
        link = result.fetchone()
    if not link:
        raise LinkNotFoundError
    return link


def add_link(link_json: dict) -> int:
    with SQLiteDBConnection() as conn:
        cursor = conn.cursor()
        cursor.execute(f'''INSERT INTO links (created_at, url) VALUES
                           ("{datetime.datetime.now()}",
                            "{link_json.get("url", "")}")''')

        link_id = cursor.lastrowid
        cursor.close()
    return link_id


def upvote_link(link_id: int) -> Dict:
    with SQLiteDBConnection() as conn:
        cursor = conn.cursor()
        cursor.execute(f'''UPDATE links SET
                                upvotes = upvotes + 1
                           WHERE id={link_id}''')
        count_ = cursor.rowcount
        cursor.close()
    if not count_:
        raise LinkNotFoundError
    return link_details(link_id)


def downvote_link(link_id: int) -> Dict:
    with SQLiteDBConnection() as conn:
        cursor = conn.cursor()
        cursor.execute(f'''UPDATE links SET
                                downvotes = downvotes + 1
                           WHERE id={link_id}''')
        count_ = cursor.rowcount
        cursor.close()
    if count_ == 0:
        raise LinkNotFoundError
    return link_details(link_id)


def truncate() -> None:
    with SQLiteDBConnection() as conn:
        cursor = conn.cursor()
        cursor.execute('delete from links')
