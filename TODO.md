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
