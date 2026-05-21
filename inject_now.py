"""Inject now.md content into the NOW section of README.md."""
import re

now_content = open("now.md", encoding="utf-8").read().strip()
readme = open("README.md", encoding="utf-8").read()

new_block = "<!-- NOW:START -->\n" + now_content + "\n<!-- NOW:END -->"
updated = re.sub(
    r"<!-- NOW:START -->.*?<!-- NOW:END -->",
    new_block,
    readme,
    flags=re.DOTALL,
)

open("README.md", "w", encoding="utf-8").write(updated)
print("Done.")
