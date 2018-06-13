import sys
import image_merge as image
import hide_text as text


def main():
    if(len(sys.argv) > 2):
        steg(sys.argv[1], sys.argv[2])
    else:
        desteg(sys.argv[1])


def steg(cover_path, hidden_path):
    '''
    Function to hide data (either an image or text) within another image
    INPUT: string, path to the cover image; string, path to the hidden data
    OUTPUT: a new image with the hidden data encoded in the least significant
    bits
    '''
    if hidden_path[-4:] == '.txt':
        text.encrypt(cover_path, hidden_path)
    else:
        image.merge(cover_path, hidden_path)


def desteg(image_path):
    '''
    Function to decode hidden data in an image
    INPUT: string, path to the coded image
    OUTPUT: If hidden data is an image, the hidden image is saved. If hidden
            data is text, the text is saved.
    '''
    try:
        text.decrypt(image_path)
    except:
        image.unmerge(image_path)


if __name__ == "__main__":
    main()
