import os
from pathlib import Path

LINE: str = (
    "Men's 10m Spider Relocation: Britain's Miller slides a postcard under "
    "the pint glass with surgical precision, only for the arachnid to sprint "
    "up his sleeve and claim gold for Australia."
)


def main() -> None:
    raw_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    output_path = Path(raw_path)

    if (
        output_path.is_dir()
        or raw_path.endswith(("/", "\\"))
        or (not output_path.suffix and output_path.name != "entry.txt")
    ):
        output_path = output_path / "entry.txt"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    text = LINE if LINE.endswith("\n") else f"{LINE}\n"
    output_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
