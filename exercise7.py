from pygame import mixer
import  datetime
from time import  time
eye_alarm = "eyes.mp3"
#init_eye = time()
exercise_alarm = "exercise.mp3"
water_alarm = "water.mp3"
eyes_timeout = "10"
exercise_timeout = "45"
water_timeout = "50"

x= datetime.datetime.now()

def play_alarm (alarm_name,stopper):

    # Starting the mixer
 mixer.init()

    # Loading the song
 mixer.music.load(alarm_name)

    # Setting the volume
 mixer.music.set_volume(0.7)

    # Start playing the song
 mixer.music.play()

 while True:
  a = input()
  if a == stopper :
   mixer.music.stop()
   break


def write_logs(msg):
 with open("mylogs.txt","a") as f:
   f.write(f"{msg} {datetime.datetime.now()}\n")



if __name__ == '__main__':
  init_water =time()
  init_eyes = time()
  init_exercise = time()
  watersecs = 10
  exercisesecs = 20
  eyessecs = 30
  while True:
    if time()-init_water > watersecs:
           print("water drinking time is here.type 'drank water' to stop the alarm")
           play_alarm(water_alarm,'drank water')
           write_logs("drank water at")
           init_water = time()

    if time() - init_exercise > exercisesecs:
             print("water drinking time is here.type 'did exercise' to stop the alarm")
             play_alarm(exercise_alarm, 'did exercise')
             write_logs("did exercise at")
             init_exercise = time()

    if time() - init_eyes > eyessecs:
             print("water drinking time is here.type 'did eye exercise' to stop the alarm")
             play_alarm(eye_alarm, 'did eye exercise')
             write_logs("did eye exercise")
             init_eyes = time()