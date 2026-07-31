# Contributing

## The one rule

**Edit `resources.yml`. Never edit `README.md`.**

The README is generated. Hand edits get overwritten on the next build, and CI
will fail the pull request with "README.md is stale".

## Adding an entry

Find the right category in `resources.yml` and add an item:

```yaml
      - name: The thing
        url: https://github.com/owner/repo
        by: Who made it
        cost: free            # free | freemium | paid
        level: beginner       # beginner | intermediate | advanced
        time: ~8 hours        # realistic, not promotional
        format: 12 lessons, Python
        status: to-review     # see below
        note: >
          Two or three sentences. What is it, who is it for, and one honest
          thing a newcomer would want to know before starting.
        tags: [llm, rag]
```

Then regenerate and check:

```bash
pip install -r requirements.txt
python scripts/build_readme.py
python scripts/check_links.py
```

Commit both `resources.yml` and the regenerated `README.md`.

## Status values

Be honest here — it's the whole point of the repo.

| Value | Use when |
|---|---|
| `daily-driver` | You use it regularly |
| `completed` | You finished it |
| `in-progress` | You're working through it now |
| `partially-completed` | You did some of it |
| `reviewed` | You've used or read enough to judge it |
| `reference` | You reopen it rather than read it through |
| `to-review` | On the list, not yet assessed — **not an endorsement** |

Anything marked `to-review` is excluded from the "personally vetted" badge count.

## What doesn't get added

- Paid courses without a substantial free preview
- Anything whose main pitch is a certificate rather than a skill
- Affiliate or referral links, in any form
- Tools that haven't had a commit in over a year, unless they're finished
- Entries with a marketing-copy note. Write what you actually think

## Notes on tone

The `note` field is the value of this repo. "Great course!" is worthless.
"Top-down: you train a model in lesson one and learn the theory afterwards" tells
someone whether it suits how they learn.

If you can't write an honest, specific note, the entry probably isn't ready.
