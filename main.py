import pygame
import sys
import random
import time

pygame.init()
pygame.mixer.init()

adminmode = "false"

print("Do not close the program while cracking!")
time.sleep(0.5)
print("Creator(s): CLOUD_STUDIOS_09 & Copilot (Microsoft AI)")
time.sleep(0.1)
print("Copyright 2025")
time.sleep(0.1)
print("Published on Github")
print("Hardware required: ")
print("-------------------")
print("Processor: 1.50 GHz or higher")
time.sleep(0.1)
print("RAM: 6GB DDR3 or higher")
time.sleep(0.1)
print("SSD: 64 GB HDD, SSD, NVME")
time.sleep(0.1)
print("GPU: Optional")
time.sleep(0.1)
print("OS Desktop: Windows: Vista or higher, MacOS: 16 or higher, Linux: Ubuntu or Kali")
time.sleep(0.1)
print("OS Phone: Android 10 or higher, iOS 16 or higher, HarmonyOS 6 or higher")
time.sleep(0.5)
print("Loading: Password Cracker...")
username = input("Username: ")
if username == "CLOUD_STUDIOS_09":
    print("Admin mode activated!")
    admincode = "010101111010110101011001010111101011010101100101011110101101010110010101111010110101011001010111101011010101100101011110101101010110"
    admincodeguess = input("Admin code: ")
    if admincodeguess == admincode:
        adminmode = "true"
        print("Succesfully entered admin panel! (exepanel.v1)")
        print("Admin panel:")
        print("------------")
        print("#1 - Edit Code")
        print("#2 - Kick Usernames")
        choice = input("Choice: ")
        if choice == "1":
            print("#1-Edit Code")
            print("------------")
            input(">>> ")
        elif choice == "2":
            print("#2-Kick Username")
            print("----------------")
            usernameban = input("Username to kick: ")
            if usernameban == username:
                print("Username banned succesfully")
            else:
                print("Username doesnt exist yet or is not online right now :(")
        else:
            print("Invalid choice :(")
    else:
        print("Code not correct :(")
else:
    print("Checking...")
