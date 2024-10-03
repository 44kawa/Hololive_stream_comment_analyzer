import pytchat
from Classes import Comment
from Output_file import output_file


def get_chat_data(video_id, ofname) -> list:
    Comment_list = []
    livechat = pytchat.create(video_id=video_id)

    while livechat.is_alive():
        chatdata = livechat.get()
        if type(chatdata) is list:
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
            Comment_list.append(new_comment)

    Txt_list = comment_list_to_txt_list(Comment_list)
    output_file(fname=ofname, txt_list=Txt_list)
    return Comment_list


def comment_list_to_txt_list(comment_list: list) -> list:
    txt_list = [
        "elapsedTime,type,message,author_name,mountString,currency,amountValue,bgColor"]

    for comment in comment_list:
        # line = ','.join([
        #     comment.elapsedTime,
        #     comment.type,
        #     comment.message,
        #     comment.author_name,
        #     comment.amountString,
        #     comment.currency,
        #     comment.amountValue,
        #     comment.bgColor
        # ])
        line = f"{comment.elapsedTime},{comment.type},{comment.message}," \
            f"{comment.author_name},{comment.amountString}," \
            f"{comment.currency},{comment.amountValue},{comment.bgColor}"
        txt_list.append(line)

    return txt_list


if __name__ == "__main__":
    video_id = 'wDpuQvdYh68'
    ofname = 'test_Get_chat_data.csv'
    get_chat_data(video_id, ofname)
