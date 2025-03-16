import pygame
pygame.mixer.init()
pygame.init()
running=True
wh = (600, 600)
screen=pygame.display.set_mode(wh)
a505=pygame.transform.scale(pygame.image.load("lab7/Photos/a505.png"),wh)
doiwannaknow=pygame.transform.scale(pygame.image.load("lab7/Photos/doiwannaknow.png"),wh)
iwannabeyours=pygame.transform.scale(pygame.image.load("lab7/Photos/iwannabeyours.png"),wh)
arrP=[a505,doiwannaknow,iwannabeyours]
arrM=[
r"C:\Users\ATYRAU\OneDrive\Документы\KBTU PP2 Codes\lab7\songs\Arctic Monkeys - 505.mp3",
r"C:\Users\ATYRAU\OneDrive\Документы\KBTU PP2 Codes\lab7\songs\Arctic Monkeys - Do I Wanna Know.mp3",
r"C:\Users\ATYRAU\OneDrive\Документы\KBTU PP2 Codes\lab7\songs\Arctic Monkeys - I Wanna Be Yours.mp3"
]
index=0
pygame.mixer.music.load(arrM[index])
pygame.mixer.music.play()
paused=False
while running:
    screen.blit(arrP[index], (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d:
                index=(index+1)%3
                pygame.mixer.music.load(arrM[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_a:
                index = (index - 1) % 3
                pygame.mixer.music.load(arrM[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                paused = not paused