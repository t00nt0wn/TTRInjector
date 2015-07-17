import decompression #pytthon decompression module..
import file

def initdepress():
  decompression.initdecompression(mode=depression) #tabs ftw xD xD xD
  file.open(decompression)

def depressbytes(bytes):
  decompression.decompress(bytes, mode=depression)

def depressoverflow(bytes):
  decompression = decompression.decompress(bytes, mode=depression)
  decompression.overflow()
