from pygoogle_image import image as pi


def Image_Downloader(Data_Name , Data_Limit):
    for value in Data_Name:
        print(value)
        pi.download(keywords=value, limit=Data_Limit)


Data_List = ['Airbus-A320' , 'Airbus-A330' , 'Airbus-A350' , 'Airbus-A380']
Limit_Number = 100

Image_Downloader(Data_List,Limit_Number)