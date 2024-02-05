create table if not exists links (
    id integer primary key,
    created_at datetime,
    url text,
    upvotes int not null default 0,
    downvotes int not null default 0
)