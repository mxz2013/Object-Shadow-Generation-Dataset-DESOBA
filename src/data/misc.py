import os


def check_img_ext(path: str, img_name: str):
    """
    function to check the extention of one image
    with its path and filename
    Parameters
    ----------
    path
    img_name

    Returns
    -------

    """

    possible_ext = [
        ".jpg",
        ".png",
        ".jpeg",
        ".svg",
        ".gif",
        ".jpe",
        ".jp2",
        ".bmp",
        ".dib",
        ".webp",
        ".pbm",
        ".pgm",
        ".ppm",
        ".pxm",
        ".pnm",
        ".tif",
        ".tiff",
    ]
    path = os.path.join(path, img_name)
    for i, ext in enumerate(possible_ext):
        if os.path.exists(path + ext):
            return ext

    print("File extensions are not in the list of \n", possible_ext)

    os.system("ls " + path + "*")
    return None