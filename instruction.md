Analyze `/app/access.log` and write the result to `/app/report.json`.

The output must be a JSON object containing exactly these fields:

- `total_requests`: the number of non-empty log lines.
- `unique_ips`: the number of distinct client IP addresses. The client IP is the
  first whitespace-delimited field of each log line.
- `top_path`: the request path that appears most often. Extract the path from the
  quoted HTTP request. If multiple paths have the same count, use the one that
  appears first in the log.

All counts must be JSON integers, and `top_path` must be a JSON string. Do not add
any other fields.
