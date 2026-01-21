# this function takes a file name as input and returns the corresponding MIME type based on its extension

def match(file_name):
    match True:
        case _ if file_name.endswith(".gif"):
            return "image/gif"
        case _ if file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
            return "image/jpeg"
        case _ if file_name.endswith(".png"):
            return "image/png"
        case _ if file_name.endswith(".pdf"):
            return "application/pdf"
        case _ if file_name.endswith(".txt"):
            return "text/plain"
        case _:
            return "application/octet-stream"


def main():
    FileExtension = input("File Extension: ").strip().lower()
    print(match(FileExtension))

main()