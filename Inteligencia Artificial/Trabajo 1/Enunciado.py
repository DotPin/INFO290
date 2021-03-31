# Tarea: Taxi

#En grupos de tres estudiantes resuelvan el ambiente ["Taxi-v3"](https://gym.openai.com/envs/Taxi-v3/)


#- Describa detalladamente el ambiente (estados posibles, acciones posibles, recompensas, etc)

#R: Estados posibles 500
#R Acciones posee 6 acciones deterministas
#R Recompensas de cada acción:
#       * -1 por cada acción, +20 por cada pasajero en viaje
#       *-10 por acciones de subir y bajar ilegalmente.

#- Utilice $\epsilon$ greedy Q-learning para entrenar un agente que resuelva el problema
#- Muestre en una gráfica la evolución de la recompensa promedio de su agente

# Cuide su salud, discutan el problema y la solución usando herramientas de teletrabajo (whereby.com, google talk, skype, slack)

from gym import wrappers
import matplotlib.pyplot as plt
import numpy as np
import gym 


env = gym.make("Taxi-v3")
env = wrappers.Monitor(env, './video', video_callable=lambda episode_id: True,force=True)
env.reset()
frames = []
for t in range(1000):
    #Render to frames buffer
    env.render()
    a = env.action_space.sample() #politica aleatoria
    q, r, end, info = env.step(a)
    frames.append(q)
    if end:
        break
env.close()

print(frames)   #conjunto de estados
print(q)        #estados
print(r)        #recompensas
print(info)     #entrega la probabilidad acumulada

There is a reward of -1 for each action and an additional reward of +20 for delivering the passenger. There is a reward of -10 for executing actions "pickup" and "dropoff" illegally.
    
