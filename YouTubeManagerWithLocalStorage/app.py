
import json

def loadData():
    try:
        with open("ytInfo.txt", "r") as file:
            test = json.load(file)
            return  test
    
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open("ytInfo.txt","w") as file:
        json.dump(videos,file)   

def list_all_videos(videos):
    for index , video in enumerate(videos , start=1):
        print("*"*50)
        print(f"\n{index}. {video['name']} - {video['duration']}\n")
        print("*"*50)
    if len(videos)==0:
        print("nothing to show --")
def add_video(videos):
    name = input("\nEnter Video Name : ")
    duration = input("\nEnter Video Duration : ")
    videos.append({'name':name , "duration":duration})
    save_data_helper(videos)

def update_video(videos):
    # print(videos)
    index = int(input("\nIndex of Video To Update: "))
    if len(videos) > index > 0 :
         name = input("\nEnter Video Name : ")
         duration = input("\nEnter Video Duration : ")
         videos[index-1] = {'name' : name , 'duration' : duration}
    
         save_data_helper(videos)

def delete_video(videos):
    index = int(input("\nIndex of Video to Delete: "))
    if len(videos) >= index > 0 :
        videos.pop(index-1)
        save_data_helper(videos)
    else:
        print("ok")
def main():
    videos = loadData()
    # print(videos)
    while 1 :
        print("\n YouTube Manager")
        print("\n 1. List all Youtube Videos")
        print("\n 2. Add a Youtube Video")
        print("\n 3. Update a Youtube Video")
        print("\n 4. Delete a Youtube Video")
        print("\n 5. Exit the App")
        #User Input
        choice = input("\nEnter Your Wish : ")
        # print(videos)

        match choice :
            case "1" : 
                list_all_videos(videos)
            case "2" :
                add_video(videos)
            case "3" :
                update_video(videos)
            case "4" :
                delete_video(videos)
            case "5" :
                print("Thank You")
                break
            case _ :
                print("invalid CHOICE")
if __name__ == "__main__": #if there is any main name method is in this file , then run this below code
    main()    