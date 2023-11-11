import time
from plyer import notification

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10,  # Notification will disappear after 10 seconds
    )

if __name__ == "__main__":
    title = "HELLO SUBHAN DO THIS"
    message = "1 learn python"
    message = '2 make a project '

    # Display the notification
    notify(title, message)
    print("LEARN CODING")


w = 0
while w<10:
    notify(title, message)
    w+=1
