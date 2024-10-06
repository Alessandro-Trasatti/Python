# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs
# that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
# .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead,
# which is a common default.

def main():
    filename = input("What is the filename? ").strip().lower()
    mediatype = get_mediatype_long(filename)
    print(mediatype)
    mediatype = get_mediatype_dict(filename)
    print(mediatype)
    

def get_mediatype_long(filename):
    if filename.endswith(".gif"):
        return "image/gif"
    if filename.endswith(".jpg"):
        return "image/jpg"
    if filename.endswith(".jpeg"):
        return "image/jpeg"
    if filename.endswith(".png"):
        return "image/png"
    if filename.endswith(".txt"):
        return "image/txt"
    if filename.endswith(".zip"):
        return "image/zip"
    return "application/octet-stream"

def get_mediatype_dict(filename):
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".txt": "image/txt",
        ".zip": "image/zip"
    }
    for file_type, media_type in media_types.items():
        if filename.endswith(file_type):
            return media_type
    return "application/octet-stream"


if __name__ == "__main__":
    main()