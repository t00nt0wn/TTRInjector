import decompressor #panda decompression module..
import file

def initdepress():
  decompressor.initdecompression(mode=depression) #tabs ftw xD xD xD
  file.open(decompression)

def depressbytes(bytes):
  decompressor.decompress(bytes, mode=depression)

def depressoverflow(bytes):
  decompressor = decompressor.decompress(bytes, mode=depression)
  decompressor.overflow()
