# medicine_project

> A command-line tool to help users manage and track their medication usage effectively.

---

## Features

- **Track multiple medications**: Supports different dosages and variants of the same medicine.
- **Auto-calculate depletion date**: Automatically calculates when a medicine will run out.
- **Dose-based computations**: Computes daily usage, mg totals, and remaining supply.
- **Test coverage**: Unit tests for core logic ensure reliability.
- **JSON storage**: Reads and writes data from a flat `data.json` file.
- **CLI-driven interface**: Text-based interface that guides user interaction.

---

## Project Structure

```
medicine_project/
├── src/medicine/         # Main logic
│   ├── main.py           # CLI runner
│   ├── medicine.py       # Medicine class
│   ├── functions_*.py    # Core functionality: time, user, files, medicines
│   └── data.json         # Medication data
├── tests/                # Unit tests
├── README.md             # You're here
├── requirements.txt      # Dependencies
├── setup.py              # Install as a package
├── TODO.md / IDEAS.md    # Roadmap and ideas
```

---

## Installation

### Prerequisites:

- Python 3.10+
- (Optional) [virtualenv](https://virtualenv.pypa.io/en/latest/)

### Install the project:

```bash
pip install -e .
```

### Run the CLI:

```bash
python src/medicine/main.py
# or if installed
medicine
```

---

## Usage

After launching the CLI, you can:

1. Check all medicine info
2. Check a single medicine
3. Add pills
4. Change daily dose
5. Create medicine (planned)
6. Remove medicine

Example interaction:

```
Give name of medicine: paracetamol_500
Give amount of pills: 20
> Pills successfully added.
```

---

## Running Tests

```bash
pytest tests/
```

Test cases exist for:

- Medicine class initialization
- Dose-related calculations
- (Work in progress) Coverage for all user functions

---

## Future Plans

Check `TODO.md` and `IDEAS.md` for live roadmap.
Highlights:

- History tracking
- Logging
- Improved user input handling
- Export to CSV or other formats

---

## Contribution

Pull requests and ideas welcome. Use Issues to report bugs or propose enhancements.

---

## License

MIT License (add license file if needed)

---

## Author

Created by [iwodud](https://github.com/iwodud)
