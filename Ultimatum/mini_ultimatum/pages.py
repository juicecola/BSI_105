from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Player1Page(Page):
    form_model = 'player'
    form_fields = ['amount_sent']  # Form field for Player 1 to input the amount to send

    def vars_for_template(self):
        return {
            'endowment': self.player.endowment,
        }

class Player3Page(Page):
    form_model = 'player'
    form_fields = ['punish']  # Form field for Player 3 to choose to punish or not

    def vars_for_template(self):
        return {
            'amount_sent': self.group.get_player_by_role('Player 1').amount_sent,
        }

class ResultsPage(Page):
    def vars_for_template(self):
        player = self.player
        group = self.group

        return {
            'amount_sent': player.amount_sent,
            'punish': 'Punish' if player.punish else 'Not Punish',
            'player1_payout': player.payoff,
            'player2_payout': group.get_player_by_role('Player 2').payoff,
        }

page_sequence = [Player1Page, Player3Page, ResultsPage]

