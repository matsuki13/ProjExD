import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900)) # Surface
    screen_rct = screen_sfc.get_rect()            # Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")    # Surface
    bgimg_rct = bgimg_sfc.get_rect()              # Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    #練習３
    kkimg_sfc = pg.image.load("fig/6.png")                  # Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)    # Surface
    kkimg_rct = kkimg_sfc.get_rect()                        # Rect
    kkimg_rct.center = 900, 400                             # Rect

    # 練習５
    bmimg_sfc = pg.Surface((20, 20))                           # Surface
    bmimg_sfc.set_colorkey((0, 0, 0))                          # Surface
    pg.draw.circle(bmimg_sfc, (255, 0, 255), (10, 10), 10)     #爆弾の色変更（追加）
    bmimg_rct = bmimg_sfc.get_rect()                           # Rect
    bmimg_rct.centerx = random.randint(0, screen_rct.width)    # Rect
    bmimg_rct.centery = random.randint(0, screen_rct.height)   # Rect
    vx, vy = +2, +2                                            #爆弾の速度変更（追加）

   

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)

        # 練習２
        for event in pg.event.get():
            if event.type == pg.QUIT: return

    
        # 練習４
        key_states = pg.key.get_pressed()
        # 
        if key_states[pg.K_UP]    == True: 
            kkimg_rct.centery -= 3
            if check_bound(kkimg_rct, screen_rct)[1]==-1:
                kkimg_rct.centery += 3
        if key_states[pg.K_DOWN]  == True:
             kkimg_rct.centery += 3
             if check_bound(kkimg_rct, screen_rct)[1]==-1:
                kkimg_rct.centery -= 3
        

        if key_states[pg.K_LEFT]  == True:
            kkimg_rct.centerx -= 3
            print(kkimg_rct.left)
            print(check_bound(kkimg_rct, screen_rct))
            if check_bound(kkimg_rct, screen_rct)[0]==-1:
                kkimg_rct.centerx += 3
        if key_states[pg.K_RIGHT] == True:
             kkimg_rct.centerx += 3 
             if check_bound(kkimg_rct, screen_rct)[0]==-1:
                kkimg_rct.centerx -= 3                                  #こうかとんの移動距離変更（追加）
        # 練習７
        # if check_bound(bmimg_rct, screen_rct) != (1, 1):
        bmimg_rct.centery += 1
        bmimg_rct.centery -= 1
        bmimg_rct.centerx += 1
        bmimg_rct.centerx -= 1 
        screen_sfc.blit(bgimg_sfc, bgimg_rct)
        bgimg_rct.move_ip(1, 1)                                         #背景移動（追加）#こうかとんと爆弾の移動履歴（追加）

        screen_sfc.blit(bmimg_sfc, bmimg_rct)

       

        # 練習６


        bmimg_rct.move_ip(vx, vy)
       
        
        # 練習５
        screen_sfc.blit(kkimg_sfc, kkimg_rct)
        
        
        # 練習７
        yoko, tate = check_bound(bmimg_rct, screen_rct)
        vx *= yoko
        vy *= tate

        if kkimg_rct.colliderect(bmimg_rct):
            return

       
        pg.display.update()
        clock.tick(1000)
    
def check_bound(rct, screen):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''

    yoko, tate = 1, 1
    if rct.left < screen.left or rct.right > screen.right:
        yoko = -1
        
    if rct.top < screen.top or rct.bottom > screen.bottom:
        tate = -1
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()