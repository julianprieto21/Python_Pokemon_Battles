from settings import *
import pygame as pg
from pygame import sprite
import time
import numpy as np

"""
Clase boton recibe posicion y imagen/texto
"""
class Button:
    def __init__(self, x, y, img) -> None:
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    """
    Dibuja boton en pantalla, registra clicks y colision con mouse
    """
    def draw(self, screen) -> bool:
        act = False
        pos = pg.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                act = True
            if pg.mouse.get_pressed()[0] == 0:
                self.clicked = False
        
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return act

    """
    Dibuja selector en pantalla
    """
    def active(self, screen, img, pos):
        if self.rect.colliderect(pos[0], pos[1], 1, 1):
                    # self.buttons[0].active(self.screen, self.gui_img[7])
                    screen.blit(img, (self.rect.topleft[0]-25, self.rect.topleft[1] + 15))

"""
Clase de sprites de pokemones
"""
class Sprites(sprite.Sprite):
    def __init__(self, pok, pos):
        super().__init__()
        self.pokemon = pok
        self.pos = pos
        self.position = "front" if self.pos == 0 else "back"  # 0: Front / 1: Back
        self.image = pg.image.load(DIR+f"sprites/{self.pokemon}_{self.position}.png")
        self.rect = self.image.get_rect()
        if self.pos == 0:
            self.rect.centerx = 1000
            self.rect.centery = 150
        elif self.pos == 1:
            self.rect.centerx = 0
            self.rect.centery = 300
        self.speed = [15, 0]

    """
    Mueve los sprites desde afuera a dentro de la pantalla. Animacion de juego original. No importante
    """
    def update(self) -> None:
        if self.pos == 1:
            if self.rect.left > 90:
                self.speed[0] = 0
            self.rect.move_ip(self.speed[0], self.speed[1])
        elif self.pos == 0:
            if self.rect.right < 850:
                self.speed[0] = 0
            self.rect.move_ip(-self.speed[0], self.speed[1])        

