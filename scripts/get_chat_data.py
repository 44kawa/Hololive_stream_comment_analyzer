"""
This module retrieves live chat data from a YouTube video and saves
it to a CSV file. It utilizes the pytchat library for fetching chat data
and converts it into a structured format for saving.
"""

import pytchat
from classes import Comment
from output_file import output_file


def get_chat_data(video_id: str, ofname: str) -> list:
    """
    Fetches live chat data from a YouTube video and saves it to a CSV file.

    Parameters
    ----------
    video_id : str
        The ID of the YouTube video to fetch chat data from.
    ofname : str
        The output file name where the chat data will be saved.

    Returns
    -------
    list
        A list of Comment objects containing the fetched chat data.
    """
    comment_list = []
    livechat = pytchat.create(video_id=video_id)

    while livechat.is_alive():
        chatdata = livechat.get()
        if isinstance(chatdata, list):  # Use isinstance() for type checking
            break

        for comment in chatdata.items:
            new_comment = Comment(comment.elapsedTime,
                                  comment.type,
                                  comment.message,
                                  comment.author.name,
                                  comment.amountString,
                                  comment.currency,
                                  comment.amountValue,
                                  comment.bgColor)
            comment_list.append(new_comment)

    txt_list = comment_list_to_txt_list(comment_list)
    output_file(fname=ofname, txt_list=txt_list)
    return comment_list


def comment_list_to_txt_list(comment_list: list) -> list:
    """
    Converts a list of Comment objects into a list of strings suitable for CSV output.

    Parameters
    ----------
    comment_list : list
        A list of Comment objects to convert.

    Returns
    -------
    list
        A list of strings where each string is a line of the CSV.
    """
    txt_list = [
        "elapsedTime,type,message,author_name,amountString,currency,amountValue,bgColor"]

    for comment in comment_list:
        line = f"{comment.elapsedTime},{comment.type},{comment.message}," \
            f"{comment.author_name},{comment.amountString}," \
            f"{comment.currency},{comment.amountValue},{comment.bgColor}"
        txt_list.append(line)

    return txt_list


if __name__ == "__main__":
    video_id = 'wDpuQvdYh68'
    output_filename = 'test_Get_chat_data.csv'
    get_chat_data(video_id, output_filename)
