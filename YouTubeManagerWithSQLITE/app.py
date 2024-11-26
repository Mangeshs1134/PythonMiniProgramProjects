import sqlite3
con = sqlite3.connect("YoutubeManager.db")
cur = con.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
            )
''')

from functions import test , list_all_videos, add_video, delete_video, update_video, exit  # here we learn how to import functions from another files
test()

def main():
    while 1 :
        print("\n YouTube Manager")
        print("\n 1. List all Youtube Videos")
        print("\n 2. Add a Youtube Video")
        print("\n 3. Update a Youtube Video")
        print("\n 4. Delete a Youtube Video")
        print("\n 5. Exit the App \n")
        choice = input("Enter Your Wish : ")

        if choice == "1":
            cur.execute("SELECT * FROM videos")
            for row in cur.fetchall():
                print(row)
        elif choice == "2":
            name = input("\nName of new Video: ")
            duration = input("\nDuration of new Video: ")
            cur.execute("INSERT INTO videos (name , time) VALUES (? ,?)", ( name , duration))
            con.commit()
        elif choice == "3":
            index= input("\nEnter Index you want to Update: ")
            name = input("\nNew name of Video: ")
            duration = input("\nNew duration of Video: ")
            cur.execute("UPDATE videos SET name=?,time=? WHERE id =? ",(name,duration,index))
            con.commit()
        elif choice == "4":
            index= input("\nEnter Index you want to DELETE: ")
            cur.execute("DELETE FROM videos  WHERE id =? ",(index,))
            con.commit()
        elif choice == "5":
            break
            

if __name__ == "__main__": #if there is any main name method is in this file , then run this below code
    main()  