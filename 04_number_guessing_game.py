{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPkr4Ai/c+2ZWD0kK9kYzRK",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/TYS-SQL/fun-python-projects/blob/main/04_number_guessing_game.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "eosGag-um_6Q"
      },
      "outputs": [],
      "source": [
        "import random\n",
        "\n",
        "print(\"🎲 Welcome to the Number Guessing Game!\")\n",
        "print(\"I'm thinking of a number between 1 and 100. Can you guess it?\")\n",
        "\n",
        "number_to_guess = random.randint(1, 100)\n",
        "\n",
        "attempts = 0\n",
        "max_attempts = 10\n",
        "\n",
        "while attempts < max_attempts:\n",
        "    try:\n",
        "        guess = int(input(f\"Attempt {attempts + 1}/{max_attempts} - Enter your guess: \"))\n",
        "    except ValueError:\n",
        "        print(\"Please enter a valid number.\")\n",
        "        continue\n",
        "\n",
        "    attempts += 1\n",
        "\n",
        "    if guess < number_to_guess:\n",
        "        print(\"Too low! Try again.\")\n",
        "    elif guess > number_to_guess:\n",
        "        print(\"Too high! Try again.\")\n",
        "    else:\n",
        "        print(f\"🎉 Congratulations! You guessed the number {number_to_guess} correctly in {attempts} attempts!\")\n",
        "        break\n",
        "else:\n",
        "    print(f\"😞 Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}. Better luck next time!\")\n",
        "\n",
        "print(\"Thanks for playing! 😊\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "code = '''import random\n",
        "\n",
        "print(\"🎲 Welcome to the Number Guessing Game!\")\n",
        "print(\"I'm thinking of a number between 1 and 100. Can you guess it?\")\n",
        "\n",
        "number_to_guess = random.randint(1, 100)\n",
        "\n",
        "attempts = 0\n",
        "max_attempts = 10\n",
        "\n",
        "while attempts < max_attempts:\n",
        "    try:\n",
        "        guess = int(input(f\"Attempt {attempts + 1}/{max_attempts} - Enter your guess: \"))\n",
        "    except ValueError:\n",
        "        print(\"Please enter a valid number.\")\n",
        "        continue\n",
        "\n",
        "    attempts += 1\n",
        "\n",
        "    if guess < number_to_guess:\n",
        "        print(\"Too low! Try again.\")\n",
        "    elif guess > number_to_guess:\n",
        "        print(\"Too high! Try again.\")\n",
        "    else:\n",
        "        print(f\"🎉 Congratulations! You guessed the number {number_to_guess} correctly in {attempts} attempts!\")\n",
        "        break\n",
        "else:\n",
        "    print(f\"😞 Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}. Better luck next time!\")\n",
        "\n",
        "print(\"Thanks for playing! 😊\")\n",
        "'''\n",
        "\n",
        "with open('04_number_guessing_game.py', 'w') as f:\n",
        "    f.write(code)\n",
        "\n",
        "print(\"Saved your code as 04_number_guessing_game.py\")\n"
      ],
      "metadata": {
        "id": "ZoiFxmsdnXGr"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}