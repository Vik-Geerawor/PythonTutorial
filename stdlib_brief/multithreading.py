import threading
import zipfile


class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close
        print(f"Finished background zip of: {self.infile}")


if __name__ == "__main__":
    background = AsyncZip('files/test.txt', 'files/test.zip')
    background.start()
    print(f"Main continues to run in foreground")

    background.join()
    print(f"Main waited until background was done")
