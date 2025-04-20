# Discord Bot

## Installation

- 新增一個 python 的 virtual environment，並開啟 virtual environment.

```bash
python -m venv .venv

source .venv/bin/activate
```

- 安裝套件

```bash
pip install -r requirements.txt
```

## Execute discord bot

專案的根目錄需有一個 `.env` 的檔案，檔案內需有 discord 的 token，例如：

`DISCORD_BOT_TOKEN=[token]`

執行程式

```bash
python project.py
```

## nAnB game

我的 Discord Bot 可以玩猜數字的遊戲，為了方便測試，這個遊戲可以直接用 terminal 測試，不需透過連結 Discord。測試方式如下：

單人版

```bash
python nAnB_game.py
```

多人版

```bash
python multi_player.py
```