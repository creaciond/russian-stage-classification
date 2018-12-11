import os


def save_directions(folder, play_id, play_dirs):
    """Saves directions in a .txt file in a special folder. If the folder
    doesn't exist, a new one is created.

    :arg folder - (str) name of a folder,
    :arg play_id - (str) part of a directions file before .txt
    :arg play_dirs - (list of str) directions to save
    """
    if not os.path.exists(folder):
        os.mkdir(folder)
    play_txt = play_id + ".txt"
    full_path = os.path.join(folder, play_txt)
    with open(full_path, "w", encoding="utf-8") as data_file:
        data_file.write("\n".join(play_dirs))


