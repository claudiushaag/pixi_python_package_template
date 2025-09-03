# 📄 Markdown Basics (with Examples)

Below you’ll find common Markdown patterns, shown side-by-side with their **source** and **rendered result** using [MkDocs Material Tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/).

---

## 📌 Headings

=== "Markdown"
    ```markdown
    # Heading 1
    ## Heading 2
    ### Heading 3
    ```

=== "Result"
    # Heading 1
    ## Heading 2
    ### Heading 3

---

## 🔗 Links

=== "Markdown"
    ```markdown
    [Internal Link](guidelines.md#metadata)

    [External Link](https://squidfunk.github.io/mkdocs-material/)
    ```

=== "Result"
    [Internal Link](guidelines.md#metadata)

    [External Link](https://squidfunk.github.io/mkdocs-material/)

---

## 💬 Lists

=== "Markdown"
    ```markdown
    Bullet points:

        - Item one
        - Item two
            - Sub-item

    Numbered list:

        1. Point
        2. Point
    ```

=== "Result"
    Bullet points:

        - Item one
        - Item two
            - Sub-item

    Numbered list:

        1. Point
        2. Point

---

## 💻 Code

=== "Markdown"
    ````markdown
    One can run the linter without a lot of commands

    ```bash
    pixi run lint_all
    ```
    ````

=== "Result"
    One can run the linter without a lot of commands

    ```bash
    pixi run lint_all
    ```

---

## 💡 Admonitions

See [here](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) for an explanation of all the different admonitions.

=== "Markdown"
    ```markdown
    !!! note
        This is a note.

    !!! tip
        This is a tip.

    !!! warning
        This is a warning.

    !!! example
        This is an example.
    ```

=== "Result"
    !!! note
        This is a note.

    !!! tip
        This is a tip.

    !!! warning
        This is a warning.

    !!! example
        This is an example.

---

## 🖼 Images

Here, the `attrs-list` extension is used to control the size of the picture.

=== "Markdown"
    ```markdown
    ![Alt text](assets/test.png){: style="height:350px"}
    ```

=== "Result"
    ![Alt text](assets/test.png){: style="height:350px"}

---

## ➕ Emphasis

=== "Markdown"
    ```markdown
    *italic text*
    **bold text**
    ***bold italic***
    ```

=== "Result"
    *italic text*
    **bold text**
    ***bold italic***

For more details, see the [MkDocs Material Markdown Reference](https://squidfunk.github.io/mkdocs-material/reference/).
