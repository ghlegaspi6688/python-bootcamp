class ImageFileValidator:

    def __init__(self, path):
        self.path = path

    def valid(self):
        if self.path == "JPG" or self.path == "JPEG" or self.path == "PNG":
            return 1
        else:
            return 0

class DocumentValidator:
    def __init__(self, path, pages):
        self.path = path
        self.pages = pages

    def valid(self):
        if self.path == "PDF" and self.pages > 0:
            return 1
        else:
            return 0

class AudioFileValidator:
    def __init__(self, path, length):
        self.path = path
        self.length = length

    def valid(self):
        if self.path == "MP3" or self.path == "WAV" and self.length > 0:
            return 1
        else:
            return 0


class VideoFileValidator:
    def __init__(self, path, length, res):
        self.path = path
        self.length = length
        self.res = res

    def valid(self):
        if self.path == "MP4" and self.res == 720 or self.res == 1080 and self.length > 0:
            return 1
        else:
            return 0


validators = (
    #ImageFileValidator()
    #DocumentValidator()
    #AudioFileValidator()
    #VideoFileValidator()

    VideoFileValidator("sport .MP4", 180, 720),
)
for validator in validators:
    print(validator.valid())
