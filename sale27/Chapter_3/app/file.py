
class File(object):

    def __init__(self, filepath=None, mode="rw"):
        self.filepath = filepath
        self.mode     = mode
        self.fp       = None


    def read(self, filepath = None, mode = None):

        if filepath and not self.filepath:
            self.filepath = filepath

        if mode and not self.mode:
            self.mode = mode

        if not self.fp:
            self.fp = open(self.filepath, self.mode)

        buf = self.fp.read()  # entire file

        return buf

if __name__ == "__main__":
    filename    = r"/tmp/file.txt"
    fp          = open(filename, "w")
    fp.write("ABC\n")
    fp.close()
    file = File(filename)
    print(file.read())
