import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
           return json.load(file) 
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*"*50)
    print("\n")
    for index,video in enumerate(videos,start=1):
        print(f"{index}.{video['Name']} , Duration.:{video['Time']}")
    print("\n")
    print("*"*50)
        
def add_video(videos):
    name = input("Enter Video Name.: ")
    time = input("Enter Video Time.: ")
    videos.append({"Name":name, "Time":time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the Video No. to update.: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name.: ")
        time = input("Enter the new Video Time.: ")
        videos[index-1] = {'Name':name, 'Time':time}
        save_data_helper(videos)
    else:
        print("Invalid No. Selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the Video No. you want to Delete.: "))
    
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid Video No.")


def main():
    videos = load_data()
    while True:
        print("\n Youtuber Manager | choose an option")
        print("1.List all Youtube Video")
        print("2.Add a Youtube Video")
        print("3.Update a Youtube Video details")
        print("4.Delete a Youtube Video")
        print("5.Exit the App")

        choice = input("Enter Your Choice.: ")
        # print(videos)
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()
