# TODO List

## Needs fixing:

- Use type annotations for python 3.5.

    Used:
    ```
    def file_from(url, filename):
        return None
    ```
    Needs:
    ```
    def file_from(url: str = None, filename: str = None) -> bool:
        return False
    ```
- In pyCharm the inspector needs to exclude the python rules for MarkDown files like Todo.md

- All the excepts with more than one error could be group with except (AttributeError, IndexError, etc.)

- For the condition "if path is None:" to "if not path:"

- Change asserts false and true (self.assertFalse) for Equal

- Do I need to add real test for delete file ad directory?

- Check if I put the patches in the class versus the method.

- Refactored all the imports when I use in the test imports for example curl but it was imported in the production code,
  I need to call this from the production code.


### PyCharm

- Exclude from the mark down files the python inspection.
  Reported in this [post](https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000686644)
- Missing inspection warning for python code in test files.
  Reported in this [post](https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000686744)  
