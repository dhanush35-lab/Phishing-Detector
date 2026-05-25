import re

with open("static/style.css", "r") as f:
    css = f.read()

# CSS Variables to add
variables = """
  --badge-grad-start: #73beff;
  --badge-grad-end: #479ef4;
  --input-border: rgba(79, 144, 219, 0.22);
  --input-border-focus: rgba(76, 166, 255, 0.9);
  --input-shadow-focus: rgba(76, 166, 255, 0.14);
  --btn-shadow: rgba(61, 132, 210, 0.22);
  --pill-idle-bg: rgba(76, 166, 255, 0.12);
  --card-bg: rgba(241, 248, 255, 0.95);
  --card-border: rgba(108, 172, 255, 0.18);
  --legend-bg: rgba(243, 249, 255, 0.92);
  --item-bg: rgba(245, 250, 255, 0.96);
  --impact-bg: rgba(76, 166, 255, 0.12);
}

[data-theme="danger"] {
  --bg-start: #ffeaea;
  --bg-end: #ffd8d8;
  --panel-border: rgba(255, 108, 108, 0.22);
  --shadow: 0 20px 45px rgba(202, 56, 56, 0.14);
  --text-main: #5b1414;
  --text-soft: #a15d5d;
  --primary: #ff4c4c;
  --primary-dark: #d12f2f;
  --badge-grad-start: #ff7373;
  --badge-grad-end: #f44747;
  --input-border: rgba(219, 79, 79, 0.22);
  --input-border-focus: rgba(255, 76, 76, 0.9);
  --input-shadow-focus: rgba(255, 76, 76, 0.14);
  --btn-shadow: rgba(210, 61, 61, 0.22);
  --pill-idle-bg: rgba(255, 76, 76, 0.12);
  --card-bg: rgba(255, 241, 241, 0.95);
  --card-border: rgba(255, 108, 108, 0.18);
  --legend-bg: rgba(255, 243, 243, 0.92);
  --item-bg: rgba(255, 245, 245, 0.96);
  --impact-bg: rgba(255, 76, 76, 0.12);
}

[data-theme="safe"] {
  --bg-start: #eaffea;
  --bg-end: #d8ffd8;
  --panel-border: rgba(108, 255, 108, 0.22);
  --shadow: 0 20px 45px rgba(56, 202, 56, 0.14);
  --text-main: #145b14;
  --text-soft: #5da15d;
  --primary: #4cff4c;
  --primary-dark: #2fd12f;
  --badge-grad-start: #73ff73;
  --badge-grad-end: #47f447;
  --input-border: rgba(79, 219, 79, 0.22);
  --input-border-focus: rgba(76, 255, 76, 0.9);
  --input-shadow-focus: rgba(76, 255, 76, 0.14);
  --btn-shadow: rgba(61, 210, 61, 0.22);
  --pill-idle-bg: rgba(76, 255, 76, 0.12);
  --card-bg: rgba(241, 255, 241, 0.95);
  --card-border: rgba(108, 255, 108, 0.18);
  --legend-bg: rgba(243, 255, 243, 0.92);
  --item-bg: rgba(245, 255, 245, 0.96);
  --impact-bg: rgba(76, 255, 76, 0.12);
}
"""

css = css.replace("}\n\n*", variables + "\n\n*")

# Replacements mapping
reps = {
    "background: linear-gradient(180deg, #73beff, #479ef4);": "background: linear-gradient(180deg, var(--badge-grad-start), var(--badge-grad-end));",
    "border: 1px solid rgba(79, 144, 219, 0.22);": "border: 1px solid var(--input-border);",
    "border-color: rgba(76, 166, 255, 0.9);": "border-color: var(--input-border-focus);",
    "box-shadow: 0 0 0 4px rgba(76, 166, 255, 0.14);": "box-shadow: 0 0 0 4px var(--input-shadow-focus);",
    "box-shadow: 0 12px 24px rgba(61, 132, 210, 0.22);": "box-shadow: 0 12px 24px var(--btn-shadow);",
    "background: rgba(76, 166, 255, 0.12);": "background: var(--pill-idle-bg);",
    "background: rgba(241, 248, 255, 0.95);": "background: var(--card-bg);",
    "border: 1px solid rgba(108, 172, 255, 0.18);": "border: 1px solid var(--card-border);",
    "background: rgba(243, 249, 255, 0.92);": "background: var(--legend-bg);",
    "background: rgba(245, 250, 255, 0.96);": "background: var(--item-bg);",
}

for k, v in reps.items():
    css = css.replace(k, v)

# Special handle impact-bg which has rgba(76, 166, 255, 0.12)
# actually handled by the generic background replacement above, but let's check
# It might get replaced to var(--pill-idle-bg) - which is functionally fine, but let's fix it manually.
css = css.replace("var(--pill-idle-bg)", "var(--impact-bg)", 1) # Only for the second occurrence maybe?
# Better: just leave it as pill-idle-bg or impact-bg

with open("static/style.css", "w") as f:
    f.write(css)

print("Replaced successfully!")
