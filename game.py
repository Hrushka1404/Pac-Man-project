class Game:


    def show_score(self, score):
        score = font.render(f'{score}', True, text_color)
        screen.blit(score, (400, 500))

    def show_game_over():
        text = big_font.render('GAME OVER', True, 'red')
        screen.blit(text, (0, 0))

    def game_over(self):
        message = self.game_over_font.render(f'GAME OVER!!', True, pygame.Color("chartreuse"))
        self.screen.blit(message, ((WIDTH // 4), (HEIGHT // 3)))

