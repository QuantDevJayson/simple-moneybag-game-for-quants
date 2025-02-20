#### simple-moneybag-game-for-quants

### Simple MoneyBag Game For Quants

#### Overview
Simple MoneyBag Game For Quants is an interactive investment quiz game designed for quantitative finance enthusiasts. Players answer investment-related multiple-choice questions and are rewarded or penalized based on their accuracy. The game incorporates tongue twisters as a redemption mechanism and has a donation system for unmet targets.

## Rules of the Game
1. **Game Setup:**
   - Players set the number of rounds they want to play.<br>
   - Players set a target score to achieve.<br>

2. **Quiz Mechanics:**
   - A multiple-choice investment-related question is generated.<br>
   - Players select an answer from four options.<br>
   - If correct, they gain **+10 points**.<br>
   - If incorrect, they face a **-5 points** penalty.<br>

3. **Redemption Mechanism:**
   - Players can avoid the penalty by successfully reciting a randomly generated tongue twister.<br>
   - The system validates the speech input.<br>
   - If successful, no points are deducted.<br>
   - If unsuccessful, the penalty remains.<br>

4. **Winning and Donations:**
   - If a player reaches their target score within the set rounds, they win.<br>
   - If they fail to meet the target, they must donate **5 times the difference** between their score and target to a charitable cause.<br>

## Installation
1. Clone the repository:<br>
   ```bash
   git clone https://github.com/QuantDevJayson/simple-moneybag-game-for-quants.git 
   cd simple-moneybag-game-for-quants
   ```
2. Requirements<br>
   Ensure you have the following dependencies installed:<br>
            streamlit <br>
            openai <br>
            speechrecognition <br>
            pydub <br>
   ```
5. Run the game using Streamlit:<br>
   ```bash
   streamlit run imple-moneybag-game-for-quants.py
   ```

## Contributions
Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.<br>

## License
This project is licensed under the MIT License.

Enjoy the game, test your investment knowledge, and remember—quants can be generous! 🎉