"""
Clase principal del juego. Contiene el main()
"""
class Game:
    def __init__(self) -> None:
        self.user = TEAM[0]
        self.enemy = np.random.choice(ENEMIES)
        self.title = TITLE
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(self.title)
        self.clock = pg.time.Clock()
        self.hp_bar_pixels = 0
        self.gui_img = []
        self.team_icons = []
        self.buttons = []
        self.running = True
        self.interfaz = "eleccion"

    """
    Carga las imagenes de la self.interfaz de usuario y las mete dentro de self.gui_img
    """
    def load_gui_images(self):
        i = np.random.randint(1, 3)
        background = pg.image.load(DIR+f"gui/fondo{i}.png")  # Fondo aleatorio
        bg_option = pg.image.load(DIR+"gui/fondo_eleccion.png")
        text_bar = pg.image.load(DIR+"gui/barra_azul.png")
        option_bar = pg.image.load(DIR+"gui/barra_options.png")
        attack_bar = pg.image.load(DIR+"gui/barra_attacks.png")
        info_f = pg.image.load(DIR+"gui/info_front.png")
        info_b = pg.image.load(DIR+"gui/info_back.png")
        selectA = pg.image.load(DIR+"gui/selector.png")
        selectB = pg.image.load(DIR+"gui/selector_2.png")
        hpF = pg.image.load(DIR+"gui/hp_bar.png") 
        hpB = pg.image.load(DIR+"gui/hp_bar.png")
        self.hp_bar_pixels = hpF.get_width()
        xp_bar = pg.image.load(DIR+"gui/xp_bar.png")
        red = pg.image.load(DIR+"gui/red_button.png")
        click = pg.image.load(DIR+"gui/mouse.png")
        self.gui_img = [background, bg_option, text_bar, option_bar,
                        attack_bar, info_f, info_b, selectA, selectB,
                        hpF, hpB, xp_bar, red, click]

    """
    Carga los botones de la self.interfaz principal y los mete dentro de self.buttons
    """
    def load_buttons(self):
        att_button_text = self.font.render("LUCHA", 0, BLACK)
        att_button = Button(540, 485, att_button_text)
        quit_button_text = self.font.render("SALIR", 0, BLACK)
        quit_button = Button(765, 540, quit_button_text)
        bag_button_text = self.font.render("MOCHILA", 0, BLACK)
        bag_button = Button(765, 485, bag_button_text)
        pok_button_text = self.font.render("POKEMON", 0, BLACK)
        pok_button = Button(540, 540, pok_button_text)
        self.buttons = [att_button, quit_button, bag_button, pok_button]

    """
    Carga los iconos del team y los mete dentro de self.team_icons
    """
    def load_team_icons(self):
        espeonIcon = pg.image.load(DIR+"sprites/icon/espeon_icon_1.png")
        flareonIcon = pg.image.load(DIR+"sprites/icon/flareon_icon_1.png")
        glaceonIcon = pg.image.load(DIR+"sprites/icon/glaceon_icon_1.png")
        jolteonIcon = pg.image.load(DIR+"sprites/icon/jolteon_icon_1.png")
        leafeonIcon = pg.image.load(DIR+"sprites/icon/leafeon_icon_1.png")
        sylveonIcon = pg.image.load(DIR+"sprites/icon/sylveon_icon_1.png")
        umbreonIcon = pg.image.load(DIR+"sprites/icon/umbreon_icon_1.png")
        vaporeonIcon = pg.image.load(DIR+"sprites/icon/vaporeon_icon_1.png")
        self.team_icons = [espeonIcon, flareonIcon, glaceonIcon, jolteonIcon,
                           leafeonIcon, sylveonIcon, umbreonIcon, vaporeonIcon]

    """
    Verifica eventos de teclado
    """
    def check_events(self):
        for e in pg.event.get():

            if e.type == pg.QUIT or pg.key.get_pressed()[pg.K_ESCAPE]:
                self.running = False

    def user_choice(self):
        pos = pg.mouse.get_pos()
        espeonButton = Button(152, 119, self.team_icons[0])
        if espeonButton.draw(self.screen):
            self.user = TEAM[0]
            self.interfaz = "inicio"
        if espeonButton.rect.colliderect(pos[0], pos[1], 1, 1):
            self.screen.blit(self.gui_img[8], (142, 105))

        flareonButton = Button(344, 119, self.team_icons[1])
        if flareonButton.draw(self.screen):
            self.user = TEAM[1]
            self.interfaz = "inicio"
        if flareonButton.rect.colliderect(pos[0], pos[1], 1, 1):
            self.screen.blit(self.gui_img[8], (324, 105))

        glaceonButton = Button(536, 119, self.team_icons[2])
        if glaceonButton.draw(self.screen):
            self.user = TEAM[2]
            self.interfaz = "inicio"
        if glaceonButton.rect.colliderect(pos[0], pos[1], 1, 1):
            self.screen.blit(self.gui_img[8], (526, 105))

        jolteonButton = Button(728, 119, self.team_icons[3])
        if jolteonButton.draw(self.screen):
            self.user = TEAM[3]
            self.interfaz = "inicio"
        if jolteonButton.rect.colliderect(pos[0], pos[1], 1, 1):
            self.screen.blit(self.gui_img[8], (708, 105))

        leafeonButton = Button(152, 268, self.team_icons[4])
        if leafeonButton.draw(self.screen):
            self.user = TEAM[4]
            self.interfaz = "inicio"
        if leafeonButton.rect.colliderect(pos[0], pos[1], 1, 1):
            self.screen.blit(self.gui_img[8], (142, 255))

        sylveonButton = Button(344, 268, self.team_icons[5])
        if sylveonButton.draw(self.screen):
            self.user = TEAM[5]
            self.interfaz = "inicio"
        if sylveonButton.rect.colliderect(pos[0], pos[1], 1, 1):
            self.screen.blit(self.gui_img[8], (325, 255))

        umbreonButton = Button(536, 268, self.team_icons[6])
        if umbreonButton.draw(self.screen):
            self.user = TEAM[6]
            self.interfaz = "inicio"
        if umbreonButton.rect.colliderect(pos[0], pos[1], 1, 1):
            self.screen.blit(self.gui_img[8], (514, 255))

        vaporeonButton = Button(728, 268, self.team_icons[7])
        if vaporeonButton.draw(self.screen):
            self.user = TEAM[7]
            self.interfaz = "inicio"
        if vaporeonButton.rect.colliderect(pos[0], pos[1], 1, 1):
            self.screen.blit(self.gui_img[8], (712, 255))

    """
    Funcion para reducir la barra de vida en pantalla proporcionalmente a los hp actuales
    """
    def loss_hp(self, damage, pok, current):
        x = (damage*self.hp_bar_pixels/pok.hp)
        current -= x
        return 0 if current < 0 else current

    def enemy_attack(self, hp_pixels):
        user_hp, damage = self.enemy.attack_cpu(self.user)
        hp_pixels = self.loss_hp(damage, self.user, hp_pixels)
        self.gui_img[-4] = pg.transform.scale(self.gui_img[-4], (hp_pixels, 12))
        first_attack_pp_text, scratch_pp_text = self.show_info(self.screen)
        if user_hp == 0:
            self.interfaz = "enemy_win"

    def show_info(self, screen):
        user_name_text_black = self.font.render(self.user.name, 0, BLACK)
        user_hp_text = self.font.render(f"{self.user.current_hp}/{self.user.hp}", 0, BLACK)
        user_lvl_text = self.font.render(f"Lv{self.user.level}", 0, BLACK)
        enemy_level_text = self.font.render(f"Lv{self.enemy.level}", 0, BLACK)
        enemy_name_text = self.font.render(self.enemy.name, 0, BLACK)
        
        first_att_pp_text = self.font.render(f"{self.user.attacks[1].current_pp}/{self.user.attacks[1].pp}", 0, BLACK)
        scratch_pp_text = self.font.render(f"{self.user.attacks[0].current_pp}/{self.user.attacks[0].pp}", 0, BLACK)

        screen.blit(self.gui_img[5], (70, 60))
        screen.blit(self.gui_img[6], (460, 296))
        screen.blit(self.gui_img[-5], (222, 128))
        screen.blit(self.gui_img[-4], (648, 364))
        
        screen.blit(user_name_text_black, (522, 302))
        screen.blit(user_hp_text, (720, 373))
        screen.blit(user_lvl_text, (764, 302))
        screen.blit(enemy_level_text, (338, 66))
        screen.blit(enemy_name_text, (94, 66))
        return first_att_pp_text, scratch_pp_text


    """
    Funcion principal de inicio de juego
    """
    def main(self):
        pg.init()
        self.interfaz = "eleccion"
        enemy_hp_pixels = 196 #self.hp_bar_pixels
        user_hp_pixels = 196 # self.hp_bar_pixels
        self.font = pg.font.Font(DIR+"font.ttf", 64)
        pg.display.set_caption(f"{self.title}-{self.clock.get_fps() :.1f}")
        self.load_gui_images()
        self.load_buttons()
        self.load_team_icons()

        enemy_sprite = Sprites(self.enemy.name, 0)
        enemy_level_text = self.font.render(f"Lv{self.enemy.level}", 0, BLACK)
        enemy_name_text = self.font.render(self.enemy.name, 0, BLACK)
        inicial_text = self.font.render(f"A LUCHAR CONTRA {self.enemy.name} !", 0, WHITE)


        while self.running:
            self.check_events()
            pos = pg.mouse.get_pos()
            mouse_press = pg.mouse.get_pressed()

            """
            Eleccion: El user elige que pokemon desea usar para asi cargar las imagenes/sprites necesarias para la self.interfaz
            """
            if self.interfaz == "eleccion":
                self.screen.blit(self.gui_img[1], (0,0))

                self.user_choice()
                
                eleccion_text = self.font.render("QUE POKEMON DESEA USAR?", 0, BLACK)
                self.screen.blit(eleccion_text, (50, 490))

                user_sprite = Sprites(self.user.name, 1)
                # user_name_text_black = self.font.render(self.user.name, 0, BLACK)
                user_name_text_white = self.font.render(self.user.name, 0, WHITE)
                # user_hp_text = self.font.render(f"{self.user.current_hp}/{self.user.hp}", 0, BLACK)
                # user_lvl_text = self.font.render(f"Lv{self.user.level}", 0, BLACK)

                # infos = [user_name_text_black, user_hp_text, user_lvl_text, enemy_name_text, enemy_level_text]

                normal = pg.image.load(DIR+"gui/normal.png")
                tipo = pg.image.load(f"{DIR}gui/{self.user.type.lower()}.png")

                first_att_text = self.font.render(f"{self.user.attacks[1].name}", 0, BLACK)
                first_att_button = Button(300, 486, first_att_text)
                # first_att_pp_text = self.font.render(f"{self.user.attacks[1].current_pp}/{self.user.attacks[1].pp}", 0, BLACK)

                scratch_text = self.font.render("ARANAZO", 0, BLACK)
                scratch_button = Button(80, 486, scratch_text)
                # scratch_pp_text = self.font.render(f"{self.user.attacks[0].current_pp}/{self.user.attacks[0].pp}", 0, BLACK)

                sprites = pg.sprite.RenderPlain(user_sprite, enemy_sprite)

            """
            Inicio: Presentacion de la batalla
            """
            if self.interfaz == "inicio":
                self.screen.blit(self.gui_img[0], (0,0))
                self.screen.blit(self.gui_img[2], (0, 448))
                self.screen.blit(inicial_text, (50, 490))
                sprites.draw(self.screen)  # Dibuja ambos sprites
                # Mueve los sprites como en el juego original
                user_sprite.update()
                enemy_sprite.update()
                # Crea boton invisible para pasar a la siguiente pantalla
                color = pg.Color(0,0,0,0)
                surface = pg.Surface((900, 136), pg.SRCALPHA)
                surface.fill(color)
                self.screen.blit(pg.transform.rotate(self.gui_img[-1], 45), (810, 480))
                cont = Button(30, 476, surface)
                if cont.draw(self.screen):
                    self.interfaz = "batalla"

            """
            Batalla: Pantalla principal de combate
            """
            if self.interfaz == "batalla":
                pg.event.wait()
                self.screen.blit(self.gui_img[3], (0, 448))
                battle_text = self.font.render("QUE DEBERIA HACER", 0, WHITE)
                self.screen.blit(battle_text, (65, 490))
                self.screen.blit(user_name_text_white, (65, 550))

                self.show_info(self.screen)

                # Accion e interaccion de botones
                self.buttons[0].active(self.screen, self.gui_img[7], pos)
                if self.buttons[0].draw(self.screen):
                    self.interfaz = "ataques"
                self.buttons[1].active(self.screen, self.gui_img[7], pos)
                if self.buttons[2].draw(self.screen):
                    print("Se ha abierto la mochila!")
                    # self.interfaz = "mochila"
                self.buttons[2].active(self.screen, self.gui_img[7], pos)
                if self.buttons[3].draw(self.screen):
                    self.interfaz = "pokemon"
                self.buttons[3].active(self.screen, self.gui_img[7], pos)
                if self.buttons[1].draw(self.screen):
                    print(f"{self.user.name} ha huido!")      
                    self.running = False

            """
            Ataques: Pantalla con diferentes ataques del pokemon + info
            """
            if self.interfaz == "ataques":
                #pg.event.wait()
                pp_text = self.font.render("PP", 0, BLACK)
                attack_text = self.font.render("TIPO/", 0, BLACK)
                self.screen.blit(self.gui_img[4], (0, 448))
                self.screen.blit(pp_text, (670, 488))
                self.screen.blit(attack_text, (670, 556))
                
                first_attack_pp_text, scratch_pp_text = self.show_info(self.screen)

                scratch_button.active(self.screen, self.gui_img[7], pos)
                if scratch_button.rect.colliderect(pos[0], pos[1], 1, 1):
                    self.screen.blit(normal, (770, 558))
                    self.screen.blit(scratch_pp_text, (770, 486))
                
                if scratch_button.draw(self.screen):
                    enemy_hp, damage = self.user.attack_user(self.enemy, self.user.attacks[0])
                    enemy_hp_pixels = self.loss_hp(damage, self.enemy, enemy_hp_pixels)
                    self.gui_img[-5] = pg.transform.scale(self.gui_img[-5], (enemy_hp_pixels, 12))
                    first_attack_pp_text, scratch_pp_text = self.show_info(self.screen)
                    self.interfaz = "batalla"
                    if enemy_hp == 0:
                        time.sleep(0.5)
                        self.interfaz = "user_win"
                    else:
                        user_hp, damage = self.enemy.attack_cpu(self.user)
                        user_hp_pixels = self.loss_hp(damage, self.user, user_hp_pixels)
                        self.gui_img[-4] = pg.transform.scale(self.gui_img[-4], (user_hp_pixels, 12))
                        first_attack_pp_text, scratch_pp_text = self.show_info(self.screen)
                        self.interfaz = "batalla"
                        if user_hp == 0:
                            time.sleep(0.5)
                            self.interfaz = "enemy_win"
                    
                
                first_att_button.active(self.screen, self.gui_img[7], pos)
                if first_att_button.rect.colliderect(pos[0], pos[1], 1, 1):
                    self.screen.blit(tipo, (770, 558))
                    self.screen.blit(first_attack_pp_text, (770, 486))
                
                if first_att_button.draw(self.screen):
                    enemy_hp, damage = self.user.attack_user(self.enemy, self.user.attacks[1])
                    enemy_hp_pixels = self.loss_hp(damage, self.enemy, enemy_hp_pixels)
                    self.gui_img[-5] = pg.transform.scale(self.gui_img[-5], (enemy_hp_pixels, 12))
                    first_attack_pp_text, scratch_pp_text = self.show_info(self.screen)
                    self.interfaz = "batalla"
                    if enemy_hp == 0:
                        time.sleep(0.5)
                        self.interfaz = "user_win"
                    else:
                        user_hp, damage = self.enemy.attack_cpu(self.user)
                        user_hp_pixels = self.loss_hp(damage, self.user, user_hp_pixels)
                        self.gui_img[-4] = pg.transform.scale(self.gui_img[-4], (user_hp_pixels, 12))
                        first_attack_pp_text, scratch_pp_text = self.show_info(self.screen)
                        self.interfaz = "batalla"
                        if user_hp == 0:
                            time.sleep(0.5)
                            self.interfaz = "enemy_win"
                    
                if mouse_press[2]:
                    self.interfaz = "batalla"
            """
            Mochila: Pantala con objetos utilizables, pociones, etc
            """
            if self.interfaz == "mochila":
                pass
            """
            Pokemon: Regresa a la pantalla de eleccion para cambiar de pokemon
            """
            if self.interfaz == "pokemon":
                self.interfaz = "eleccion"
            """
            Caso que la vida del rival llegue a 0
            """
            if self.interfaz == "user_win":
                print("User Wins")
                self.running = False
            """
            Caso que la vida del user llegue a 0
            """
            if self.interfaz == "enemy_win":
                print("Enemy Wins")
                self.running = False

            self.clock.tick(FPS)
            pg.display.flip()
        pg.quit()



if __name__=="__main__":
    game = Game()
    game.main()