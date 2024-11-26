def test () :
    print("Welcome to YouTube Manager with sqlite")

def list_all_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

def exit():
    pass