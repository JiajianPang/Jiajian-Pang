import random

class MotivationEngine:
    # A collection of motivational quotes to display during study sessions
    quotes = [
        "Don't stop now—every hour counts! 🔥",
        "Visualize your high score and keep going! 📈",
        "You're not alone—let's work hard together! 👊",
        "A little bit of study each day keeps exam stress away! 📘",
        "The future you will thank you for studying today. 💡"
    ]

    @staticmethod
    def get_daily_quote():
        """
        Return a randomly selected motivational quote.
        :return: String
        """
        return random.choice(MotivationEngine.quotes)

