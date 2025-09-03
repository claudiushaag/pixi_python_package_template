# 📚 Contributing to the Documentation

This page explains **how to edit, add, and style pages** in our documentation using [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

---

## ✏ Editing Existing Pages

!!! note "Quick edit options"
    You can use the **Edit this page** button or the **View source** button (top right) to directly access the page’s source in the repository.

Our documentation lives in the `docs/` folder.
Each `.md` file in this folder corresponds to a page.

**Normal workflow for changing docs:**

1. **Clone the repository** to your local machine.
2. Make your changes to the relevant `.md` files inside the `docs/` folder.
3. Commit your changes to a new branch:
    ```bash
    git checkout -b update-docs
    git add docs/yourfile.md
    git commit -m "Updated docs page"
    ```
4. Push your branch:
    ```bash
    git push origin update-docs
    ```
5. Create a **Pull Request (PR)** from your branch to `main`.

!!! tip
    The site is built **automatically** via CI on every push to `main`.
    You just need to commit and push your changes — no need to manually deploy.

---

## ➕ Adding New Pages

To add a new page:

1. Create a new `.md` file inside the `docs/` folder.
2. Open `mkdocs.yml` and add the new file to the `nav` section:

    ```yaml
    nav:
      - Home: index.md
      - Guide: guide.md
      - New Page: newpage.md
    ```

3. Follow the same **PR workflow** as above to push your changes.

!!! example "Example"
    If you create a file `docs/troubleshooting.md`, add it to `mkdocs.yml` like:
    ```yaml
    nav:
      - Troubleshooting: troubleshooting.md
    ```

---

## 🖥 Building and Previewing Locally

You can run the site locally to preview your changes before pushing.

```bash
pixi run docs
```

Also see [here](pixi.md#documentation-tasks).

---

## Using macros

The documentation uses macros, which calls python code, a few times.
The macros can be found in `docs/scripts/macros.py`.
They need to adhere to the rules set by the [macros-extension](https://mkdocs-macros-plugin.readthedocs.io/en/latest/) of Mkdocs.
The can be utilized by calling with a Jinja themed template and two surrounding curly brackets.
```markdown
{ { info_markdown(["TM1", "TM2"]) } }
```
Here, to not trigger the macro, the curly brackets are divided by a whitespace. To trigger the macro, delete the whitespace.