Analyze `/app/access.log` and write the result to `/app/report.json`.

Success criteria:

1. **Output contract:** `/app/report.json` exists and contains a JSON object with
   exactly the fields `total_requests`, `unique_ips`, and `top_path`. The two count
   fields are JSON integers (booleans are not accepted), `top_path` is a JSON
   string, and there are no additional fields.
2. **Total requests:** `total_requests` equals the number of non-empty log lines.
3. **Unique clients:** `unique_ips` equals the number of distinct client IP
   addresses, where the client IP is the first whitespace-delimited field of each
   log line.
4. **Most popular path:** `top_path` is the request path that appears most often in
   the quoted HTTP requests. If multiple paths have the same count, use the one
   that appears first in the log.