run = input("Are you sure you have the hardware requirements above here? Run it(Yes/No): ")
if run == "Yes":
    time.sleep(1)
    try:
        WIDTH, HEIGHT = 400, 250
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Password Cracker v2.1")
    except pygame.error or IndexError:
        print("Error: Could not initialize: pygame.init(), pygame.mixer.init()")
    try:
        BACKGROUND = (15, 15, 15)
        TEXT_COLOR = (0, 255, 0)
        BOX_COLOR = (40, 40, 40)
        BUTTON_COLOR = (0, 120, 0)
        PROGRESS_BG = (60, 60, 60)
        PROGRESS_FILL = (0, 255, 0)
    except pygame.error or IndexError:
        print("Error: Could not import: BACKGROUND, TEXT_COLOR, BOX_COLOR, BUTTON_COLOR, PROGRESS_BG, PROGRESS_FILL")

    try:
        font = pygame.font.Font(None, 14)
        title_font = pygame.font.Font(None, 21)
        console_font = pygame.font.Font(pygame.font.match_font('couriernew', bold=True), 20)
    except pygame.error:
        print("Error: Something went wrong while setting up the text fonts")

    try:    
        input_box = pygame.Rect(125, 60, 150, 20)
        ip_box = pygame.Rect(125, 85, 150, 20)
        ok_button = pygame.Rect(285, 60, 40, 20)
        generate_button = pygame.Rect(125, 110, 100, 20)
        copy_button = pygame.Rect(235, 110, 40, 20)
        dropdown_box = pygame.Rect(125, 135, 100, 15)
        dropdown_open = False
        dropdown_options = ["Strong", "Creative"]
        selected_option = "Creative"
    except pygame.error:
        print("Error: Something went wrong while loading the buttons")

    try:
        start_button = pygame.Rect(150, 100, 100, 25)
        settings_button = pygame.Rect(150, 135, 100, 25)
        exit_button = pygame.Rect(150, 170, 100, 25)
        back_button = pygame.Rect(25, 210, 50, 20)
    except pygame.error:
        print("Error: Something went wrong while loading the buttons")

    try:
        color = BOX_COLOR
        active_input = False
        active_ip = False
        text = ""
        ip_address = "192.83.245.17" + "/" + username
        cracking = False
        guessed = ""
        progress = 0
        log_lines = []
        current_screen = "splash"
        sound_enabled = True
        splash_alpha = 0
        splash_timer = pygame.time.get_ticks()
    except pygame.error:
        print("Error: Something went wrong while importing: IP, Sound(s), Timer")

    clock = pygame.time.Clock()

    try:
        crack_sound = pygame.mixer.Sound("crack.wav")
    except:
        crack_sound = None

    def generate_password(length=12):
        charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()+=-_<>"
        return ''.join(random.choice(charset) for _ in range(length))

    def generate_ai_password():
        adjectives = ["Quantum", "Silent", "Neon", "Echo", "Cyber", "Frozen", "Rapid", "Fire", "Mighty", "Red", "Blue", "Yellow", "Green", "Galaxy", "Star", "Solar"]
        nouns = ["Tiger", "Storm", "Blade", "Falcon", "Ghost", "Matrix", "Shadow", "King", "Tree", "Car", "Coin", "Money", "Newspaper", "Street"]
        symbols = ["!", "@", "#", "$", "-", "_", "%", "()"]
        number = str(random.randint(10, 99))
        return random.choice(adjectives) + random.choice(symbols) + random.choice(nouns) + number

    def add_to_log(message):
        log_lines.append(message)
        if len(log_lines) > 10:
            log_lines.pop(0)

    def draw_console_log():
        y = 320
        for line in log_lines:
            log_surface = console_font.render(line, True, TEXT_COLOR)
            screen.blit(log_surface, (50, y))
            y += 22

    def draw_progress_bar(current, total):
        bar_x, bar_y = 125, 150
        bar_width, bar_height = 150, 10
        fill_width = int((current / total) * bar_width)
        pygame.draw.rect(screen, PROGRESS_BG, (bar_x, bar_y, bar_width, bar_height), border_radius=5)
        pygame.draw.rect(screen, PROGRESS_FILL, (bar_x, bar_y, fill_width, bar_height), border_radius=5)

    def crack_password(target):
        global guessed, progress
        guessed = ""
        charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        for i in range(len(target)):
            while True:
                guess_char = random.choice(charset)
                guessed = guessed[:i] + guess_char + guessed[i+1:]
                progress = i + 1
                draw_crack_screen()
                pygame.display.flip()
                time.sleep(0.05)
                if sound_enabled and crack_sound:
                    crack_sound.stop()
                    crack_sound.play()
                add_to_log(f"Trying: {guessed}")
                if guess_char == target[i]:
                    break
        add_to_log(f"Password cracked: {guessed}")

    def draw_button(rect, text):
        pygame.draw.rect(screen, BUTTON_COLOR, rect, border_radius=5)
        label = font.render(text, True, BACKGROUND)
        screen.blit(label, (rect.x + 10, rect.y + 8))

    def draw_dropdown():
        pygame.draw.rect(screen, BOX_COLOR, dropdown_box, border_radius=5)
        label = font.render(selected_option, True, TEXT_COLOR)
        screen.blit(label, (dropdown_box.x + 10, dropdown_box.y + 5))
        if dropdown_open:
            for i, option in enumerate(dropdown_options):
                opt_rect = pygame.Rect(dropdown_box.x, dropdown_box.y + 15 + i * 15, 100, 15)
                pygame.draw.rect(screen, BOX_COLOR, opt_rect, border_radius=5)
                opt_label = font.render(option, True, TEXT_COLOR)
                screen.blit(opt_label, (opt_rect.x + 10, opt_rect.y + 5))

    def draw_splash():
        global splash_alpha
        screen.fill(BACKGROUND)
        splash = title_font.render("Password Cracker v2.1", True, TEXT_COLOR)
        splash.set_alpha(splash_alpha)
        screen.blit(splash, (WIDTH // 2 - splash.get_width() // 2, HEIGHT // 2 - 80))
        if splash_alpha < 255:
            splash_alpha += 3
        elif pygame.time.get_ticks() - splash_timer > 2000:
            return "menu"
        return "splash"

    def draw_menu():
        screen.fill(BACKGROUND)
        title = title_font.render("Password Cracker v2.1", True, TEXT_COLOR)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
        draw_button(start_button, "Start Cracking")
        draw_button(settings_button, "Settings")
        draw_button(exit_button, "Close")

    def draw_settings():
        screen.fill(BACKGROUND)
        title = title_font.render("Settings", True, TEXT_COLOR)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 80))
        sound_text = font.render(f"Music: {'On' if sound_enabled else 'Off'}", True, TEXT_COLOR)
        screen.blit(sound_text, (150, 100))
        ip_text = font.render(f"IP: {ip_address}", True, TEXT_COLOR)
        screen.blit(ip_text, (150, 125))
        draw_button(back_button, "Back")

    def draw_crack_screen():
        screen.fill(BACKGROUND)
        title = title_font.render("Password Cracker v2.1", True, TEXT_COLOR)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 15))
        pygame.draw.rect(screen, color, input_box, border_radius=5)
        pygame.draw.rect(screen, color, ip_box, border_radius=5)
        draw_button(ok_button, "OK")
        draw_button(generate_button, "Generate")
        draw_button(copy_button, "Copy")
        draw_dropdown()
        draw_button(back_button, "Back")

        screen.blit(font.render("Password:", True, TEXT_COLOR), (input_box.x - 100, input_box.y + 8))
        screen.blit(font.render("IP-adres:", True, TEXT_COLOR), (ip_box.x - 100, ip_box.y + 8))

        display_text = guessed if cracking else text
        screen.blit(font.render(display_text, True, TEXT_COLOR), (input_box.x + 10, input_box.y + 8))
        screen.blit(font.render(ip_address, True, TEXT_COLOR), (ip_box.x + 10, ip_box.y + 8))

        if cracking:
            draw_progress_bar(progress, len(text))
            draw_console_log()

    print("Loaded: Password Cracker!")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if current_screen == "splash":
                    continue

                elif current_screen == "menu":
                    if start_button.collidepoint(event.pos):
                        current_screen = "crack"
                    elif settings_button.collidepoint(event.pos):
                        current_screen = "settings"
                    elif exit_button.collidepoint(event.pos):
                        running = False

                elif current_screen == "settings":
                    if back_button.collidepoint(event.pos):
                        current_screen = "menu"
                    elif pygame.Rect(150, 100, 100, 15).collidepoint(event.pos):
                        sound_enabled = not sound_enabled

                elif current_screen == "crack":
                    if input_box.collidepoint(event.pos):
                        active_input = True
                        active_ip = False
                    elif ip_box.collidepoint(event.pos):
                        active_ip = True
                        active_input = False
                    else:
                        active_input = active_ip = False

                    if ok_button.collidepoint(event.pos) and not cracking and text:
                        cracking = True
                        add_to_log(f"Connecting to {ip_address}...")
                        add_to_log("Handshake complete.")
                        add_to_log(f"Starting brute-force on '{text}'...")
                        crack_password(text)

                    if generate_button.collidepoint(event.pos) and not cracking:
                        text = generate_ai_password() if selected_option == "Creative" else generate_password()

                    if copy_button.collidepoint(event.pos) and text:
                        if pygame.scrap.get_init():
                            pygame.scrap.put(pygame.SCRAP_TEXT, text.encode())
                            add_to_log("Password Copied!.")
                        else:
                            add_to_log("Clipboard not available.")

                    if dropdown_box.collidepoint(event.pos):
                        dropdown_open = not dropdown_open
                    elif dropdown_open:
                        for i, option in enumerate(dropdown_options):
                            opt_rect = pygame.Rect(dropdown_box.x, dropdown_box.y + 15 + i * 15, 100, 15)
                            if opt_rect.collidepoint(event.pos):
                                selected_option = option
                                dropdown_open = False

                    if back_button.collidepoint(event.pos):
                        current_screen = "menu"
                        text = ""
                        guessed = ""
                        cracking = False
                        progress = 0
                        log_lines.clear()

            elif event.type == pygame.KEYDOWN:
                if current_screen == "crack" and not cracking:
                    if active_input:
                        if event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                    elif active_ip:
                        if event.key == pygame.K_BACKSPACE:
                            ip_address = ip_address[:-1]
                        else:
                            ip_address += event.unicode

        if current_screen == "splash":
            current_screen = draw_splash()
        elif current_screen == "menu":
            draw_menu()
        elif current_screen == "settings":
            draw_settings()
        elif current_screen == "crack":
            draw_crack_screen()

        pygame.display.flip()
        clock.tick(60)

    pygame.surface.quit()
    pygame.quit()
    sys.exit()

else:
    while True:
        running = False
        break
