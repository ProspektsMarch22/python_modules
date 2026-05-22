#!/usr/bin/env python3

def secure_archive(file_name: str, mode: str,
                   content: str | None = None) -> tuple[bool, str]:
    try:
        with open(file_name, mode) as f:
            if mode == "r":
                return (True, f.read())
            elif mode == "w":
                if content is None:
                    return (False, "No content provided for write mode")
                f.write(content)
                return (True, content)
            else:
                return (False, f"Unsupported mode: '{mode}'")
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a non-existent file:")
    print(secure_archive('non/existing/file', 'r'))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('litany.txt', 'r'))
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive('ancient_fragment.txt', 'r'))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive('new_file.txt', 'w',
                         'Content successfully written to file'))


if __name__ == '__main__':
    main()
