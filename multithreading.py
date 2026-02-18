import threading
import time



def dog(dname):
    time.sleep(8)
    print(f"You finished taking out {dname}")


def trash():
    time.sleep(2)
    print("You have taken out the trash")
    
def mail():
    time.sleep(4)
    print("You have taken the mail out")


chore1= threading.Thread(target=dog ,args=("Dontolliver",))
chore2=threading.Thread(target=trash)
chore3=threading.Thread(target=mail)


chore1.start()
chore2.start()
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete")