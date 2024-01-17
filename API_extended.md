After having built the Comments feature (with comments being posted to a Link by calling the `/api/comments/[commentID]/comment` endpoint), we now want to implement a way to **report** inappropriate comments.

Our system will receive **Reports** through an empty POST request to `/api/comments/[commentID]/report`. A **Report** does not contain any data except the datetime at which the report made.

Once our system has received the **Report**, it needs to **transfer** it to an external API. Our system must then make a call to `https://commentreporter.com/api/report` with the following payload:

```json
POST https://commentreporter.com/api/report
{
    "link_id": 1,
    "link_url": "https://example.com/badlink",
    "reported_at": "2023-05-04T05:27:16+0000"
}
```

In the context of this exercice, all calls to that API will be **mocked** and will not actually perform a real HTTP request. The `commentreporter` API returns no data, and will always returns either a HTTP 200 code (success), or a 500 HTTP code (failure). 

One important detail is that the `commentreporter` API is **flaky**: whenever we send it a request, we have **no guarantee** that it will sucessfully receive it. Our system needs to guarantee that `commentreporter` will **eventually receive** our Reports, so a system to handle failures and retries has to be implemented. Sometimes, the API can be down for hours at a time.

Tasks:
- Implement the Report API endpoint and model in our system.
- Implement the mock `commentreporter` external API, which will arbitrarily succeed or fail. Out of a 100 requests, `commentreporter` fails 90 times (HTTP 500), and succeeds 10 times (HTTP 200).
- Implement a way for our system to guarantee that for each Report we receive, one (and only one) successful call to `commentreporter` will be made.

