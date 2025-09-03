import csv
from markupsafe import Markup, escape
import xml.etree.ElementTree as ET
import subprocess
import sys
from pathlib import Path

def define_env(env):
    @env.macro
    def csv_to_markdown_table_plain(csv_rel_path):
        """
        Read a CSV file and return its content as a Markdown table.
        - csv_rel_path: relative path to the CSV file
        """
        csv_path = Path(csv_rel_path)
        if not csv_path.exists():
            return f"Error: CSV file not found at {csv_rel_path}"

        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)

        if not rows:
            return "Error: CSV file is empty"

        # Generate Markdown table
        table = []
        table.append("| " + " | ".join(rows[0]) + " |")
        table.append("| " + " | ".join(["---"] * len(rows[0])) + " |")
        for row in rows[1:]:
            table.append("| " + " | ".join(row) + " |")

        return "\n".join(table)

    @env.macro
    def csv_to_markdown_table(csv_rel_path):
        csv_path = Path(csv_rel_path)
        if not csv_path.exists():
            return f"Error: CSV file not found at {csv_rel_path}"

        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        if not rows:
            return "Error: CSV file is empty"

        # Group by section_id/section_name
        topics = {}
        for row in rows:
            section_id = row["section_id"]
            section_name = row["section_name"]
            subtopic_id = row["subtopic_id"]
            subtopic_name = row["subtopic_name"]

            if section_id not in topics:
                topics[section_id] = {
                    "name": section_name,
                    "subtopics": []
                }
            topics[section_id]["subtopics"].append((subtopic_id, subtopic_name))

        # Generate Markdown table
        table = []
        table.append("| Topic Number | Topic Name | Subtopic Number | Subtopic Name |")
        table.append("|--------------|------------|-----------------|---------------|")

        for section_id, data in topics.items():
            for i, (subtopic_id, subtopic_name) in enumerate(data["subtopics"]):
                if i == 0:
                    # First subtopic: include topic info
                    table.append(f"| {section_id} | {data['name']} | {subtopic_id} | {subtopic_name} |")
                else:
                    # Subsequent subtopics: leave topic columns empty
                    table.append(f"|              |            | {subtopic_id} | {subtopic_name} |")

        return "\n".join(table)

    @env.macro
    def pixi_task_table(env_name=None):
        """
        Generate a Markdown table from the output of `pixi task list`.

        This macro executes `pixi task list` and converts the printed list of tasks
        into a Markdown-formatted table with two columns: **Task** and **Description**.

        Args:
            env_name (str, optional):
                If provided, will be passed to the `-e` option of the `pixi task list` command.
                If None, the command is run without `-e`.

        Returns:
            str:
                A Markdown string containing a table of tasks and their descriptions.
                If the table header cannot be found in the command output, a descriptive
                error message string is returned instead.

        Example usage in Markdown:
            ```markdown
            {{ pixi_task_table("linter") }}  # With specific environment
            {{ pixi_task_table() }}          # Without environment
            ```

        Notes:
            - The parsing relies on finding a line that contains both the words "Task"
            and "Description" (case-sensitive) to detect the table start.
            - The function prints debug information to help with troubleshooting.
        """
        import subprocess
        import re

        print(f"[pixi_task_table] Running pixi task list with env={env_name!r}...")

        cmd = ["pixi", "task", "list"]
        if env_name:
            cmd.extend(["-e", env_name])

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        lines = result.stdout.strip().splitlines()
        if lines:
            print(f"[pixi_task_table] First line of output: {lines[0]}")
        else:
            print("[pixi_task_table] No output from pixi command.")

        # Find the header line more flexibly
        header_index = None
        for i, line in enumerate(lines):
            if "Task" in line and "Description" in line:
                header_index = i
                break

        if header_index is None:
            print("[pixi_task_table] Could not find table header.")
            return "Could not find task list header in output."

        table_lines = lines[header_index + 1:]

        rows = []
        for line in table_lines:
            if not line.strip():
                continue
            parts = re.split(r"\s{2,}", line.strip(), maxsplit=1)
            if len(parts) == 2:
                rows.append(parts)
            else:
                if rows:
                    rows[-1][1] += " " + parts[0]

        md = ["| Task | Description |", "|------|-------------|"]
        for task, desc in rows:
            md.append(f"| `{task}` | {desc} |")

        md_output = "\n".join(md)
        print("[pixi_task_table] Markdown table built:")
        # print(md_output)

        return md_output
