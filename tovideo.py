import ffmpeg
import os.path

def file_name(t, z):
  return "t={:02d}_z={:03d}.jpg".format(t, z)

def main():
  for z in range(1, 101):
    if not os.path.exists(z):
      os.mkdir(z)
    for t in range(1, 21):
      path = file_name(t, z)
      if os.path.isfile(path):
        print(path)

if __name__ == '__main__':
    main()
    
