# Bot Factory Trivia

## Overview
Bot Factory Trivia is a simple trivia game bot for Discord. It allows users to participate in a trivia game by answering questions and tracking their scores.

## Features
- Start a trivia game with a random question.
- Submit answers to questions.
- Check your current score.

## Commands

### Start a Trivia Game
- **Command:** `!trivia`
- **Description:** Starts a new trivia game and sends a random trivia question to the channel.
- **Example Usage:** `!trivia`

### Submit an Answer
- **Command:** `!answer [your_answer]`
- **Description:** Submits an answer for the current trivia question. If the answer is correct, it updates the player's score.
- **Example Usage:** `!answer Paris`

### Check Your Score
- **Command:** `!score`
- **Description:** Displays the current score of the user who invoked the command.
- **Example Usage:** `!score`

## Installation

To use Bot Factory Trivia, go to [this Replit link](https://replit.com/@calestialashley/Bot-Factory-Trivia?s=app) where the bot is hosted.

## Configuration

- **Trivia Questions:** Modify the `trivia_questions` dictionary in `bot.py` to add or change questions and answers.

## Contributing

Feel free to contribute by opening issues or submitting pull requests to enhance the trivia game.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
