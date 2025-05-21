import os
import re

# 设置你要处理的文件夹路径
folder = "./"  # 或替换为具体路径，例如 "./content/posts"

for filename in os.listdir(folder):
    if not filename.endswith(".md") or filename == "_index.md":
        continue

    filepath = os.path.join(folder, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    doi_url = None
    bib_path = None

    for line in lines:
        if line.strip().startswith("**Source**"):
            continue  # 删除 Source 行
        elif line.strip().startswith("[Download Paper]"):
            match = re.search(r"\((https?://[^\s)]+)\)", line)
            if match:
                doi_url = match.group(1)
            continue  # 不保留这一行
        elif line.strip().startswith("[Download BibTeX]"):
            match = re.search(r"\((bib/[^\s)]+\.bib)\)", line)
            if match:
                bib_path = match.group(1)
            continue  # 不保留这一行
        else:
            new_lines.append(line.rstrip())

    # 添加按钮 HTML
    if doi_url and bib_path:
        button_block = f'''
<div style="margin-top: 1rem; padding: 1rem; display: inline-block;">

  <a href="{doi_url}" target="_blank" style="background-color: #0d9bdc; color: white; padding: 10px 16px; margin-right: 8px; text-decoration: none; border-radius: 4px; font-weight: bold;">
    Download Paper
  </a>

  <a href="{bib_path}" download style="background-color: #f0a500; color: white; padding: 10px 16px; text-decoration: none; border-radius: 4px; font-weight: bold;">
    Download BibTeX
  </a>

</div>'''.strip()
        new_lines.append("")
        new_lines.append(button_block)

    # 写回原文件
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines) + "\n")

print("✅ 所有 Markdown 文件已处理完毕。")
