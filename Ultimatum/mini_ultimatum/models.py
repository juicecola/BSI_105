from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer

class Constants(BaseConstants):
    name_in_url = 'mini_ultimatum_game'
    players_per_group = 3
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Player 1's fields
    endowment = models.CurrencyField(initial=200)
    amount_sent = models.CurrencyField(min=0, max=200)

    # Player 3's fields
    punish = models.BooleanField(
        choices=[
            [False, 'Not Punish'],
            [True, 'Punish']
        ],
        widget=models.RadioSelect,
        label="Do you want to punish Player 1?",
        blank=True,
    )

    def set_payoffs(self):
        if self.punish:
            self.payoff = 0
        else:
            self.payoff = self.endowment - self.amount_sent
            self.group.get_player_by_role('Player 2').payoff = self.amount_sent

